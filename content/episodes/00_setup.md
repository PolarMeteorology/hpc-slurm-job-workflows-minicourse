# Episode 0 - Software setup

This episode prepares the local environment used for the helper scripts and explains what changes on a real SLURM cluster.

```{admonition} Objectives
:class: tip

After this episode, learners will be able to create a local Python environment, run the helper scripts, inspect the SLURM examples, and identify which cluster-specific settings must be adapted.
```

## Local installation

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

## Run local helper scripts

```bash
python scripts/simulate_workload.py --mode cpu --seconds 2
python scripts/simulate_workload.py --mode memory --megabytes 64
python scripts/summarize_sacct.py data/sample_sacct.csv
```

These commands do not require a cluster. They support teaching and testing before learners submit jobs.

## Cluster prerequisites

On a real cluster, learners need:

- an account on the system;
- a project or allocation if required;
- access to a partition or queue;
- a software environment policy, such as modules, conda, or containers;
- a shared working directory where jobs can write logs and outputs.

```{admonition} Exercise: identify local policy
:class: important

Find the commands used on your cluster to list partitions, inspect account information, load Python, and check job accounting. If you do not have cluster access, write placeholders for the commands you would ask support staff about.
```

## Key points

- The same job script pattern must be adapted to local cluster policy.
- Helper scripts make the examples testable even without scheduler access.
- Cluster-ready training material should separate portable logic from site-specific configuration.

