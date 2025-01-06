# From the repository, download the python image which is required for the project 
FROM python:alpine

# This command tells Docker to set /app as the working directory.
WORKDIR /app

# This command installs and set up system dependencies inside a Docker container
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y pkg-config \
    && rm -rf /var/lib/apt/lists/*  

# (rm -rf /var/lib/apt/lists/*) - When apt-get update runs, it downloads package index files to /var/lib/apt/lists/. These files are no longer needed after the packages have been installed, so they are deleted in this step to reduce the image size.

# Copy the requirements file into the container
COPY requirements.txt .

# Install app dependencies
RUN pip install mysqlclient
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Specify the command to run your application
CMD ["python", "pythonclock.py"]
