# DVC Setup Guide

This file documents the DVC-based workflow for this project without changing the original `README.md`.

## Files Used By DVC

- `data/data.csv.dvc`: tracks the dataset with DVC
- `train-dvc.py`: trains the model from the DVC-tracked CSV
- `dvc.yaml`: defines the reproducible training pipeline
- `params.yaml`: stores training parameters
- `metrics.json`: stores the latest training metric
- `model.pkl`: saved trained model

## Important Environment Note

This project uses `ml-env`, which is a WSL/Linux virtual environment.

That means DVC commands should be run from WSL using the Python and DVC executables inside:

```bash
./ml-env/bin/python
./ml-env/bin/dvc
```

## Local DVC Remote

The repo is configured with a local DVC remote in:

```text
.dvc/localremote
```

This remote is set in [`.dvc/config.local`](C:/Users/donaa/Desktop/MLOps/Demo1/.dvc/config.local) and is intended for local storage on this machine.

## Open The Project In WSL

```bash
cd /mnt/c/Users/donaa/Desktop/MLOps/Demo1
```

## Main DVC Commands

Check DVC version:

```bash
./ml-env/bin/dvc version
```

Check pipeline status:

```bash
./ml-env/bin/dvc status
```

Reproduce the pipeline:

```bash
./ml-env/bin/dvc repro
```

Show metrics:

```bash
./ml-env/bin/dvc metrics show
```

Push tracked data and outputs to the local remote:

```bash
./ml-env/bin/dvc push
```

Pull tracked data and outputs from the local remote:

```bash
./ml-env/bin/dvc pull
```

## Pipeline Definition

The training stage is:

```yaml
stages:
  train:
    cmd: ./ml-env/bin/python train-dvc.py
```

It depends on:

- `train-dvc.py`
- `data/data.csv`
- `params.yaml`

It produces:

- `model.pkl`
- `metrics.json`

## Training Parameters

The pipeline reads values from `params.yaml`:

```yaml
train:
  test_size: 0.2
  random_state: 42
  n_estimators: 100
```

If you change any of these values, run:

```bash
./ml-env/bin/dvc repro
```

## Manual Script Options

This repo now contains two training scripts:

- `train.py`: original simple training script using sklearn's built-in Iris dataset
- `train-dvc.py`: DVC-based training script using `data/data.csv`

## Typical Workflow

1. Open the repo in WSL.
2. Make changes to `data/data.csv`, `train-dvc.py`, or `params.yaml`.
3. Run `./ml-env/bin/dvc repro`.
4. Check results with `./ml-env/bin/dvc metrics show`.
5. Run `./ml-env/bin/dvc push` to store outputs in the local remote.

## Current Verified Commands

These were verified successfully in WSL:

```bash
./ml-env/bin/dvc version
./ml-env/bin/dvc remote list
./ml-env/bin/python train-dvc.py
./ml-env/bin/dvc repro -v
```
