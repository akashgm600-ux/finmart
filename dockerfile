# Use Python 3.13
FROM python:3.13-slim

# Set work directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]