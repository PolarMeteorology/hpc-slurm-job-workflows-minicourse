"""Run small local workloads used by the SLURM lesson examples."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import time


def cpu_work(seconds: float) -> str:
    deadline = time.monotonic() + seconds
    digest = b"training"
    iterations = 0
    while time.monotonic() < deadline:
        digest = hashlib.sha256(digest).digest()
        iterations += 1
    result = digest.hex()[:16]
    print(f"CPU workload finished: iterations={iterations} digest={result}")
    return result


def memory_work(megabytes: int) -> int:
    if megabytes < 1:
        raise ValueError("megabytes must be at least 1")
    block = bytearray(megabytes * 1024 * 1024)
    for index in range(0, len(block), 4096):
        block[index] = index % 251
    checksum = sum(block[::4096])
    print(f"Memory workload finished: megabytes={megabytes} checksum={checksum}")
    return checksum


def io_work(directory: Path, files: int) -> int:
    if files < 1:
        raise ValueError("files must be at least 1")
    directory.mkdir(parents=True, exist_ok=True)
    total_bytes = 0
    for index in range(files):
        path = directory / f"chunk-{index:04d}.txt"
        text = f"sample file {index}\n" * 100
        path.write_text(text, encoding="utf-8")
        total_bytes += path.stat().st_size
    print(f"I/O workload finished: files={files} bytes={total_bytes} directory={directory}")
    return total_bytes


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("cpu", "memory", "io"), required=True)
    parser.add_argument("--seconds", type=float, default=2.0, help="duration for CPU mode")
    parser.add_argument("--megabytes", type=int, default=64, help="allocation size for memory mode")
    parser.add_argument("--files", type=int, default=10, help="number of files for I/O mode")
    parser.add_argument("--directory", type=Path, default=Path("scratch/io-demo"), help="directory for I/O mode")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.mode == "cpu":
        cpu_work(args.seconds)
    elif args.mode == "memory":
        memory_work(args.megabytes)
    else:
        io_work(args.directory, args.files)


if __name__ == "__main__":
    main()

