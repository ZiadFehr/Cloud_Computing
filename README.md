# Hospital Waiting Time Prediction API

This project deploys a machine learning regression model that predicts hospital patient waiting time (in minutes).  
The model is served via a REST API, containerized with Docker, and deployed to Kubernetes.

---

## Project Overview

- **Problem type**: Regression
- **Model**: XGBoost Regressor (trained with preprocessing pipeline)
- **API Framework**: FastAPI
- **Containerization**: Docker
- **Orchestration**: Kubernetes (Deployment + Service)
- **Autoscaling**: Horizontal Pod Autoscaler (CPU-based)

---

## Prerequisites

Ensure the following tools are installed:

- Python 3.10+
- Docker
- Kubernetes cluster (Minikube, Docker Desktop, or cloud-based)
- kubectl
- Docker Hub account (for image hosting)

---

## Local Setup (Without Kubernetes)

### 1. Build the Docker Image

```bash
docker build -t hospital-waiting-api .
```

### 2. Run the Container

```bash
docker run -p 8000:8000 hospital-waiting-api
```
