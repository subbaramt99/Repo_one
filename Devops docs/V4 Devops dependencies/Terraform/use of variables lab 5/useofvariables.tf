provider "aws" {
  region = "us-east-1"  #region where i want to perform all the actions
}

data "aws_subnet" "selected" {
  filter {
    name   = "tag:Name"
    values = [var.subnet_name]
  }
}

resource "aws_instance" "new" {
  ami           = "ami-0c02fb55956c7d316" #you can take ami id from the aws management console
  subnet_id = data.aws_subnet.selected.id  
  instance_type = "t2.micro"
  
}

###variables#####
variable "subnet_name" {
  description = "this is the subnet which need to be created"
  type = string
  default = "akshat"
  
}
