FROM python:3.9-slim

# Install only Chromium (no chromedriver)
RUN apt-get update && apt-get install -y \
    chromium \
    wget \
    gnupg \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Let Selenium know where Chromium binary is
ENV CHROME_BIN=/usr/bin/chromium

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY tests/ ./tests/

CMD ["pytest", "tests/"]
