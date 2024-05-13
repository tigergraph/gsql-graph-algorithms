# Use an official Python runtime as a parent image
FROM python:3.9-slim
# FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /my_home

# Copy the current directory contents into the container
COPY ./test /my_home/test
COPY ./requirements.txt /my_home/requirements.txt
# COPY ./script.py /my_home/script.py
# COPY ./hello.sh /home/hello.sh

# Install any needed packages specified in requirements.txt
# RUN python pip install --no-cache-dir -r /home/requirements.txt
RUN apt update
# RUN apt install python3 python3-pip -y
RUN pip install --no-cache-dir -r /my_home/requirements.txt
# RUN chmod +x hello.sh

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
# ENV NAME World
ENV LOGLEVEL="INFO"

# run test1.py
# CMD ["python", "test/setup.py"]
CMD python test/setup.py; pytest --junitxml "output.xml" -n 4
# CMD ["./hello.sh"]
# RUN python script.py
# CMD ["python", "/script.py"]
