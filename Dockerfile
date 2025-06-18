FROM python:3.9-slim

# Install system dependencies including Chromium and ChromeDriver
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    wget \
    gnupg \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables so Selenium knows where the browser is
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy test files
COPY tests/ ./tests/

# Default command to run tests
CMD ["pytest", "tests/"]
