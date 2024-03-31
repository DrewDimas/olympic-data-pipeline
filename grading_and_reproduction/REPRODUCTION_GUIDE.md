Prereqs: GCloud, Terraform, Mage, & Docker installed.
Repo ran on VSCode via Github Codespaces.


Segment 1: Terraform
    - Open Terraform folder
    - Add your Google API key named 'my-creds.json' into keys/ folder
    - Run command 
    '

Segment 2: Docker / Mage / Spark

    # Open mage folder

    # Add your Google API key named 'my-creds.json' into keys/ folder

    # Build Mage docker image with Spark environment
    docker build -t mage_spark .

    # Start Mage with SPARK_MASTER_HOST environment variable
    docker run -it --name mage_spark -e SPARK_MASTER_HOST='local' -p 6789:6789 -v $(pwd):/home/src mage_spark \ /app/run_app.sh mage start

    #Run pipeline named raw_data_ingestion (This will import data from internet, transform to parquet, and upload to Google Cloud Storage.

    # Run pipeline named gcs_clean_to_bigquery (This will import parquet from GCS, perform basic clean/transformation on dataset, split into two tables (male & female), and upload to bigquery.
    
Segment 3: Dbt

    # Set dbt folder as home project directoy
    
