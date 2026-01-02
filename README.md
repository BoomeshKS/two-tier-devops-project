# Two-Tier Flask Application with CI/CD

This project demonstrates a two-tier web application consisting of:
- A Flask backend service
- A MySQL database

The application is containerized using Docker and deployed automatically using Jenkins.

---

## Architecture Overview

- Flask application runs in one container
- MySQL database runs in a separate container
- Docker Compose manages service communication
- Jenkins automates build and deployment

---

## Project Structure

two-tier-project/
├── app/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
├── db/
│ └── init.sql
├── docker-compose.yml
├── Jenkinsfile
└── README.md

---

## How the Application Works

1. Flask starts and waits for incoming requests
2. MySQL starts and initializes the database
3. Flask connects to MySQL using environment variables
4. Flask executes a SQL query
5. MySQL returns the result
6. Flask returns the response to the browser

---

## How to Run Locally

```bash
docker-compose up --build

Access the app at:

http://localhost:5000