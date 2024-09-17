terraform {
  required_providers {
    env = {
      source  = "sethvargo/env"
      version = "0.1.0"
    }
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.15.0"
    }
  }
}

provider "env" {
  # Path to the .env file
  path = "${path.module}/.env"
}

provider "docker" {
  host = "npipe:////./pipe/docker_engine"
}

resource "docker_image" "streamlit_app" {
  name         = "streamlit-app"
  build {
    context    = "${path.module}"
    dockerfile = "${path.module}/Dockerfile"
  }
}

resource "docker_container" "streamlit_app" {
  image = docker_image.streamlit_app.latest
  name  = "streamlit-app"
  ports {
    internal = 8501
    external = 8501
  }

  env {
    EMAIL_ADDRESS = env.EMAIL_ADDRESS
    EMAIL_PASSWORD = env.EMAIL_PASSWORD
  }
}
