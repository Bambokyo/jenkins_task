pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Check out your source code from GitHub repository and branch
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: 'main']], // Specify your branch name here
                    userRemoteConfigs: [
                        [
                            url: 'https://github.com/Bambokyo/jenkins_task.git' // Specify your GitHub repository URL here
                        ]
                    ]
                ])
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    bat 'pip install pytest'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    bat 'python3 test_case.py'
                }
            }
        }
    }
}
