terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region                   = var.aws_region
  shared_config_files      = [var.config_location]
  shared_credentials_files = [var.creds_location]
  profile                  = var.profile
}

output "http_api_logs_command" {
  description = "Command to view http api logs with sam"
  value       = "sam logs --cw-log-group ${aws_cloudwatch_log_group.logs.name} -t"
}

output "thumbnailizer_logs_command" {
  description = "Command to view responder function logs with sam"
  value       = "sam logs --cw-log-group ${module.lambda_function_thumbnailizer.lambda_cloudwatch_log_group_name} -t"
}

output "all_logs" {
  description = "Command to view an aggragate of all logs with sam"
  value       = "sam logs --cw-log-group ${aws_cloudwatch_log_group.logs.name} --cw-log-group ${module.lambda_function_thumbnailizer.lambda_cloudwatch_log_group_name} -t"
}

