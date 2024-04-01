# Olympic Data Pipeline
Quick Links: [Looker Studio Data Visualization](https://lookerstudio.google.com/reporting/ad0360d8-04d4-4dec-9184-897b87895043/page/LS0uD) | [Reproduction Guide](grading_and_reproduction/REPRODUCTION_GUIDE.md) | [Grading Guide](grading_and_reproduction/GRADING_GUIDE.md)

![Olympic Data Pipeline Flow](images/olympic_flow.gif)

Analyzing historical Olympic data (1896-2016) with a data pipeline
-
This document describes a data pipeline that leverages Terraform for infrastructure setup, Docker for containerized data processing with Mage and Apache Spark, Google BigQuery for data analysis and storage, and dbt (data build tool) for advanced data transformation and modeling. The pipeline integrates these technologies to streamline the process from data ingestion to visualization, ensuring a robust and scalable architecture for handling and analyzing large datasets.

## Problem Statement

Navigating the expansive historical datasets of Olympic events poses significant challenges in data management, accessibility, and analysis. This project aims to harness a dataset encompassing extensive Olympic history to streamline data processing, enhance data quality, and facilitate advanced analytical capabilities.

## Objective

The objective of this project is twofold:

- **Clean and Transform Data:** Utilize Apache Spark within a Docker container to perform data cleaning and transformation tasks, ensuring a clean and consistent dataset.
- **Enrich and Analyze Data:** Enhance the dataset with additional dimensions and metrics, employing dbt for data modeling and transformation, and ultimately visualizing the enriched data in a user-friendly Looker dashboard.

# Pipeline Structure

## Terraform (Setup Infrastructure)

- **Data Input:** Configuration files defining required cloud resources.
- **Action:** Provisions cloud infrastructure, including Google Cloud Storage (GCS) buckets for raw data storage and BigQuery datasets and tables for processed data storage, ensuring a ready environment for data processing and analysis.
- **Data Output to:** Infrastructure prepared for raw data storage in GCS, processing with Apache Spark within a Docker container, and analysis in BigQuery.

## Data Ingestion (Initial Data Loading into GCS)

- **Data Input:** Raw Olympic data collected from [here.](https://figshare.com/articles/dataset/Olympic_history_longitudinal_data_scraped_from_www_sports-reference_com/6121274) 
- **Action:** Utilizes a Docker container with Mage to automate the initial data ingestion process, directly loading raw data into Google Cloud Storage (GCS) without immediate processing. This step prepares the data for subsequent processing and ensures it is securely stored in a scalable cloud environment.
- **Data Output to:** Raw data securely stored in Google Cloud Storage, ready for detailed processing and transformation.

## Docker Container (Data Processing with Mage and Apache Spark)

- **Data Input:** Raw data from Google Cloud Storage (GCS), previously ingested from internet source.
- **Action:** Hosts a separate Docker container equipped with Mage and Apache Spark to perform comprehensive data processing. This phase includes cleaning the raw data, transforming it into a structured format, and performing necessary aggregations and data enrichment tasks to prepare it for analytical queries and visualization.
- **Data Output to:** Processed and structured data, optimized for analysis, is loaded into Google BigQuery for subsequent storage, further transformations, and analysis.

## Google BigQuery (Data Analysis and Storage)

- **Data Input:** Processed and transformed data from Apache Spark, orchestrated by Mage for direct loading.
- **Action:** Stores and enables complex querying of processed data. Optimizes query performance and cost by partitioning and clustering tables based on expected query patterns.
- **Data Output to:** Data structured and optimized for further transformations with dbt and analysis.

## dbt (Data Transformation within BigQuery)

- **Data Input:** Data loaded into BigQuery from previous steps.
- **Action:** Performs SQL-based transformations and modeling within BigQuery to refine data for analysis, utilizing partitioned and clustered tables for efficient data manipulation.
- **Data Output to:** Refined and modeled data within BigQuery, ready for visualization.

## Google Data Studio (Visualization) - [Click here.](https://lookerstudio.google.com/reporting/ad0360d8-04d4-4dec-9184-897b87895043/page/LS0uD) 

- **Data Input:** The transformed and modeled data within BigQuery.
- **Action:** Creates interactive dashboards and reports for data visualization and insights, benefiting from the optimized data structure.
- **Data Output:** Engaging visualizations that provide actionable insights to stakeholders.

---
## Data Engineering Zoomcamp

This project was developed as part of the [Data Engineering Zoomcamp](https://www.datatalks.club/courses/2024-data-engineering-zoomcamp.html) by DataTalks.Club, a comprehensive course designed to provide hands-on experience with the latest technologies in data engineering. Throughout the course, participants engage with topics ranging from containerization and infrastructure as code to workflow orchestration, data warehouses, analytics engineering, batch processing, and streaming.

### Acknowledgments

Special thanks to the instructors and organizers from DataTalks.Club, including Ankush Khanna, Victoria Perez Mola, Alexey Grigorev, Matt Palmer, Luis Oliveira, and Michael Shoemaker, for creating an engaging and educational experience.

I extend my gratitude to all the data scientists, developers, and researchers who have contributed to the Olympic data collection, as well as to the open-source tools and platforms that made this analysis possible. A special thank you to the volunteers and organizations maintaining the historical Olympic data sets and providing open access for educational and research purposes.

## Further Reading

For those interested in exploring more about Olympic history, data analysis techniques, or the technology stack used in this project, we recommend the following resources:

- [International Olympic Committee (IOC)](https://www.olympic.org/)
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [dbt Documentation](https://docs.getdbt.com/)
- [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Docker Get Started Guide](https://docs.docker.com/get-started/)

## License

This project is released under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


