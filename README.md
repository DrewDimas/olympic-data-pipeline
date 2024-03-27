# olympic-data-pipeline
Analyzing historical Olympic data (1896-2016) with a data pipeline

___

Current Plan:

Olympic Data (1896-2016)
      ↓
Google Cloud Storage (Raw Data Storage)
      ↓
  Terraform (Setup Infrastructure)
      ↓
 Docker Container (Apache Spark for Data Processing)
      ↓
Mage (Workflow Orchestration)
      ↓
Google Cloud Storage (Processed Data)
      ↓
   Google BigQuery (Data Loading)
      ↓
          dbt (Data Transformation within BigQuery)
      ↓
      Google Data Studio (Visualization)


## Data Pipeline Overview

This pipeline is designed for processing, analyzing, and visualizing Olympic data spanning from 1896 to 2016. Below is an overview of the steps involved in the pipeline:

1. **Google Cloud Storage (Raw Data Storage)**
   - The initial repository for raw Olympic dataset, leveraging Google Cloud Storage for its scalability and global accessibility.

2. **Terraform (Setup Infrastructure)**
   - Utilizes Terraform to provision and manage the necessary cloud infrastructure, ensuring efficient, reproducible setup of resources like BigQuery datasets and Apache Spark compute resources.

3. **Docker Container (Apache Spark for Data Processing)**
   - Employs Docker containers to run Apache Spark jobs for data processing and transformation, ensuring consistent environments across different stages of the pipeline.

4. **Mage (Workflow Orchestration)**
   - Orchestrates the pipeline workflow with Mage, automating the execution of data processing tasks, and managing the direct loading of data into BigQuery for analysis.

5. **Google BigQuery (Data Analysis and Storage)**
   - Acts as the analytical engine and storage solution, with processed data loaded directly into BigQuery for scalable querying and in-depth analysis.

6. **dbt (Data Transformation within BigQuery)**
   - Leverages dbt for further data transformations and modeling within BigQuery, refining the data for analysis and ensuring its quality.

7. **Google Data Studio (Visualization)**
   - Utilizes Google Data Studio for data visualization and reporting, creating interactive dashboards and reports based on the analysis performed in BigQuery.

### Key Considerations

- This pipeline optimizes for efficiency by eliminating intermediate storage of processed data in Google Cloud Storage, instead opting for a direct load into BigQuery.
- It aims to reduce complexity and potential costs by streamlining data handling steps.
- The configuration is focused on robust error handling and efficient re-processing capabilities by making the most of BigQuery's analytical features.
