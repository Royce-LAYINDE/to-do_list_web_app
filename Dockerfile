# Utiliser une image Python officielle comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /

# Copier tous les fichiers de l'application
COPY . /app

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt


# Exposer le port sur lequel l'application Flask va écouter
EXPOSE 5000

# Commande pour lancer l'application Flask
CMD ["python", "app.py"]