pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t employee-app:latest .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker stop leaveapp || true
                docker rm leaveapp || true

                docker run -d \
                --name leaveapp \
                -p 5000:5000 \
                employee-app:latest
                '''
            }
        }
    }
}
