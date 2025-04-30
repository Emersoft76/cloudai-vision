```hd
provider "aws" {
  region = var.region
}

resource "aws_s3_bucket" "input" {
  bucket = var.bucket_name

  tags = {
    Name        = "CloudAI Vision Input Bucket"
    Environment = "dev"
  }
}

resource "aws_dynamodb_table" "results" {
  name           = var.dynamodb_table
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "imageKey"

  attribute {
    name = "imageKey"
    type = "S"
  }

  tags = {
    Name = "CloudAI Results Table"
  }
}
```
