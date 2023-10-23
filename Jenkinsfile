pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: 'main']],
                    userRemoteConfigs: [
                        [
                            url: 'https://github.com/Bambokyo/jenkins_task.git'
                        ]
                    ]
                ])
            }
        }

               stage('Install Dependencies') {
            steps {
                // Install Python and required dependencies
                bat 'pip install pytest'  // If you have a requirements file
            }
        }

        stage('Run Tests') {
            steps {
                // Run your test cases using pytest
                bat 'python3 test_cases.py'
            }
        }
    }
}
