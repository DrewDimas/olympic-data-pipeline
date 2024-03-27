terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
}

resource "google_storage_bucket" "olympic_raw_data_bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true
}

resource "google_bigquery_dataset" "olympic_data_dataset" {
  dataset_id                  = var.bq_dataset_name
  location                    = var.location
  default_table_expiration_ms = 3600000 # Optional: Sets default table expiration to 1 hour. Adjust as needed.
}
