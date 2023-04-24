# base image  
FROM python:3.8   

# set work directory  
RUN mkdir /faceApp

WORKDIR /faceApp

# install dependencies  
RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

# copy whole project to your docker home directory. 
ADD . /faceApp
# run this command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs  
EXPOSE 8000  
# start server  
CMD python manage.py runserver 0.0.0.0:$PORT
