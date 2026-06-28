from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.render_job import render
from scripts.summarize_sacct import load_rows, parse_memory_to_mb, summarize
from scripts.make_array_manifest import build_rows, write_manifest
from scripts.plan_resources import load_completed_rows, recommend, seconds_to_slurm_time
from scripts.check_slurm_script import check_script


def test_parse_memory_to_mb():
    assert parse_memory_to_mb("1024K") == 1
    assert parse_memory_to_mb("512M") == 512
    assert parse_memory_to_mb("2G") == 2048
    assert parse_memory_to_mb("Unknown") is None


def test_summarize_sample_sacct():
    rows = load_rows(ROOT / "data" / "sample_sacct.csv")
    summary = summarize(rows)

    assert summary["jobs"] == 6
    assert summary["states"]["COMPLETED"] == 3
    assert summary["states"]["TIMEOUT"] == 1
    assert summary["max_memory_mb"] == 2048
    assert summary["total_alloc_cpus"] == 6


def test_render_job_updates_directives():
    output = ROOT / "rendered_unit_test.slurm"
    try:
        text = render(
            ROOT / "slurm" / "basic_python_job.slurm",
            output,
            {
                "job_name": "unit-test",
                "time": "00:02:00",
                "ntasks": 2,
                "cpus_per_task": 4,
                "mem": "2G",
            },
        )

        assert "#SBATCH --job-name=unit-test" in text
        assert "#SBATCH --time=00:02:00" in text
        assert "#SBATCH --ntasks=2" in text
        assert "#SBATCH --cpus-per-task=4" in text
        assert "#SBATCH --mem=2G" in text
        assert output.exists()
    finally:
        output.unlink(missing_ok=True)


def test_make_array_manifest_writes_expected_rows():
    output = ROOT / "data" / "generated_unit_test_manifest.csv"
    try:
        rows = build_rows(3, "cpu", 2)
        write_manifest(output, rows)
        text = output.read_text(encoding="utf-8")

        assert "task_id,mode,seconds,megabytes,files,label" in text
        assert "0,cpu,2,64,5,cpu-000" in text
        assert "2,cpu,4,192,15,cpu-002" in text
    finally:
        output.unlink(missing_ok=True)


def test_resource_recommendation_from_observations():
    rows = load_completed_rows(ROOT / "data" / "resource_observations.csv")
    result = recommend(rows)

    assert result["evidence_jobs"] == 5
    assert result["time"] == "00:01:00"
    assert result["memory"] == "768M"
    assert result["cpus_per_task"] == 1
    assert seconds_to_slurm_time(3661) == "01:01:01"


def test_slurm_checker_accepts_training_scripts():
    assert check_script(ROOT / "slurm" / "basic_python_job.slurm") == []
    assert check_script(ROOT / "slurm" / "manifest_array.slurm") == []
