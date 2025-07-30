pipeline {
    agent any

    stages {
        stage('Run in Python Docker') {
            steps {
                script {
                    docker.image('python:3.10').inside {
                        sh 'pip install pytest'
                        sh 'pytest test_app.py'
                    }
                }
            }
        }
    }
}
