#!/bin/bash
#SBATCH --job-name=postprocess
#SBATCH --output=logs/%x-%j.out
#SBATCH --error=logs/%x-%j.err
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=512M

set -euo pipefail
mkdir -p logs

python scripts/summarize_sacct.py data/sample_sacct.csv

