pipeline {
    agent any  
    
    environment {
        PYTHON_ENV = 'python3'
        DEPENDENCIES = 'requirements.txt'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Cloner le dépôt Git
                git 'https://github.com/Royce-LAYINDE/to-do_list_web_app.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    // Create a virtual environment
                    bat 'python -m venv venv'
                    // Activate the virtual environment (Windows syntax)
                    bat '.\\venv\\Scripts\\activate'
                    // Install dependencies
                    bat 'pip install -r requirements.txt'
                }
            }
        }    
        
        stage('Run Tests') {
            steps {
                // Exécuter les tests avec pytest
                bat '''
                    . venv/bin/activate
                    pytest tests/  //  le chemin des tests 
                '''
            }
        }

       
    }
    
    post {
        success {
            echo 'Build et tests réussis!'
        }
        failure {
            echo 'Le build a échoué.'
        }
    }
}
