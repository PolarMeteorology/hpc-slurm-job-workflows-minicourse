"""Render a simple SLURM script by replacing common resource directives."""
from __future__ import annotations

import argparse
from pathlib import Path
import re


DIRECTIVE_PATTERNS = {
    "job_name": re.compile(r"^#SBATCH --job-name=.*$", re.MULTILINE),
    "time": re.compile(r"^#SBATCH --time=.*$", re.MULTILINE),
    "ntasks": re.compile(r"^#SBATCH --ntasks=.*$", re.MULTILINE),
    "cpus_per_task": re.compile(r"^#SBATCH --cpus-per-task=.*$", re.MULTILINE),
    "mem": re.compile(r"^#SBATCH --mem=.*$", re.MULTILINE),
}


def replace_directive(text: str, key: str, value: str | int | None) -> str:
    if value is None:
        return text
    option = key.replace("_", "-")
    if key == "job_name":
        option = "job-name"
    if key == "cpus_per_task":
        option = "cpus-per-task"
    replacement = f"#SBATCH --{option}={value}"
    pattern = DIRECTIVE_PATTERNS[key]
    if not pattern.search(text):
        raise ValueError(f"Template does not contain directive for {key}")
    return pattern.sub(replacement, text)


def render(template: Path, output: Path, replacements: dict[str, str | int | None]) -> str:
    text = template.read_text(encoding="utf-8")
    for key, value in replacements.items():
        text = replace_directive(text, key, value)
    output.write_text(text, encoding="utf-8")
    return text


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--job-name", default=None)
    parser.add_argument("--time", default=None)
    parser.add_argument("--ntasks", type=int, default=None)
    parser.add_argument("--cpus-per-task", type=int, default=None)
    parser.add_argument("--mem", default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    render(
        args.template,
        args.output,
        {
            "job_name": args.job_name,
            "time": args.time,
            "ntasks": args.ntasks,
            "cpus_per_task": args.cpus_per_task,
            "mem": args.mem,
        },
    )
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()

