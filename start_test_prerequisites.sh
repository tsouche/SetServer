#!/usr/bin/env bash

# The unit and integration tests require a mongo DB server to be running, according to the parameters set in
# constants.py.

systemctl start mongodb
systemctl status mongodb

pipenv run python setserver.py

echo "Ready to start tests"

