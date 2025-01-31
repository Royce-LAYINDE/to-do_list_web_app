pipeline {
    agent any

    environment {
        // Définir les variables d'environnement si nécessaire
        DOCKER_IMAGE_NAME = 'to-dovision-app'
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Cloner le dépôt GitHub') {
            steps {
                // Cloner le code depuis GitHub
                git 'https://github.com/Royce-LAYINDE/to-do_list_web_app.git'
            }
        }

        stage('Construire les conteneurs avec Docker') {
            steps {
                script {
                    // Construire l'image Docker à partir du Dockerfile
                    bat 'docker build -t %DOCKER_IMAGE_NAME% .'
                }
            }
        }

        stage('Déployer l\'application avec Docker Compose') {
            steps {
                script {
                    // Lancer Docker Compose pour déployer l'application localement
                    bat 'docker-compose -f %DOCKER_COMPOSE_FILE% up -d'
                }
            }
        }
    }

    post {
        always {
            // Nettoyer ou arrêter les conteneurs après le déploiement
            bat 'docker-compose -f %DOCKER_COMPOSE_FILE% down'
        }
    }
}
