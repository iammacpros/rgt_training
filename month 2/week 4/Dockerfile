# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install pipenv
RUN pip install --upgrade pip && pip install pipenv

# Copy Pipfiles
COPY requirements.txt /app/



# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Expose FastAPI port
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
