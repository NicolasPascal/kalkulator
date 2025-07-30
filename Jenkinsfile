pipeline {
    agent any
    stages {
        stage('Run in Python Docker') {
            steps {
                script {
                    sh 'docker pull python:3.10'
                    sh 'docker run --rm -v $(pwd):/app -w /app python:3.10 sh -c "pip install pytest && pytest test_app.py"'
                }
            }
        }
    }
}
