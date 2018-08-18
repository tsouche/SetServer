FROM ubuntu:18.04 as set_app_dev

# -- Configuration variables

# Image de DEV
ENV PORT="8080"
# Image de PROD
# ENV PORT="80"

ENV LC_ALL="C.UTF-8"
ENV LC_ALL="C.UTF-8"



# -- Install Pipenv:
RUN apt update && apt install python3-pip git -y && pip3 install pipenv

# -- Install Application into container (including pipfiles):
RUN mkdir /app
WORKDIR /app
COPY . /app

# -- Adding Pipfiles  -- obsolete (already covered by previous COPY instruction)
# COPY pipfile pipfile
# COPY pipfile.lock pipfile.lock

# -- Install dependencies:
RUN pipenv install --deploy --system

# -- expose the server port
EXPOSE $PORT

# -- Launches the server
ENTRYPOINT ["python3","setserver.py"]
