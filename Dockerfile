# Use official Python base image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy project files to the container
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80
EXPOSE 80

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]