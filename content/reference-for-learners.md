# Reference for learners

## Useful SLURM commands

```bash
sbatch job.slurm
squeue --me
scancel JOBID
sacct -j JOBID --format=JobID,JobName,State,Elapsed,MaxRSS,AllocCPUS
scontrol show job JOBID
```

## Common directives

```bash
#SBATCH --job-name=my-job
#SBATCH --output=logs/%x-%j.out
#SBATCH --error=logs/%x-%j.err
#SBATCH --time=00:30:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=4G
#SBATCH --array=0-9
```

## Key terms

**Batch job**  
A non-interactive job submitted to the scheduler.

**Job array**  
A set of similar jobs managed under one array identifier.

**Partition**  
A scheduler queue or resource class.

**Wall time**  
Maximum elapsed runtime requested for a job.

**MaxRSS**  
Maximum resident memory reported for a job or job step.

**Dependency**  
A rule that delays a job until another job reaches a specified state.

## Local helper commands

```bash
python scripts/simulate_workload.py --mode cpu --seconds 2
python scripts/render_job.py --template slurm/basic_python_job.slurm --output rendered_basic_job.slurm
python scripts/summarize_sacct.py data/sample_sacct.csv
python scripts/check_slurm_script.py slurm/basic_python_job.slurm
python scripts/make_array_manifest.py --output data/generated_manifest.csv --count 6 --mode cpu
python scripts/plan_resources.py data/resource_observations.csv
pytest
```
