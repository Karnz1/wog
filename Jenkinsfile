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
                sh 'python e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                sh 'docker rm -f scores-scores-1'
                sh 'git push'
            }
        }
    }
}