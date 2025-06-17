FROM python:3.9-slim

# Install system dependencies for webdriver-manager
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy test files
COPY tests/ ./tests/

# Command to run tests
CMD ["pytest", "tests/"]