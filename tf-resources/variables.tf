variable "aws_region" {
  description = "AWS region"
  type        = string
}

variable "profile" {
  description = "AWS profile"
  type        = string
  default     = "default"
}

variable "config_location" {
  description = "AWS configuration file"
  type        = string
  default     = "~/.aws/config"
}

variable "creds_location" {
  description = "AWS credentials file"
  type        = string
  default     = "~/.aws/credentials"
}

variable "resource_tags" {
  type = object({
    name        = string
    owner       = string
    environment = string
  })
  default = {
    name        = "thumbnailizer"
    owner       = "ahsan"
    environment = "dev"
  }

}

