# Stage 1: Builder stage
FROM python:3.10.11-slim as builder

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install build dependencies and create virtual environment
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir -U pip setuptools && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Stage 2: Final stage
FROM python:3.10.11-slim

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Set working directory
WORKDIR /app

# Copy application files
COPY main.py .
COPY templates/ templates/
COPY titanic_model.pkl .

# Make sure we use the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]