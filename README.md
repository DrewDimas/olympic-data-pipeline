# Olympic Data Pipeline Overview

Analyzing historical Olympic data (1896-2016) with a data pipeline

This document describes a data pipeline that leverages Terraform for infrastructure setup, Docker for containerized data processing with Mage and Apache Spark, Google BigQuery for data analysis and storage, and dbt (data build tool) for advanced data transformation and modeling. The pipeline integrates these technologies to streamline the process from data ingestion to visualization, ensuring a robust and scalable architecture for handling and analyzing large datasets.

## Terraform (Setup Infrastructure)

- **Data Input:** Configuration files defining required cloud resources.
- **Action:** Provisions cloud infrastructure, including Google Cloud Storage (GCS) buckets for raw data storage and BigQuery datasets and tables for processed data storage, ensuring a ready environment for data processing and analysis.
- **Data Output to:** Infrastructure prepared for raw data storage in GCS, processing with Apache Spark within a Docker container, and analysis in BigQuery.

## Docker Container (Mage and Apache Spark for Data Processing)

- **Data Input:** Raw data from various internet sources and configurations for orchestrating the data pipeline workflow.
- **Action:** Hosts both Mage and Apache Spark to automate data ingestion from internet sources directly into GCS and perform data processing tasks such as cleaning, transformations, and aggregations.
- **Data Output to:** Processed data ready for loading into BigQuery for subsequent storage and analysis.

## Google BigQuery (Data Analysis and Storage)

- **Data Input:** Processed and transformed data from Apache Spark, orchestrated by Mage for direct loading.
- **Action:** Stores and enables complex querying of processed data. Optimizes query performance and cost by partitioning and clustering tables based on expected query patterns.
- **Data Output to:** Data structured and optimized for further transformations with dbt and analysis.

## dbt (Data Transformation within BigQuery)

- **Data Input:** Data loaded into BigQuery from previous steps.
- **Action:** Performs SQL-based transformations and modeling within BigQuery to refine data for analysis, utilizing partitioned and clustered tables for efficient data manipulation.
- **Data Output to:** Refined and modeled data within BigQuery, ready for visualization.

## Google Data Studio (Visualization)

- **Data Input:** The transformed and modeled data within BigQuery.
- **Action:** Creates interactive dashboards and reports for data visualization and insights, benefiting from the optimized data structure.
- **Data Output:** Engaging visualizations that provide actionable insights to stakeholders.

This pipeline facilitates a streamlined workflow from data ingestion to visualization, leveraging the integration of Mage and Apache Spark within a Docker container to simplify the processing steps and enhance the efficiency of the overall pipeline.
