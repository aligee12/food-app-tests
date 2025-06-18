FROM python:3.9-slim

# Install only Chromium (NOT chromedriver)
RUN apt-get update && apt-get install -y \
    chromium \
    fonts-liberation \
    wget \
    gnupg \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Let Selenium know where Chromium is
ENV CHROME_BIN=/usr/bin/chromium

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY tests/ ./tests/

# Run the tests
CMD ["pytest", "tests/"]
