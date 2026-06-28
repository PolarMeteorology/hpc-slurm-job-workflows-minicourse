# HPC SLURM Job Workflows Minicourse

This lesson teaches practical job workflow skills for shared HPC systems using SLURM. Learners move from basic scheduler concepts to batch scripts, resource requests, job arrays, dependencies, logging, accounting analysis, workflow templates, and a capstone mini-project.

The training examples are intentionally small. Helper scripts can run on a laptop, while the annotated SLURM files show how the same ideas transfer to a real cluster.

## Target learners

- students and researchers who are beginning to use HPC clusters;
- technical users who know the command line but are new to batch scheduling;
- scientific programmers who want more reliable job submission workflows;
- instructors who need compact examples for scheduler training.

Prerequisites:

- basic shell usage;
- ability to run a Python script;
- no prior SLURM experience is required.

## Learning outcomes

By the end of the lesson, learners will be able to:

- explain the role of the scheduler on a shared cluster;
- distinguish jobs, tasks, CPUs, memory, wall time, partitions, and logs;
- write and adapt a basic SLURM batch script;
- use job arrays for independent parameter sweeps;
- use job dependencies for staged workflows;
- diagnose common job failures from logs and accounting fields;
- summarise job efficiency from sample accounting data;
- use manifest files to make job-array inputs reviewable;
- revise resource requests from observed job evidence.

## Software Setup

```{toctree}
:maxdepth: 1

episodes/00_setup
```

## Episodes

```{toctree}
:maxdepth: 1

episodes/01_scheduler_concepts
episodes/02_first_batch_job
episodes/03_resources_and_efficiency
episodes/04_job_arrays_and_dependencies
episodes/05_debugging_and_accounting
episodes/06_workflow_templates_and_portability
episodes/07_capstone_mini_project
```

## Assessment

```{toctree}
:maxdepth: 1

quiz/quiz
```

## Reference

```{toctree}
:maxdepth: 1

instructor-guide
reference-for-learners
```

## Credit and license

Authors: Polar Meteorology / Polar Meteorological Consultancy and Engineering Inc.

Pedagogical text and lesson material are licensed under **CC BY-SA 4.0**. Source code and scripts are licensed under the **MIT License**.
