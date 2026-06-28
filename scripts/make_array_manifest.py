"""Create a small CSV manifest for SLURM job-array examples."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path


def build_rows(count: int, mode: str, start_seconds: int) -> list[dict[str, object]]:
    if count < 1:
        raise ValueError("count must be at least 1")
    rows: list[dict[str, object]] = []
    for task_id in range(count):
        rows.append(
            {
                "task_id": task_id,
                "mode": mode,
                "seconds": start_seconds + task_id,
                "megabytes": 64 * (task_id + 1),
                "files": 5 * (task_id + 1),
                "label": f"{mode}-{task_id:03d}",
            }
        )
    return rows


def write_manifest(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["task_id", "mode", "seconds", "megabytes", "files", "label"])
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("data/generated_manifest.csv"))
    parser.add_argument("--count", type=int, default=6)
    parser.add_argument("--mode", choices=("cpu", "memory", "io"), default="cpu")
    parser.add_argument("--start-seconds", type=int, default=1)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = build_rows(args.count, args.mode, args.start_seconds)
    write_manifest(args.output, rows)
    print(f"Wrote {args.output} with {len(rows)} tasks")


if __name__ == "__main__":
    main()
