#!/bin/bash
set -euo pipefail

first_job=$(sbatch --parsable slurm/array_parameter_sweep.slurm)
second_job=$(sbatch --parsable --dependency=afterok:${first_job} slurm/dependent_postprocess.slurm)

echo "Submitted array job ${first_job}"
echo "Submitted dependent postprocess job ${second_job}"

