pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest test_app.py'
            }
        }
    }
}
