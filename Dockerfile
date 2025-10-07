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
