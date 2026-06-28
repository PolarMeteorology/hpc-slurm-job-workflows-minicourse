# Episode 7 - Capstone mini-project

The capstone asks learners to combine the lesson patterns into one small but realistic workflow: plan resources, run independent tasks, postprocess results, and justify improvements.

```{admonition} Objectives
:class: tip

After this episode, learners will be able to design a small end-to-end SLURM workflow and explain the reasoning behind resource requests, arrays, dependencies, logs, and accounting.
```

## Project scenario

You have six independent workloads described in a manifest file. Some are CPU-oriented, some allocate memory, and some create small files. Your task is to design a workflow that:

1. runs each workload as an array task;
2. writes separate logs for each task;
3. starts a postprocessing step only after the array succeeds;
4. checks accounting output;
5. proposes improved resource requests for the next run.

## Suggested workflow

Generate or inspect a manifest:

```bash
python scripts/make_array_manifest.py --output data/generated_manifest.csv --count 6 --mode cpu
```

Run the array:

```bash
sbatch slurm/manifest_array.slurm
```

Submit a dependency chain:

```bash
bash slurm/submit_dependency_chain.sh
```

Analyse sample accounting:

```bash
python scripts/summarize_sacct.py data/sample_sacct.csv
python scripts/plan_resources.py data/resource_observations.csv
```

## Deliverables

Learners submit:

- one annotated batch script;
- one manifest file or manifest excerpt;
- one paragraph explaining resource requests;
- one paragraph explaining logs and failure handling;
- one recommended improvement after accounting review.

## Assessment rubric

| Criterion | Excellent | Partial | Needs work |
|---|---|---|---|
| Workflow structure | Array and dependency are used appropriately | Only one pattern used | Workflow ordering unclear |
| Resource reasoning | Requests are justified from evidence | Requests are plausible but not justified | Requests are arbitrary |
| Logging | Output and error logs are predictable | Logs exist but naming is weak | Logs missing |
| Portability | Site-specific settings are isolated | Some assumptions documented | Assumptions hidden |
| Debugging | Failure paths are discussed | One failure mode discussed | No debugging plan |

## Key points

- A useful HPC workflow is more than a working command.
- Reviewable inputs, predictable logs, and resource evidence make jobs easier to teach, maintain, and scale.
