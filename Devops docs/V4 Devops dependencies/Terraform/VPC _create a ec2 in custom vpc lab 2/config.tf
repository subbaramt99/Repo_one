provider "aws" {
  region = "us-east-1"
}
resource "aws_vpc" "akshat" {
  cidr_block = "10.0.0.0/16"
}

###Subnet#######

resource "aws_subnet" "akshatsubnet" {
  vpc_id     = aws_vpc.akshat.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "akshat"
  }
}

############Internet gateway#########
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.akshat.id
  

  tags = {
    Name = "akshat"
  }
}


#############Route table##############

resource "aws_route_table" "akshatroutetable" {
  vpc_id = aws_vpc.akshat.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }


  tags = {
    Name = "example"
  }
}

###Subnet association#####
resource "aws_route_table_association" "akshatroutetable" {
  subnet_id      = aws_subnet.akshatsubnet.id
  route_table_id = aws_route_table.akshatroutetable.id
}

###creating Ec2 in that akshat vpc ####






resource "aws_instance" "akshatinstance" {
  ami           = "ami-0c02fb55956c7d316" 
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.akshatsubnet.id

 
  }

 