pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Création et activation de l’environnement virtuel...'
                    // Détection du système d'exploitation
                    if (isUnix()) {
                        sh '''
                            /usr/bin/python3 -m venv venv
                            . venv/bin/activate
                            /usr/bin/pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            C:\\chemin\\vers\\python.exe -m venv venv
                            .\\venv\\Scripts\\activate
                            .\\venv\\Scripts\\pip install -r requirements.txt
                        '''
                    }
                }
            }
        }
    }
}
