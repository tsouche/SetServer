FROM python:3.6

#ENV LC_ALL="C.UTF-8"

# We assume that python3 and pip3 are already isntalled

# -- Install Application into container (including pipfiles):
RUN mkdir /app
WORKDIR /app
# copy the app files
COPY ./app_players.py ./shared.py ./shared_db.py ./requirements.txt /app/
# copy the test scripts
COPY ./reference_test_data.py ./test_app_players.py ./test_utils.py /app/
#RUN ls -al /app

#RUN which python
#RUN ls -al /usr/local/bin/pyt*
#RUN python --version
#RUN /usr/local/bin/python --version
RUN pip install -r requirements.txt

# -- expose the server port
EXPOSE 8080

# -- Launches the server
#ENTRYPOINT ["python","-m","unittest","test_app_players.py"]
ENTRYPOINT ["ls","-al"]
