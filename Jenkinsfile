pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/Royce-LAYINDE/to-do_list_web_app.git'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main', url: "${REPO_URL}"
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                # Install virtualenv if not already installed
                python3 -m pip install --user virtualenv
                
                # Create a virtual environment
                python3 -m virtualenv venv
                
                # Activate the virtual environment and install dependencies (if requirements.txt exists)
                if [ -f requirements.txt ]; then
                    source venv/bin/activate && pip install -r requirements.txt
                fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '''
                # Activate the virtual environment and run the specified test file
                source venv/bin/activate && python -m unittest tests/test_sample.py
                '''
            }
        }

        stage('Archive Test Results') {
            steps {
                echo 'Archiving test results...'
                junit testResults: '**/tests/results/*.xml', allowEmptyResults: true
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
        always {
            echo 'Cleaning up workspace...'
            cleanWs() // Cleans the workspace after the pipeline finishes
        }
    }
}
