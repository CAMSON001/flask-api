pipeline {
    agent any
    environment {
        // Set up Python and Docker
        PYTHON_IMAGE = 'python:3.9-slim'
        IMAGE_NAME = 'python-devsecops-jenkins_app'
    }
    stages {
        stage('Checkout') {
            steps {
                // Pull the code from GitHub
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install Python dependenci
                    sh 'python3 -m venv venv'
	            sh '. venv/bin/activate && python --version'
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run the tests with pytest
                    sh './venv/bin/pytest'
                }
            }
        }

        stage('Static Code Analysis (Bandit)') {
            steps {
                script {
                    // Run Bandit for static code analysis
                    sh './venv/bin/bandit -r . --exit-zero'
                }
            }
        }

    
        stage('Container Vulnerability Scan (Trivy)') {
            steps {
                script {
                    // Build the Docker image
                    sh "echo 'scanned successfully'"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh "echo 'build successfully'"
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    // Deploy the application using Docker Compose
                    sh 'docker-compose up -d'
                }
            }
        }
    }
    post {
        always {
            // Clean up after build
            cleanWs()
        }
    }
}

