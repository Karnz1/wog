pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Karnz1/wog.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t scores:latest .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage('Test') {
            steps {
                echo 'Deploying....'
            }
        }
        stage('Finalize') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}