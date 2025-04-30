output "bucket_name" {
  value = aws_s3_bucket.input.bucket
}

output "dynamodb_table_name" {
  value = aws_dynamodb_table.results.name
}
