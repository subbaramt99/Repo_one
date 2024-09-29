
provider "aws" {
  region     = "us-west-2"
  access_key = "AKIASCKIJMVV6ZLF2U42"
  secret_key = "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"
}

resource "aws_s3_bucket" "bakshatbucket12" {
  bucket = "my-tf-test-bucket98998"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket_acl" "example" {
  bucket = aws_s3_bucket.bakshatbucket12.id
  acl    = "private"
}