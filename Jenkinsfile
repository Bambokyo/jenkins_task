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
                    // Use a virtual environment (Python venv) for isolation
                    bat 'pip install pytest'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Activate the virtual environment and run pytest
                    bat 'python3 test_case.py'
                }
            }
        }
    }
}
