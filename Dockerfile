
# Use official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Expose port 8000 for Django
EXPOSE 8000

# Run Django server
CMD ["gunicorn", "auth_service.wsgi:application", "--bind", "0.0.0.0:8000"]
