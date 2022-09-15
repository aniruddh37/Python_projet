resource "aws_vpc" "ownvpc" {
  cidr_block       = var.cidr
  instance_tenancy = "default"

  tags = {
    Name = var.vpc_name
  }
}