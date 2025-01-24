# Utiliser une image Python slim comme base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt /app/

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers dans le conteneur
COPY . /app

# Exposer le port sur lequel l'application écoute
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
