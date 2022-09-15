resource "aws_internet_gateway" "hadoop_gateway" {
  depends_on = [
    aws_subnet.public
  ]
  vpc_id = aws_vpc.ownvpc.id

  tags = {
    Name = var.gw_name
  }
}