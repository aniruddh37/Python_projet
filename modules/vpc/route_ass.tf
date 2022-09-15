resource "aws_route_table_association" "rta_subnet_public" {
  depends_on = [
    aws_route_table.my_table
  ]
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.my_table.id
}