module "lambda_function_thumbnailizer" {
  source              = "terraform-aws-modules/lambda/aws"
  version             = "~> 6.0"
  timeout             = 300
  source_path         = "../src/thumbnailizer"
  function_name       = "thumbnailizer"
  handler             = "thumbnailizer.lambda_handler"
  runtime             = "python3.11"
  create_sam_metadata = true
  publish             = true
  tags                = var.resource_tags
  allowed_triggers = {
    APIGatewayAny = {
      service    = "apigateway"
      source_arn = "${aws_apigatewayv2_api.api.execution_arn}/*/*"
    }
  }
}