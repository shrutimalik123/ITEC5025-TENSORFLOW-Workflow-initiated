# Dockerized TensorFlow Environment

This project sets up a Docker container with Python 3.11 and TensorFlow, suitable for development without conflicting with your local Python setup.

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

## Usage

### Start the Environment
To start the container:
```bash
docker-compose up -d --build
```

### Stop the Environment
To stop the container:
```bash
docker-compose down
```

### Run Scripts
To run a Python script inside the container:
```bash
docker-compose exec tensorflow-dev python <script_name.py>
```
Example (Verification):
```bash
docker-compose exec tensorflow-dev python test_tf.py
```

### Interactive Shell
To get a bash shell inside the container:
```bash
docker-compose exec tensorflow-dev bash
```

## Files

-   `Dockerfile`: Defines the Python 3.11 image with TensorFlow installed.
-   `docker-compose.yml`: Orchestrates the container and mounts your current directory to `/app`.
-   `requirements.txt`: Lists dependencies (tensorflow, numpy, pandas).
-   `test_tf.py`: A simple script to verify TensorFlow installation.
