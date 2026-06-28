# Instructor guide

## Recommended duration

This lesson can be delivered as:

- **2 hours**: scheduler concepts, first job, and quiz;
- **4 hours**: practical session with arrays, dependencies, and accounting;
- **6 hours**: full workshop including templates, portability checks, resource planning, and capstone;
- **self-paced**: learners complete episodes and helper-script exercises independently.

## Suggested learner profile

- First-time HPC users.
- MSc or PhD students moving from local scripts to cluster execution.
- Researchers who need reliable batch workflows.
- Technical staff preparing an introductory scheduler workshop.

## Suggested flow

| Section | Time |
|---|---:|
| Setup and local helper scripts | 20 min |
| Scheduler concepts | 35 min |
| First batch job | 40 min |
| Resources and efficiency | 40 min |
| Arrays and dependencies | 40 min |
| Debugging and accounting | 30 min |
| Workflow templates and portability | 35 min |
| Capstone mini-project | 45 min |
| Quiz and discussion | 20 min |

## Common learner difficulties

- Confusing tasks and CPU cores.
- Forgetting that the job starts in a batch environment, not an interactive shell.
- Requesting too much memory or wall time without evidence.
- Not checking logs after failure.
- Treating job arrays as a replacement for workflow design.

## Teaching recommendations

- Use a real cluster if available, but keep local helper scripts as a fallback.
- Ask learners to predict resource use before running examples.
- Show both successful and failing jobs.
- Use the SVG diagrams as anchor slides before live terminal work.
- Ask learners to run the script checker before submitting their final job script.
- Emphasize log paths, working directories, and environment activation.
- Keep site-specific account and partition settings in one visible block.

## Assessment guidance

For a practical assessment, ask learners to submit:

- a batch script;
- a short explanation of resource choices;
- output or accounting evidence from one run;
- one improvement they would make after inspecting the result.

For a longer workshop, use the capstone mini-project as the final assessment.
