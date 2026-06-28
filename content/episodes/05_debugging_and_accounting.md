# Episode 5 - Debugging and accounting

HPC jobs fail for ordinary reasons: missing files, wrong paths, missing modules, insufficient time, insufficient memory, or writing logs to a missing directory. The key skill is to diagnose from evidence.

```{admonition} Objectives
:class: tip

After this episode, learners will be able to inspect logs, interpret common SLURM states, and summarise sample accounting data.
```

## Common states

| State | Meaning | First place to look |
|---|---|---|
| `COMPLETED` | job finished successfully | output log |
| `FAILED` | command exited with non-zero status | error log |
| `TIMEOUT` | wall time limit reached | elapsed time and script progress |
| `OUT_OF_MEMORY` | memory limit exceeded | MaxRSS and memory request |
| `CANCELLED` | job was cancelled by user or policy | scheduler message |

## Debugging checklist

- Does the log directory exist?
- Did the script run from the expected working directory?
- Was the right Python/module/container loaded?
- Did the input file exist on the compute node?
- Did the job request enough time and memory?
- Did the script stop at the first error?

## Accounting exercise

```bash
python scripts/summarize_sacct.py data/sample_sacct.csv
```

```{admonition} Exercise: diagnose three jobs
:class: important

Use the sample accounting file to identify one completed job, one failed job, and one timed-out job. For each, write the next debugging action you would take.
```

## Key points

- Good logs are part of the workflow, not an afterthought.
- Accounting data helps improve future resource requests.
- Debugging starts with the scheduler state, then moves to logs and application output.

