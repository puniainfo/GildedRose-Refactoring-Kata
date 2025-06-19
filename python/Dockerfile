# Use official Python 3.12 slim base image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy only the requirements first for better layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Make sure scripts are executable (optional, if you're using shell/entry scripts)
RUN chmod +x entrypoint.sh

# Set default entrypoint
ENTRYPOINT ["sh","/app/entrypoint.sh"]
