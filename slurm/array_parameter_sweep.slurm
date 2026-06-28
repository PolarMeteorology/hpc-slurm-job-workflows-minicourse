#!/bin/bash
#SBATCH --job-name=cpu-sweep
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --error=logs/%x-%A_%a.err
#SBATCH --time=00:10:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=512M
#SBATCH --array=0-9

set -euo pipefail
mkdir -p logs

seconds=$((SLURM_ARRAY_TASK_ID + 1))
python scripts/simulate_workload.py --mode cpu --seconds "${seconds}"

