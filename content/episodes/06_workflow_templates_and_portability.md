# Episode 6 - Workflow templates and portability

Once learners can write a single batch script, the next step is to make job workflows reusable. A portable workflow separates site-specific settings from scientific commands and records the inputs used for each task.

```{admonition} Objectives
:class: tip

After this episode, learners will be able to use a manifest file for job arrays, render job scripts from templates, and check scripts for common portability issues.
```

## Why templates help

A one-off job script is useful for learning. A template is useful for repeated work because it makes the changeable parts visible:

- job name;
- wall time;
- memory;
- CPU count;
- input manifest;
- output directory;
- environment setup.

## Manifest-driven arrays

The file `data/parameter_manifest.csv` contains one row per array task:

```text
task_id,mode,seconds,megabytes,files,label
0,cpu,1,64,5,cpu-short
```

The script `slurm/manifest_array.slurm` reads the row matching `SLURM_ARRAY_TASK_ID` and chooses the right helper workload.

```bash
sbatch slurm/manifest_array.slurm
```

You can generate a new manifest locally:

```bash
python scripts/make_array_manifest.py --output data/generated_manifest.csv --count 8 --mode cpu
```

## Script checks

The repository includes a simple teaching-oriented checker:

```bash
python scripts/check_slurm_script.py slurm/basic_python_job.slurm
python scripts/check_slurm_script.py slurm/manifest_array.slurm
```

It checks for common quality markers such as job name, logs, time, CPU and memory requests, strict shell mode, and log-directory creation.

```{admonition} Exercise: improve a template
:class: important

Copy `slurm/basic_python_job.slurm`, change the resource requests for a memory-heavy workload, and run the checker. Then explain which parts are site-specific and which parts are portable.
```

## Key points

- Templates reduce repeated editing and accidental drift.
- Manifests make job-array inputs reviewable.
- Portability improves when environment setup and resource choices are explicit.
