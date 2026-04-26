📘 Week 02: DagsHub Integration
## What I Added

This week I integrated DagsHub with my DVC project to enable remote storage and collaboration.

## Changes made:

- connected DVC to DagsHub remote
- configured authentication using access token
- pushed tracked dataset to remote storage
- verified data sync between local and remote
- linked Git repo with DagsHub

## How To Do It Step By Step
1. Create a repository in DagsHub
2. Add DagsHub as DVC remote
   dvc remote add origin https://dagshub.com/<username>/<repo>.dvc
3. Configure authentication
    dvc remote modify origin --local auth basic
    dvc remote modify origin --local user <username>
    dvc remote modify origin --local password <access-token>
4. Push data to remote
    dvc push
5. Push code to Git
    git push origin main

## What I Learned
- DVC can use remote storage like DagsHub instead of local storage
- Remote storage enables team collaboration in ML projects
- Access tokens are safer than passwords for authentication
- dvc push uploads data, while Git handles code
- Separation of code + data improves scalability

## Commands I Used

From WSL:

cd /mnt/c/Users/donaa/Desktop/MLOps/Demo1
./ml-env/bin/dvc remote add origin https://dagshub.com/<username>/<repo>.dvc
./ml-env/bin/dvc remote modify origin --local auth basic
./ml-env/bin/dvc remote modify origin --local user <username>
./ml-env/bin/dvc remote modify origin --local password <token>
./ml-env/bin/dvc push
git push origin main

## Files Added For DagsHub
.dvc/config (updated with remote)
.dvc/config.local (credentials stored locally)

## Concept Notes
1. What is DagsHub?

DagsHub is a platform that combines Git, DVC, and ML experiment tracking in one place.

2. Why use DagsHub with DVC?

It provides:

- remote storage for datasets
- collaboration across teams
- versioning of ML data and models
3. What is DVC Remote?

A storage location (local or cloud) where DVC keeps tracked data.

4. Storage Options in DagsHub

DagsHub supports two ways to store data with DVC:

1. HTTPS Remote (Default & Simple)
- Uses DagsHub’s built-in storage
- Easy to set up
- Works with username + access token
- Best for beginners and small projects

Example:
dvc remote add origin https://dagshub.com/<username>/<repo>.dvc

2. S3-Compatible Storage (Advanced)
Uses external storage like:
- Amazon S3
- MinIO or other S3-compatible services
- More scalable and flexible
- Requires access key + secret key
- Suitable for large datasets and production setups

Example:

dvc remote add origin s3://my-bucket/path
## When to Use What?
Use HTTPS → for learning, small projects, quick setup
Use S3 → for production, large-scale ML pipelines, team environments

## Main Takeaway
Integrating DagsHub with DVC and understanding storage options (HTTPS vs S3) helped me move from local-only ML workflows to a more scalable and collaborative MLOps setup.