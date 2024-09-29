provider "aws" {
  region     = "us-east-1"
  access_key = "AKIASCKIJMVV2QGI4YRM"
  secret_key = "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"
}

resource "aws_instance" "foo" {
  ami           = var.ami # us-west-2
  instance_type = var.instance_type
}

##variables

variable "ami" {
  description = "this is the ami of the ec2 machine"
  type = string
  default = "ami-0f9fc25dd2506cf6d"
  
}

variable "instance_type" {
  type = string
  default = "t2.micro"
  
}