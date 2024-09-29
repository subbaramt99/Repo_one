provider "aws" {
  region = "us-east-1"
}

data "aws_subnet" "selected" {
  filter {
    name   = "tag:Name"
    values = ["akshat"]
  }
}

resource "aws_instance" "new" {
  ami           = "ami-0c02fb55956c7d316" # us-west-2
  subnet_id = data.aws_subnet.selected.id
  instance_type = "t2.micro"
  
}