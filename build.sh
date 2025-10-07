#!/bin/bash

# Variables
ImageName="flask-api"
Tag="latest"

# 1. Créer requirements.txt
echo "flask==3.0.0" > requirements.txt

# 2. Créer Dockerfile
cat <<EOF > Dockerfile
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier requirements et installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY . .

# Exposer le port Flask
EXPOSE 5000

# Lancer l'application
CMD ["python", "flaskApp.py"]
EOF

# 3. Construire l'image
sudo docker build -t "${ImageName}:${Tag}" .

# 4. Connexion à Docker Hub
sudo docker login

# 5. Push sur Docker Hub
sudo docker push "${ImageName}:${Tag}"

echo "✅ Image ${ImageName}:${Tag} build & push completed!"

