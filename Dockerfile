FROM python:3.8

# create root directory for our project in the container
RUN mkdir /yahoo_data_api

# Set the working directory to /music_service
WORKDIR /yahoo_data_api

# Copy the current directory contents into the container at /music_service
ADD . /yahoo_data_api

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt