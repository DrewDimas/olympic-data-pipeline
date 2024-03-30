## Course Project Data Pipeline 

**Batch Pipeline Selected**

## Evaluation Criteria

* Problem description
### Comment: Problem description described in README in main directory. 
    * 0 points: Problem is not described
    * 2 points: Problem is described but shortly or not clearly 
    * 4 points: Problem is well described and it's clear what the problem the project solves
* Cloud
**Comment**: Terraform used to create GCP and BigQuery infastructure. Dbt cloud also utilized. 
    * 0 points: Cloud is not used, things run only locally
    * 2 points: The project is developed in the cloud
    * 4 points: The project is developed in the cloud and IaC tools are used
* Batch / Workflow orchestration
**Comment**: Utilized Mage orchestration for weekly upload of primary data.
    * 0 points: No workflow orchestration
    * 2 points: Partial workflow orchestration: some steps are orchestrated, some run manually
    * 4 points: End-to-end pipeline: multiple steps in the DAG, uploading data to data lake
* Data warehouse
**Comment**: Tables partioned to male/female athletes, as well as 
    * 0 points: No DWH is used
    * 2 points: Tables are created in DWH, but not optimized
    * 4 points: Tables are partitioned and clustered in a way that makes sense for the upstream queries (with explanation)
* Transformations (dbt, spark, etc)
**Comment**: First transformation with Spark within Docker/Mage container. Secondary transformations made in Dbt cloud.
    * 0 points: No tranformations
    * 2 points: Simple SQL transformation (no dbt or similar tools)
    * 4 points: Tranformations are defined with dbt, Spark or similar technologies
* Dashboard
**Comment**: Multiple tiles in dashboard located here: 
    * 0 points: No dashboard
    * 2 points: A dashboard with 1 tile
    * 4 points: A dashboard with 2 tiles
* Reproducibility
**Comment**: Reproduction.md located in grading_and_reproduction folder. Code comments throughtout project.
    * 0 points: No instructions how to run the code at all
    * 2 points: Some instructions are there, but they are not complete
    * 4 points: Instructions are clear, it's easy to run the code, and the code works
