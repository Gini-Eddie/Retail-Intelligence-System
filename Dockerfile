# Use a slim Python image to keep the container lightweight
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies needed for some Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt-packages/*

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Streamlit uses port 8501 by default
EXPOSE 8501

# Healthcheck to make sure the app is running
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# The command to run your app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]