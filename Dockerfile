FROM python:3.12-slim

# Installer dépendances système
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier requirements et installer
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code
COPY . .

# Exposer le port Flask
EXPOSE 5000

# Variables d'environnement pour Flask
ENV FLASK_APP=app.app
ENV FLASK_ENV=production

# Lancer Flask
CMD ["flask", "run", "--host=0.0.0.0"]
