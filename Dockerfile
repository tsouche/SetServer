# Use an official Python runtime as a parent image
FROM python:latest

# -- Configuration variables

# Image de DEV
ENV PORT="8080"
# Image de PROD
# ENV PORT="80"

ENV LC_ALL="C.UTF-8"
ENV LC_ALL="C.UTF-8"


# -- Install Pipenv:
RUN apt-get update && apt-get install python3-pip git -y && pip3 install pipenv

# -- Install Application into container (including pipfiles):
RUN mkdir /app
WORKDIR /app
COPY . /app

# -- Install dependencies:
RUN pipenv install
#RUN pipenv install --deploy --system

# -- expose the server port
EXPOSE $PORT

# -- Launches the server
ENTRYPOINT ["python3","setserver.py"]
