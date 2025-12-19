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
### 3. Verify Health Endpoint

```bash
curl http://localhost:8000/healthz
```
### 4. Test Prediction Endpoint

```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json"
 -d '{
    "doctor_type": "General",
    "financial_class": "Insurance",
    "patient_type": "New",
    "medication_revenue": 50,
    "lab_cost": 30,
    "consultation_revenue": 100,
    "entry_hour": 10,
    "entry_dayofweek": 2,
    "entry_minute": 15,
    "year": 2024,
    "month": 5,
    "dayofweek": 2
  }'
```

### 5. Push Image to Docker

```bash
docker tag hospital-waiting-api ziadfehr/hospital-waiting-api:latest
docker push ziadfehr/hospital-waiting-api:latest
```

### Push Image to DockerHub

```bash
docker tag hospital-waiting-api ziadfehr/hospital-waiting-api:latest
docker push ziadfehr/hospital-waiting-api:latest
```

## Kubernetes Deployment

### 1. Create Deployment

```bash
kubectl create deployment hospital-waiting --image=<dockerhub-username>/hospital-waiting-api:latest
```

### 2. Expose Service

```bash
kubectl expose deployment hospital-waiting --type=NodePort --port=8000
```

### 3. Apply Health Probes

```bash
kubectl patch deployment hospital-waiting --type='json' -p='[
     {
       "op": "add",
       "path": "/spec/template/spec/containers/0/livenessProbe",
       "value": {
         "httpGet": {
           "path": "/healthz",
           "port": 8000
         },
         "initialDelaySeconds": 10,
         "periodSeconds": 10
       }
     }
   ]'

kubectl patch deployment hospital-waiting --type='json' -p='[
     {
       "op": "add",
       "path": "/spec/template/spec/containers/0/readinessProbe",
       "value": {
         "httpGet": {
           "path": "/healthz",
           "port": 8000
         },
         "initialDelaySeconds": 5, 
         "periodSeconds": 5 
       }
     }
   ]'
```

### 4. Export Kubernetes YAML Files

```bash
kubectl get deployment hospital-waiting -o yaml > deployment.yaml
kubectl get service hospital-waiting -o yaml > service.yaml
```

## AutoScaling

```bash
kubectl autoscale deployment hospital-waiting --cpu=50% --min=1 --max=5
kubectl get hpa
```
