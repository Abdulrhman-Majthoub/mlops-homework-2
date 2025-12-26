FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first and install (faster builds)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ src/

# Expose port for FastAPI
EXPOSE 8000

# Run the API
CMD ["uvicorn", "src.model_server:app", "--host", "0.0.0.0", "--port", "8000"]
