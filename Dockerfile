# Use an official Python runtime as a parent image
FROM python:3.x

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install project dependencies
RUN pip install -r requirements.txt

# Expose a port for Gunicorn
EXPOSE 8000

# Run database migrations during the image build process
RUN python manage.py migrate

# Start the Django application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "DREAMBAZAAR.wsgi:application"]

//