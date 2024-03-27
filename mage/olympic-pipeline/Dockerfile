FROM mageai/mageai:latest
ARG PIP=pip3

# Add Debian Bullseye repository
RUN echo 'deb http://deb.debian.org/debian bullseye main' > /etc/apt/sources.list.d/bullseye.list

# Install OpenJDK 11
RUN apt-get update -y && \
    apt-get install -y openjdk-11-jdk

# Remove Debian Bullseye repository
RUN rm /etc/apt/sources.list.d/bullseye.list

# Install PySpark
RUN ${PIP} install pyspark


# Set the environment variable for Google Cloud authentication
ENV GOOGLE_APPLICATION_CREDENTIALS=keys/my-creds.json

# Set the MAGE_DATA_DIR environment variable to the copied pipeline directory inside the container
ENV MAGE_DATA_DIR='/mage/olympic-pipeline'

CMD ["/app/run_app.sh", "mage", "start"]
