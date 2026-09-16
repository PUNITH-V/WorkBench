import json
from pathlib import Path

from app.schemas.research import ResearchReport


OUTPUT_PATH = Path("output/research_report.json")


def save_report(report: ResearchReport) -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_PATH.open("w", encoding="utf-8") as file:
        json.dump(
            report.model_dump(),
            file,
            indent=2,
            ensure_ascii=False,
        )

    print(f"\nReport saved to {OUTPUT_PATH}")