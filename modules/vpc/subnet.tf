resource "aws_subnet" "public" {
  depends_on = [
    aws_vpc.ownvpc
  ]
  vpc_id     = aws_vpc.ownvpc.id
  cidr_block = var.sub_cidr
  availability_zone = var.az

  tags = {
    Name = var.sub_name
  }
}