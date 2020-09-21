pipeline {
    agent { docker { image 'python:3.7.7' } }
    stages {
        stage('Downloading requirements') {
            steps {
                echo 'Installing requirements...'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Linting') {
            steps {
                echo 'Linting...'
                sh 'flake8'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
    }
    post {
        always {
            echo 'BUILD WAS COMPLETED'
        }
        success {
            echo 'BUILD SUCCEEDED FOR THE PROJECT come-and-unity-backend'
        }
        failure {
            echo 'BUILD FAILED FOR THE PROJECT come-and-unity-backend'
        }
    }
}