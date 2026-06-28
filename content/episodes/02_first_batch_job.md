# Episode 2 - Your first batch job

A batch job is a script with scheduler directives and shell commands. The directives request resources; the commands perform the work.

```{admonition} Objectives
:class: tip

After this episode, learners will be able to read a basic SLURM script, adapt job name and resources, submit with `sbatch`, and inspect logs.
```

## A minimal Python job

```bash
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

python scripts/simulate_workload.py --mode cpu --seconds 5
```

The full example is in `slurm/basic_python_job.slurm`.

## Submit and inspect

```bash
sbatch slurm/basic_python_job.slurm
squeue --me
```

After completion:

```bash
ls logs
sacct -j JOBID --format=JobID,JobName,State,Elapsed,MaxRSS,AllocCPUS
```

```{admonition} Exercise: change one thing at a time
:class: important

Render a copy of the basic job with a new job name, then change the requested wall time and memory. Explain which changes affect queue placement and which changes affect only log readability.
```

## Local rendering helper

```bash
python scripts/render_job.py \
  --template slurm/basic_python_job.slurm \
  --output rendered_basic_job.slurm \
  --job-name test-run \
  --time 00:03:00 \
  --mem 1G
```

## Key points

- Keep resource requests visible and deliberate.
- Write logs to predictable paths.
- Start with small jobs before scaling up.

