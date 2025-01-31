pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/Royce-LAYINDE/to-do_list_web_app.git'
    }

    stages {
        stage('Cloner le dépôt GitHub') {
            steps {
                echo 'Clonage du dépôt...'
                git branch: 'main', url: "${REPO_URL}"
            }
        }

        stage('Construire les conteneurs avec Docker') {
            steps {
                echo 'Construction des images Docker...'
                script{
                    docker.compose.build()
                }
            }
        }

        stage('Déployer l\'application avec Docker Compose') {
            steps {
                echo 'Démarrage des services...'
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        success {
            echo 'Déploiement réussi !'
        }
        failure {
            echo 'Échec du déploiement. Veuillez vérifier les logs Jenkins.'
        }
        always {
            echo 'Nettoyage des conteneurs...'
            sh 'docker-compose down || true'
        }
    }
}
