pipeline {
    agent any  

    stages {
        stage('Checkout') {
            steps {
                echo 'Clonage du dépôt GitHub...'
                git 'https://github.com/Royce-LAYINDE/to-do_list_web_app.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Création et activation de l’environnement virtuel...'
                    // Détection du système d'exploitation
                    if (isUnix()) {
                        sh '''
                            python3 -m venv venv
                            . venv/bin/activate
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            python -m venv venv
                            .\\venv\\Scripts\\activate
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    echo 'Exécution des tests...'
                    if (isUnix()) {
                        sh '''
                            . venv/bin/activate
                            pytest tests/
                        '''
                    } else
