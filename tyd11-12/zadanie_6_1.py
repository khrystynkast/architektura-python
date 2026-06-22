import os
import json
from datetime import datetime
from dataclasses import dataclass
from typing import Callable
import pandas as pd

@dataclass
class Rule:
    name: str
    check: Callable[[pd.DataFrame], dict]
    severity: str = "warning"

class DataContract:
    def __init__(self, name: str):
        self.name = name
        self.rules: list[Rule] = []
        
    def add_rule(self, name: str, check: Callable[[pd.DataFrame], dict], severity: str = "warning"):
        self.rules.append(Rule(name=name, check=check, severity=severity))

class DataValidator:
    def __init__(self, contract: DataContract):
        self.contract = contract
        
    def validate(self, df: pd.DataFrame) -> dict:
        report = {
            "contract_name": self.contract.name,
            "timestamp": datetime.now().isoformat(),
            "results": {}
        }
        
        for rule in self.contract.rules:
            res = rule.check(df)
            
            report["results"][rule.name] = {
                "passed": bool(res["passed"]),
                "severity": rule.severity,
                "details": str(res["details"])
            }
            
            if not res["passed"] and rule.severity == "error":
                raise ValueError(f"KRYTYCZNY BŁĄD JAKOŚCI DANYCH: Reguła '{rule.name}' nie przeszła walidacji! {res['details']}")
                
        return report

if __name__ == "__main__":
    data = {
        "text": [
            "This movie was absolutely amazing and wonderful!", 
            "Worst film ever. Total waste of precious time.", 
            "Short text <br> with some HTML tags inside.",
            "An interesting story but poor acting.",
            "Loved it! Best cinema experience this year."
        ],
        "label": [1, 0, 0, 0, 1]
    }
    df_imdb = pd.DataFrame(data)
    df_imdb["word_count"] = df_imdb["text"].str.split().str.len()

    imdb_contract = DataContract("IMDB Quality Contract")

    def check_no_nulls(df):
        nulls = df[["text", "label"]].isnull().sum().sum()
        return {"passed": bool(nulls == 0), "details": f"Znaleziono {nulls} wartości NULL."}
    imdb_contract.add_rule("no_nulls", check_no_nulls, severity="error")

    def check_labels_in_set(df):
        invalid_labels = df[~df["label"].isin([0, 1])].shape[0]
        return {"passed": bool(invalid_labels == 0), "details": f"Liczba etykiet spoza zbioru {{0, 1}}: {invalid_labels}."}
    imdb_contract.add_rule("labels_in_set", check_labels_in_set, severity="error")

    def check_min_word_count(df):
        too_short = df[df["word_count"] < 5].shape[0]
        return {"passed": bool(too_short == 0), "details": f"Znaleziono {too_short} recenzji mających mniej niż 5 słów."}
    imdb_contract.add_rule("min_word_count", check_min_word_count, severity="error")

    def check_max_word_count(df):
        too_long = df[df["word_count"] > 2000].shape[0]
        return {"passed": bool(too_long == 0), "details": f"Znaleziono {too_long} recenzji mających ponad 2000 słów."}
    imdb_contract.add_rule("max_word_count", check_max_word_count, severity="error")

    def check_no_duplicates(df):
        dups = df["text"].duplicated().sum()
        return {"passed": bool(dups == 0), "details": f"Liczba zduplikowanych tekstów: {dups}."}
    imdb_contract.add_rule("no_duplicates", check_no_duplicates, severity="error")

    def check_class_balance(df):
        counts = df["label"].value_counts()
        if len(counts) < 2 or counts.min() == 0:
            return {"passed": False, "details": "Brak reprezentacji jednej z klas."}
        ratio = counts.max() / counts.min()
        passed = 0.5 <= ratio <= 1.5
        return {"passed": bool(passed), "details": f"Stosunek klas wynosi {ratio:.2f} (wymagany przedział: [0.5, 1.5])."}
    imdb_contract.add_rule("class_balance", check_class_balance, severity="error")

    def check_no_html_tags(df):
        has_html = df["text"].str.contains(r"<[^>]+>", regex=True).sum()
        return {"passed": bool(has_html == 0), "details": f"Znaleziono {has_html} recenzji zawierających tagi HTML."}
    imdb_contract.add_rule("no_html_tags", check_no_html_tags, severity="warning")

    validator = DataValidator(imdb_contract)

    try:
        final_report = validator.validate(df_imdb)
    except ValueError as e:
        final_report = {
            "contract_name": imdb_contract.name,
            "timestamp": datetime.now().isoformat(),
            "status": "FAILED_FAST",
            "error_message": str(e)
        }

    os.makedirs("workspace", exist_ok=True)
    report_path = "workspace/data_quality_report.json"

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(final_report, f, indent=4, ensure_ascii=False)