#!/bin/bash
#SBATCH --job-name=manifest-array
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --error=logs/%x-%A_%a.err
#SBATCH --time=00:10:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --array=0-5

set -euo pipefail
mkdir -p logs

# Adapt this section to local cluster policy.
# module load python
# source .venv/bin/activate

manifest="data/parameter_manifest.csv"
row=$(awk -F, -v task_id="${SLURM_ARRAY_TASK_ID}" 'NR > 1 && $1 == task_id {print}' "${manifest}")

if [[ -z "${row}" ]]; then
  echo "No manifest row for task ${SLURM_ARRAY_TASK_ID}" >&2
  exit 1
fi

IFS=, read -r task_id mode seconds megabytes files label <<< "${row}"
echo "Running task=${task_id} label=${label} mode=${mode}"

if [[ "${mode}" == "cpu" ]]; then
  python scripts/simulate_workload.py --mode cpu --seconds "${seconds}"
elif [[ "${mode}" == "memory" ]]; then
  python scripts/simulate_workload.py --mode memory --megabytes "${megabytes}"
else
  python scripts/simulate_workload.py --mode io --files "${files}" --directory "scratch/${label}"
fi
