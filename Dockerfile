FROM python:2.7.13
FROM node

RUN npm install -g artillery && apt-get update && apt-get -y install python-matplotlib

VOLUME ["/data", "/bin"]
