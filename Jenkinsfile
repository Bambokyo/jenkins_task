pipeline {
    agent { label 'your_agent_label' } // Specify an agent label or name here

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
                script {
                    bat 'pip install pytest' // Use 'sh' on Unix-based agents
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    bat 'python test_case.py' // Use 'sh' on Unix-based agents
                }
            }
        }
    }
}
