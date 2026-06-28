# HPC SLURM Job Workflows Minicourse

**Reusable training material for writing, submitting, monitoring, and improving SLURM jobs on shared HPC systems.**

This repository contains a hands-on training lesson for learners who are beginning to run computational work on clusters. It focuses on practical job workflow skills: resource requests, batch scripts, job arrays, dependencies, logging, failure diagnosis, and simple accounting analysis.

The material is designed as a 4-6 hour workshop or a self-paced lesson. It includes short concept episodes, annotated SLURM scripts, diagrams, small Python exercises that can run without a cluster, sample accounting data, practical tasks, and regression tests for the helper scripts.

## Why this module is useful

Many learners can run code locally but struggle when the same work moves to a shared scheduler. Common issues include requesting the wrong resources, losing logs, running heavy work on login nodes, submitting thousands of tiny jobs, or failing to interpret queue and accounting output. This lesson turns those everyday HPC problems into a structured learning path.

## Training scope

The material demonstrates capacity to develop:

- self-contained modular HPC training lessons;
- annotated job scripts for common scheduler patterns;
- local simulations for learners without immediate cluster access;
- practical exercises with clear assessment criteria;
- reusable scripts for rendering job files and parsing accounting output;
- manifest-driven job-array examples;
- resource recommendation from observed job data;
- visual explanations of job lifecycle and workflow patterns;
- quality checks that make the training repository reviewable.

## Learning outcomes

After completing this lesson, learners will be able to:

1. Explain the difference between login nodes, compute nodes, jobs, tasks, CPUs, memory, and wall time.
2. Write a basic SLURM batch script with clear resource requests and logs.
3. Choose reasonable resource requests for small CPU, memory, and file I/O workloads.
4. Use job arrays for parameter sweeps and independent tasks.
5. Chain jobs with dependencies for simple multi-step workflows.
6. Diagnose common job failures from logs and accounting fields.
7. Summarise job efficiency from sample `sacct` output.
8. Convert a one-off job script into a reusable workflow template.
9. Use a manifest file to make job-array inputs reviewable.
10. Recommend revised resource requests from completed job evidence.

## Course structure

```text
content/
|-- conf.py
|-- index.md
|-- episodes/
|   |-- 00_setup.md
|   |-- 01_scheduler_concepts.md
|   |-- 02_first_batch_job.md
|   |-- 03_resources_and_efficiency.md
|   |-- 04_job_arrays_and_dependencies.md
|   |-- 05_debugging_and_accounting.md
|   |-- 06_workflow_templates_and_portability.md
|   `-- 07_capstone_mini_project.md
|-- figures/
|   |-- job-lifecycle.svg
|   |-- resource-feedback-loop.svg
|   `-- array-dependency-workflow.svg
|-- quiz/
|   `-- quiz.md
|-- instructor-guide.md
`-- reference-for-learners.md
```

Supporting files:

```text
scripts/       helper scripts for simulation, linting, manifests, and resource planning
slurm/         annotated SLURM job examples
data/          sample accounting, manifest, and resource-observation data
tests/         regression tests for helper scripts
```

## Quick start

Create a local environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Run the helper scripts locally:

```bash
python scripts/simulate_workload.py --mode cpu --seconds 2
python scripts/render_job.py --template slurm/basic_python_job.slurm --output rendered_basic_job.slurm --job-name demo
python scripts/summarize_sacct.py data/sample_sacct.csv
python scripts/check_slurm_script.py slurm/basic_python_job.slurm
python scripts/make_array_manifest.py --output data/generated_manifest.csv --count 4 --mode cpu
python scripts/plan_resources.py data/resource_observations.csv
```

Run tests:

```bash
pytest
```

Build the lesson site, if Sphinx dependencies are installed:

```bash
sphinx-build -b html content content/_build/html
```

## Notes for cluster use

The SLURM scripts are examples. Learners should adapt account names, partitions, module commands, conda activation, time limits, and storage paths to the policy of their own cluster.

## Licenses

- Text and pedagogical material: **CC BY-SA 4.0**.
- Source code and scripts: **MIT License**.

See `LICENSE` and `LICENSE.code`.
