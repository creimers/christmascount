FROM python:3.6
# RUN apt-get -qq update && apt-get install -y binutils libproj-dev gdal-bin
ADD . /project
WORKDIR /project

RUN pip install -r requirements.txt
# RUN pip install -r requirements.txt
# CMD ['python', 'manage.py', 'runserver', '0.0.0.0:8000']
