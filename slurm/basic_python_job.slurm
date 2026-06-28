#!/bin/bash
#SBATCH --job-name=hello-slurm
#SBATCH --output=logs/%x-%j.out
#SBATCH --error=logs/%x-%j.err
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=512M

set -euo pipefail
mkdir -p logs

# Adapt this section to local cluster policy.
# module load python
# source .venv/bin/activate

python scripts/simulate_workload.py --mode cpu --seconds 5

