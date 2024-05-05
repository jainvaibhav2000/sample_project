pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/jainvaibhav2000/sample_project.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/jainvaibhav2000/sample_project.git'
                sh 'python main.py'
            }
        }
        stage('Test') {
            steps {
                
                sh 'pytest test.py'
            }
        }
    }
}
