# Reproduction Guide

## Prerequisites
Ensure you have GCloud, Terraform, Mage, Docker, and dbt CLI installed on your machine. This guide assumes the repository is run on VSCode via GitHub Codespaces.

### Terraform
1. Navigate to the Terraform folder within the project directory.
2. Place your Google Cloud Platform credentials file (`my-creds.json`) in the `keys/` folder.
3. Initialize Terraform and apply configurations to provision cloud resources:
    ```bash
    terraform init
    terraform apply
    ```

### Docker Container (Mage and Apache Spark for Data Processing)
1. Navigate to the Mage/olympic-pipeline folder.
2. Ensure your GCP credentials file (`my-creds.json`) is placed in the `keys/` folder.
3. Build the Mage Docker image that includes the Apache Spark environment:
    ```bash
    docker build -t mage_spark .
    ```
4. Start the Mage container with the necessary environment variables:
    ```bash
    docker run -it --name mage_spark -e SPARK_MASTER_HOST='local' -p 6789:6789 -v $(pwd):/home/src mage_spark /app/run_app.sh mage start
    ```
5. Run the pipeline named `raw_data_ingestion` to import data from internet sources, transform it to Parquet format, and upload it to Google Cloud Storage.
6. Execute the pipeline named `gcs_clean_to_bigquery` to import Parquet data from GCS, perform basic cleaning and transformation on the dataset, split it into two tables (male & female), and upload to BigQuery.

### Dbt
1. Change your working directory to the dbt project folder.
2. Update the `profiles.yml` file with your BigQuery credentials.
3. Run dbt commands to install dependencies, run transformations, and test:
    ```bash
    dbt deps
    dbt run
    dbt test
    ```

### Looker
1. Open Looker Studio and create a new report or dashboard.
2. Connect to the BigQuery dataset created by the dbt jobs as the data source.
3. Design your report or dashboard by selecting from the created BigQuery tables and utilizing the available fields for visualization.

By following these steps, you should be able to replicate the data pipeline and generate visualizations based on the transformed and modeled data.
