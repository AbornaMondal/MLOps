# Week 01: DVC

## What I Added

This week I added DVC to the project to learn how data versioning and pipeline reproducibility work in an ML workflow.

Changes made:

- tracked `data/data.csv` with DVC
- created `train-dvc.py` to train from the tracked CSV
- added `params.yaml` for training parameters
- added `dvc.yaml` for the training pipeline
- generated `metrics.json` for accuracy tracking
- configured a local DVC remote for storage

## How To Do It Step By Step

1. Initialize DVC in the repo
2. Add dataset with `dvc add data/data.csv`
3. Track the `.dvc` file in Git
4. Create `train-dvc.py`
5. Add `params.yaml`
6. Add `dvc.yaml`
7. Run `dvc repro`
8. Check metrics with `dvc metrics show`
9. Push artifacts with `dvc push`


## What I Learned

- Git should track code and DVC metadata, not large datasets directly
- `.dvc` files are pointers to tracked data
- `dvc.yaml` defines the ML pipeline steps
- `params.yaml` helps make experiments reproducible
- `dvc repro` reruns only when something important changes
- DVC can track metrics like model accuracy

## Commands I Used

From WSL:

```bash
cd /mnt/c/Users/donaa/Desktop/MLOps/Demo1
./ml-env/bin/dvc version
./ml-env/bin/dvc status
./ml-env/bin/dvc repro
./ml-env/bin/dvc metrics show
./ml-env/bin/dvc push
```

## Files Added For DVC

- `data/data.csv.dvc`
- `train-dvc.py`
- `dvc.yaml`
- `params.yaml`
- `metrics.json`
- `.dvc/config.local`


## Concept Notes

### What is DVC?
DVC is a tool for versioning datasets, models, and ML pipelines.

### Why not use Git alone?
Git is good for code, but not large datasets and model artifacts.

### What is `dvc.yaml`?
It defines the ML pipeline stages, dependencies, outputs, and params.

## Main Takeaway

DVC helped me move from "just running a training script" to "building a reproducible ML workflow with tracked data, parameters, and outputs."
