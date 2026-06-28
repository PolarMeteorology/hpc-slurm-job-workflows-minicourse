# Quiz and practical tasks

## Concept questions

1. What is the difference between a login node and a compute node?
2. Why should a batch script create its log directory before running work?
3. What is the difference between `--ntasks` and `--cpus-per-task`?
4. When is a job array a good workflow pattern?
5. What does a `TIMEOUT` state usually mean?
6. Why can over-requesting resources be harmful on a shared system?
7. Why is a manifest file useful for job arrays?
8. What evidence would you use before increasing a memory request?

## Multiple choice

### Question 1

Which command normally submits a SLURM batch job?

A. `squeue`  
B. `sbatch`  
C. `ssh`  
D. `scp`

Correct answer: **B**

### Question 2

Which directive requests a maximum wall time?

A. `#SBATCH --time=01:00:00`  
B. `#SBATCH --job-name=demo`  
C. `#SBATCH --output=logs/out.txt`  
D. `#SBATCH --array=0-9`

Correct answer: **A**

### Question 3

Which workflow is a good fit for a job array?

A. One MPI program where ranks communicate every second  
B. 200 independent files processed with the same command  
C. One interactive shell session  
D. One postprocessing step that must wait for all tasks

Correct answer: **B**

## Practical task

Create a batch script for a Python workload that:

- requests one task and two CPUs per task;
- requests 2 GB memory;
- writes output and error logs under `logs/`;
- runs `scripts/simulate_workload.py --mode cpu --seconds 10`;
- stops on the first command failure.

## Extension task

Design a two-stage workflow:

1. a job array that processes 12 independent parameter values;
2. a postprocessing job that starts only if the array completes successfully.

Include the `sbatch` commands or a short submission script.

## Capstone task

Design a manifest-driven workflow for six independent tasks and a dependent postprocessing job. Include:

- a manifest excerpt;
- the array script or relevant directives;
- the dependency submission command;
- a resource request justification;
- one debugging step you would take if one array task fails.
