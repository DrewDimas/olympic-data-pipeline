variable "credentials" {
  description = "Path to the Google Cloud service account key JSON file."
}

variable "project" {
  description = "The Google Cloud project ID."
  default     = "datacamp2024-412820"
}

variable "region" {
  description = "The Google Cloud region for resources."
  default     = "us-central1"
}

variable "location" {
  description = "The location for the Google Cloud Storage bucket and BigQuery dataset."
  default     = "US"
}

variable "bq_dataset_name" {
  description = "The name for the BigQuery dataset storing Olympic data."
  default     = "olympic_data"
}

variable "gcs_bucket_name" {
  description = "The name for the Google Cloud Storage bucket storing raw Olympic data."
  default     = "olympic-raw-data-bucket"
}

variable "gcs_storage_class" {
  description = "The storage class for the Google Cloud Storage bucket."
  default     = "STANDARD"
}
