import subprocess

@transformer
def run_pyspark_transformation(data, *args, **kwargs):
    # Construct the Docker run command with volume mounts as needed
    command = [
        "docker", "run", "--rm",
        "-v", "/local/path/to/data:/container/path/to/data",  # Adjust paths as needed
        "your-docker-image-name",  # Use the image name you provided when building the Docker image
        "python", "/path/in/container/transform_spark.py"  # Adjust to where your PySpark script is located within the container
    ]
    subprocess.run(command, check=True)
    # Handle the output from your PySpark job as needed

   