resource "aws_route_table" "my_table" {
  depends_on = [
    aws_internet_gateway.hadoop_gateway
  ]
  vpc_id = aws_vpc.ownvpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.hadoop_gateway.id
  }

  tags = {
    Name = var.rt_name
  }
}