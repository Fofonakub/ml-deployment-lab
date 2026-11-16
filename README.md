# ML Deployment Lab

Machine Learning Model as a Service
using Flask and Docker.

## Project Structure

- app.py
- train_model.py
- requirements.txt
- Dockerfile
- templates/main.html
- model/

## Build Docker Image

docker build -t ds-ml-service .

## Run Docker Container

docker run --rm -p 5000:5000 ds-ml-service

## Access Web Application

http://127.0.0.1:5000/

## Health Check

http://127.0.0.1:5000/health

## API Endpoint

POST /predict