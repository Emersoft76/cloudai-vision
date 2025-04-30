variable "region" {
  description = "AWS region"
  type        = string
  default     = "eu-west-1"
}

variable "bucket_name" {
  description = "S3 Bucket name for uploads"
  type        = string
}

variable "dynamodb_table" {
  description = "DynamoDB table for storing image analysis"
  type        = string
}
