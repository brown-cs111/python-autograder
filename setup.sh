#!/usr/bin/env bash

add-apt-repository ppa:deadsnakes/ppa   
apt-get update   
apt-get install -y python3.7 python3-pip python3-dev

pip3 install -r /autograder/source/python-autograder/requirements.txt
