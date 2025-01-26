pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Création et activation de l’environnement virtuel...'
                    bat 'C:\\chemin\\vers\\python.exe -m venv venv'
                    bat '.\\venv\\Scripts\\activate && pip install -r requirements.txt'
                }
            }
        }
    }
}
