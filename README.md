# Two-Tier Flask Application with CI/CD

This project demonstrates a **two-tier web application** built using **Flask** and **MySQL**, fully containerized with **Docker**, orchestrated using **Docker Compose**, and deployed automatically using **Jenkins CI/CD**.

---

## Project Overview

The application consists of:
- A **Flask backend service** (Application Tier)
- A **MySQL database** (Database Tier)

The goal of this project is to show how a simple backend system can be:
- Containerized
- Automated
- Deployed consistently using CI/CD practices

---

## Architecture Diagram

### High-Level Architecture

```

+-------------+
|   Browser   |
+------+------+
|
v
+------+-------------------+
|   Flask Application      |
|   (Docker Container)     |
+------+-------------------+
|
v
+------+-------------------+
|   MySQL Database         |
|   (Docker Container)     |
+--------------------------+

```

---

## CI/CD Flow Diagram

```

Developer
|
v
GitHub Repository
|
v
Jenkins Pipeline
|
v
Docker Build
|
v
Docker Compose
|
v
Flask App  <---->  MySQL DB

```

---

## Project Structure

```

two-tier-project/
│
├── app/
│   ├── app.py              # Flask application logic
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Flask Docker image
│
├── db/
│   └── init.sql            # Database initialization script
│
├── docker-compose.yml      # Multi-container orchestration
├── Jenkinsfile             # CI/CD pipeline definition
└── README.md               # Project documentation

````

---

## How the Application Works

1. The **Flask container** starts and listens on port `5000`
2. The **MySQL container** initializes the database using `init.sql`
3. Flask reads database credentials using **environment variables**
4. Flask connects to MySQL through Docker’s internal network
5. A SQL query is executed
6. The response is returned to the browser

---

## Docker & Docker Compose

### Why Docker?
- Ensures consistent behavior across environments
- Removes dependency installation issues
- Isolates application and database

### Why Docker Compose?
- Runs multiple containers together
- Automatically creates a shared network
- Simplifies service communication using service names

---

## 🚀 How to Run the Project Locally

From the project root:

```bash
docker-compose up --build
````

Access the application in your browser:

```
http://localhost:5000
```

To stop the application:

```bash
docker-compose down
```

---

## Jenkins CI/CD Pipeline

The Jenkins pipeline performs the following steps:

1. Clones the repository from GitHub
2. Builds Docker images
3. Runs containers using Docker Compose
4. Deploys the application automatically

This removes manual deployment steps and ensures consistency.

---

## Key Concepts Demonstrated

* Two-tier application architecture
* Containerization with Docker
* Multi-container orchestration
* Environment-based configuration
* CI/CD automation with Jenkins
* Basic debugging and logging


