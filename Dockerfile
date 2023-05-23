# Use the scratch base image
FROM scratch

# Add your application executable to the container
ADD myapp /

# Specify the command to run your application
CMD ["/myapp"]

# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Specify the command to run your application
CMD ["python", "app.py"]

