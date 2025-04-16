resource "local_file" "fooo" {
  content  = "foo!"
  filename = "${path.module}/foo.bar"
}