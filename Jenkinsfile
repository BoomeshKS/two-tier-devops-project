pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/BoomeshKS/two-tier-devops-project.git'
            }
        }

        stage('Build and Run Docker Compose') {
            steps {
                bat 'docker compose down || exit 0'
                bat 'docker compose up --build -d'
            }
        }
    }
}
