"""Summarise a small CSV export of SLURM accounting data."""
from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def parse_memory_to_mb(value: str) -> float | None:
    if not value or value == "Unknown":
        return None
    units = {"K": 1 / 1024, "M": 1, "G": 1024, "T": 1024 * 1024}
    suffix = value[-1].upper()
    if suffix not in units:
        return None
    try:
        return float(value[:-1]) * units[suffix]
    except ValueError:
        return None


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def summarize(rows: list[dict[str, str]]) -> dict[str, object]:
    states = Counter(row.get("State", "UNKNOWN") for row in rows)
    memory_values = [
        parsed
        for row in rows
        if (parsed := parse_memory_to_mb(row.get("MaxRSS", ""))) is not None
    ]
    allocated_cpus = [int(row["AllocCPUS"]) for row in rows if row.get("AllocCPUS", "").isdigit()]
    return {
        "jobs": len(rows),
        "states": dict(states),
        "max_memory_mb": max(memory_values) if memory_values else None,
        "total_alloc_cpus": sum(allocated_cpus),
    }


def format_summary(summary: dict[str, object]) -> str:
    lines = [f"Jobs: {summary['jobs']}"]
    states = summary["states"]
    if isinstance(states, dict):
        for state, count in sorted(states.items()):
            lines.append(f"{state}: {count}")
    if summary["max_memory_mb"] is not None:
        lines.append(f"Max memory: {summary['max_memory_mb']:.1f} MB")
    lines.append(f"Total allocated CPUs: {summary['total_alloc_cpus']}")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    summary = summarize(load_rows(args.path))
    print(format_summary(summary))


if __name__ == "__main__":
    main()

