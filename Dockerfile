# Use official Python image for building dependencies
FROM python:3.10 AS builder

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Use Distroless as the final image
FROM gcr.io/distroless/python3

# Set working directory
WORKDIR /app

# Copy files and installed dependencies from builder stage
COPY --from=builder /app /app

# Expose port 8000
EXPOSE 8000

# Run Gunicorn server
CMD ["gunicorn", "auth_service.wsgi:application", "--bind", "0.0.0.0:8000"]
