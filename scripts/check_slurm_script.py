"""Check a SLURM script for common teaching-workflow requirements."""
from __future__ import annotations

import argparse
from pathlib import Path
import re


REQUIRED_DIRECTIVES = [
    "job-name",
    "output",
    "error",
    "time",
    "ntasks",
    "cpus-per-task",
    "mem",
]


def check_script(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    findings: list[str] = []

    for directive in REQUIRED_DIRECTIVES:
        pattern = re.compile(rf"^#SBATCH --{re.escape(directive)}=", re.MULTILINE)
        if not pattern.search(text):
            findings.append(f"missing #SBATCH --{directive}=...")

    if "set -euo pipefail" not in text:
        findings.append("missing strict shell mode: set -euo pipefail")

    if "mkdir -p logs" not in text and "logs/" in text:
        findings.append("logs are referenced but mkdir -p logs was not found")

    if re.search(r"^python\s+", text, flags=re.MULTILINE) and "module load" not in text and "activate" not in text:
        findings.append("python command found without an environment setup comment or command")

    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    findings = check_script(args.path)
    if findings:
        for finding in findings:
            print(f"WARNING: {finding}")
        raise SystemExit(1)
    print(f"OK: {args.path}")


if __name__ == "__main__":
    main()
