import functools
import time
import json
import random
import hashlib
from pathlib import Path

WORKDIR = Path(".")

def retry(max_attempts: int = 3, delay: float = 0.1, backoff: float = 2.0):
    """Ponawia wywołanie funkcji przy wyjątku, z exponential backoff."""
    def opakuj(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_exc = exc
                    sleep_time = delay * (backoff ** attempt)
                    print(f"[retry] próba {attempt+1}/{max_attempts} nieudana: {exc}. "
                          f"czekam {sleep_time:.3f}s")
                    time.sleep(sleep_time)
            print("[retry] wszystkie próby nieudane — podnoszę wyjątek")
            raise last_exc
        return wrapper
    return opakuj

def cache_to_disk(cache_dir: Path):
    """Cachuje wynik funkcji do JSON na dysku."""
    cache_dir.mkdir(exist_ok=True, parents=True)

    def opakuj(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            raw_key = repr((args, kwargs)).encode("utf-8")
            key = hashlib.md5(raw_key).hexdigest()
            cache_file = cache_dir / f"{key}.json"

            if cache_file.exists():
                with open(cache_file, "r", encoding="utf-8") as f:
                    print(f"[cache_to_disk] HIT -> {cache_file.name}")
                    return json.load(f)

            result = func(*args, **kwargs)

            with open(cache_file, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)

            print(f"[cache_to_disk] MISS -> zapisano {cache_file.name}")
            return result

        return wrapper
    return opakuj

@cache_to_disk(WORKDIR / "flaky_cache")
@retry(max_attempts=5, delay=0.05)
def flaky_fetch(text_id: int) -> dict:
    if random.random() < 0.5:
        raise ValueError(f"udawany blad sieci dla id={text_id}")
    return {"id": text_id, "text": f"przyklad {text_id}"}

successes = 0
for i in range(100):
    try:
        flaky_fetch(i)
        successes += 1
    except Exception:
        pass

print(f"Sukcesy: {successes}/100")

p_theoretical = 1 - 0.5**5
p_theoretical
