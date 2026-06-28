#!/bin/bash
#SBATCH --job-name=threaded-python
#SBATCH --output=logs/%x-%j.out
#SBATCH --error=logs/%x-%j.err
#SBATCH --time=00:10:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=1G

set -euo pipefail
mkdir -p logs

# Adapt this section to local cluster policy.
# module load python
# source .venv/bin/activate

export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK}"
export OPENBLAS_NUM_THREADS="${SLURM_CPUS_PER_TASK}"
export MKL_NUM_THREADS="${SLURM_CPUS_PER_TASK}"

python scripts/simulate_workload.py --mode cpu --seconds 10
