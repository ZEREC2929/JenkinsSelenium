pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out project...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat '"C:\\Users\\arind\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t selenium-jenkins-test .'
            }
        }

        stage('Run Selenium Test') {
            steps {
                echo 'Running Selenium test inside Docker...'
                bat '"C:\\Users\\arind\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" run --rm selenium-jenkins-test'
            }
        }
    }

    post {
        always {
            echo 'CI/CD Pipeline execution completed.'
        }
    }
}