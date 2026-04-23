# MLOps Learning Journey

This repository is my hands-on MLOps learning project.

Instead of creating a separate project for each tool, I am building one ML project step by step and improving it every week. The idea is to start simple and gradually make the workflow more reproducible, trackable, and production-aware.

## Project Goal

Build a simple machine learning project and keep layering MLOps tools on top of it:

- Week 1: DVC for data and pipeline reproducibility
- Week 2: MLflow for experiment tracking
- Week 3: Dagshub for collaboration and remote experiment visibility
- Next: deployment, CI/CD, and broader MLOps practices

## Current Project State

This repo currently includes:

- `train.py`: baseline sklearn training script using the built-in Iris dataset
- `train-dvc.py`: training script that uses the DVC-tracked dataset
- `data/data.csv.dvc`: DVC metadata for the dataset
- `dvc.yaml`: reproducible training pipeline definition
- `params.yaml`: configurable training parameters
- `metrics.json`: latest recorded training metric
- `model.pkl`: trained model artifact

## Learning Notes

- DVC guide: [README-DVC.md](C:/Users/donaa/Desktop/MLOps/Demo1/README-DVC.md)
- Weekly notes: [docs/week-01-dvc.md](C:/Users/donaa/Desktop/MLOps/Demo1/docs/week-01-dvc.md)
- Roadmap: [docs/roadmap.md](C:/Users/donaa/Desktop/MLOps/Demo1/docs/roadmap.md)

## Tech Stack

- Python
- scikit-learn
- joblib
- DVC
- MLflow

## Why This Repo Exists

This project is meant to document the learning process, not just the final output.

I want each stage to show:

- what problem a tool solves
- how it changes the project structure
- what commands and files are involved
- what I learned while implementing it

## Current Workflow

For the DVC stage, the project is currently designed to run with the `ml-env` WSL-based virtual environment.

The main DVC workflow is documented in [README-DVC.md](C:/Users/donaa/Desktop/MLOps/Demo1/README-DVC.md).
