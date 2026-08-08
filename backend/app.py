from fastapi import FastAPI
from fastapi.responses import FileResponse
import json
import os

from agents.security_agent import check_security
from agents.drift_agent import detect_drift

app = FastAPI()

# Project folders
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")


# Load cloud JSON data
def load_cloud(file_name):
    file_path = os.path.join(DATA_DIR, file_name)

    with open(file_path, "r") as file:
        return json.load(file)


# Cloud Guardian Dashboard
@app.get("/")
def home():
    return FileResponse(
        os.path.join(FRONTEND_DIR, "index.html")
    )


# Get all clouds
@app.get("/clouds")
def get_clouds():
    return {
        "clouds": [
            load_cloud("aws.json"),
            load_cloud("azure.json"),
            load_cloud("gcp.json")
        ]
    }


# Security Agent
@app.get("/security")
def security():
    clouds = [
        load_cloud("aws.json"),
        load_cloud("azure.json"),
        load_cloud("gcp.json")
    ]

    result = []

    for cloud in clouds:
        result.append(check_security(cloud))

    return result


# Drift Agent
@app.get("/drift")
def drift():
    clouds = [
        load_cloud("aws.json"),
        load_cloud("azure.json"),
        load_cloud("gcp.json")
    ]

    baseline_path = os.path.join(DATA_DIR, "baseline.json")

    with open(baseline_path, "r") as file:
        baseline = json.load(file)

    result = []

    for cloud in clouds:
        expected = baseline[cloud["cloud"]]

        result.append(
            detect_drift(cloud, expected)
        )

    return result