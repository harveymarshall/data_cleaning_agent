FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies and uv
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && curl -LsSf https://astral.sh/uv/install.sh | sh \
    && rm -rf /var/lib/apt/lists/*

# Add uv to PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy requirements file
COPY pyproject.toml .

# Install Python dependencies
RUN uv pip install --system -r pyproject.toml

# Copy .env file
COPY .env .

# Copy application code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI app
CMD ["fastapi", "run", "src/main.py", "--host", "0.0.0.0", "--port", "8000"]
