pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Karnz1/wog.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Run') {
            steps {
                echo 'Deploying....'
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