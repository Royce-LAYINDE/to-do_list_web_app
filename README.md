# To-DoVision – Application Web de Gestion de Tâches

**To-DoVision** est une application web interne développée pour les employés de l’entreprise **AI-Vision**. Elle permet une gestion simple, efficace et sécurisée des tâches, sans recourir à des outils tiers susceptibles de compromettre la confidentialité des données.

## Objectifs

- Développer un outil interne de gestion des tâches adapté aux besoins métier.
- Automatiser le processus de déploiement grâce à un pipeline CI/CD.
- Déployer l’application dans un environnement scalable via Kubernetes.

## Fonctionnalités

- Ajout de tâches
- Validation et invalidation de tâches
- Suppression de tâches
- Compteur de tâches effectuées et totales
- Interface simple et fluide (HTML, CSS, Bootstrap)

## Technologies utilisées

| Composant           | Technologies mises en œuvre            |
|---------------------|----------------------------------------|
| Backend             | Flask (Python 3.9)                     |
| Base de données     | SQLite                                 |
| Frontend            | HTML, CSS, Bootstrap                   |
| Conteneurisation    | Docker, Docker Compose                 |
| Intégration continue| Jenkins + Jenkinsfile                  |
| Orchestration       | Kubernetes (Minikube)                  |
| Hébergement image   | Docker Hub (`roy61/to-do_list_web_app-web`) |

## Architecture

### Backend

- `/` : affichage des tâches
- `/add` : ajout d'une tâche (POST)
- `/delete/<id>` : suppression
- `/complete/<id>` : marquage comme terminée
- `/incomplete/<id>` : retour à l’état initial

### Frontend

- Interface statique HTML/CSS
- Utilisation de Bootstrap pour la mise en page

### Conteneurisation

- Dockerfile basé sur `python:3.9-slim`
- Installation des dépendances via `requirements.txt`
- Exposition du port 5000

### Déploiement avec Docker Compose

- Lancement multi-conteneurs
- Volume pour la persistance des données
- Variables d’environnement définies via `FLASK_ENV`

## Intégration et déploiement continus (CI/CD)

Un pipeline Jenkins a été mis en place pour automatiser :

1. Le clonage du dépôt GitHub
2. La construction de l’image Docker
3. Le déploiement via Docker Compose
4. Le nettoyage automatique après exécution

Extrait des commandes utilisées :

```bash
docker build -t roy61/to-do_list_web_app-web .
docker-compose up -d
docker-compose down
```

## Déploiement Kubernetes
### Fichier deployment.yaml
- Déploiement avec trois réplicas pour assurer la haute disponibilité
- Utilisation de l’image depuis Docker Hub

### Service Kubernetes
- Type LoadBalancer, exposant l’application en externe
- Redirection du port 80 vers 5000 dans le conteneur

## Mise à jour continue
- Rebuild de l’image Docker à chaque changement de code
- Application des mises à jour via :

  ```bash
  kubectl apply -f deployment.yaml
  ```
- Possibilité de rollback avec :

  ```bash
  kubectl rollout undo deployment/to-dovision-deployment
  ```
## Installation locale

```bash
git clone https://github.com/Royce-LAYINDE/to-do_list_web_app.git
cd to-do_list_web_app

pip install -r requirements.txt
python app.py
```

## Structure du projet
```bash
.
├── app.py                  # Serveur Flask
├── templates/              # Pages HTML
├── static/                 # Feuilles de style
├── Dockerfile              # Image Docker
├── docker-compose.yml      # Déploiement local
├── Jenkinsfile             # Pipeline Jenkins
└── deployment.yaml         # Déploiement Kubernetes
