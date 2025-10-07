#!/bin/bash

# Variables
IMAGE_NAME="flask-api"
USERNAME="test330"
REPO="$USERNAME/$IMAGE_NAME"
FILE_TO_WATCH="flaskApp.py"

echo "🚀 Watching $FILE_TO_WATCH for changes..."

while true; do
    # Surveille les modifications du fichier
    inotifywait -e modify $FILE_TO_WATCH

    echo "⚡ Change detected in $FILE_TO_WATCH. Rebuilding Docker image..."

    # Build de l'image avec le tag "latest"
    docker build -t $IMAGE_NAME:latest .

    # Générer un tag dynamique basé sur la date et l'heure
    TAG=$(date +%Y%m%d%H%M%S)

    # Tag pour Docker Hub
    docker tag $IMAGE_NAME:latest $REPO:$TAG

    # Push vers Docker Hub
    echo "📤 Pushing $REPO:$TAG to Docker Hub..."
    docker push $REPO:$TAG

    echo "✅ Done. Waiting for next change..."
done

