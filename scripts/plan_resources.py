"""Recommend conservative SLURM resource requests from small observation data."""
from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


def round_up(value: float, step: int) -> int:
    return int(math.ceil(value / step) * step)


def load_completed_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return [row for row in rows if row.get("State") == "COMPLETED"]


def recommend(rows: list[dict[str, str]], *, time_factor: float = 1.5, memory_factor: float = 1.5) -> dict[str, object]:
    if not rows:
        raise ValueError("no completed rows available for recommendation")

    elapsed = [int(row["ElapsedSeconds"]) for row in rows]
    memory = [float(row["MaxRSSMB"]) for row in rows]
    cpus = [int(row["AllocCPUS"]) for row in rows]

    requested_seconds = round_up(max(elapsed) * time_factor, 60)
    requested_memory_mb = round_up(max(memory) * memory_factor, 256)

    return {
        "time": seconds_to_slurm_time(requested_seconds),
        "memory": f"{requested_memory_mb}M",
        "cpus_per_task": max(1, round(sum(cpus) / len(cpus))),
        "evidence_jobs": len(rows),
    }


def seconds_to_slurm_time(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{remaining:02d}"


def format_recommendation(result: dict[str, object]) -> str:
    return "\n".join(
        [
            f"Evidence jobs: {result['evidence_jobs']}",
            f"Recommended --time={result['time']}",
            f"Recommended --mem={result['memory']}",
            f"Recommended --cpus-per-task={result['cpus_per_task']}",
        ]
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--time-factor", type=float, default=1.5)
    parser.add_argument("--memory-factor", type=float, default=1.5)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = recommend(load_completed_rows(args.path), time_factor=args.time_factor, memory_factor=args.memory_factor)
    print(format_recommendation(result))


if __name__ == "__main__":
    main()
