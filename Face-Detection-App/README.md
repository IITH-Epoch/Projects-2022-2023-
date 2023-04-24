# Face Detection Web App
A simple django app to detect faces in an image using mediapipe and opencv.
Please upload image files of any of the following formats:
* .jpeg
* .jpg
* .png
* .jpe
### About the Project
Face detection is used in various applications. I have tried to make one on web app.
Major technologies used are mediapipe machine learning library, opencv and django web framework.
## Getting started
To run this app,
* Update the system and clone this repository:
```bash
sudo apt-get update
git clone https://github.com/aaryan200/face_detection_app.git
```
* Head over to project directory and install all the dependencies.
```bash
cd Face-Detection-App/
```
```bash
pip install -r requirements.txt
```
Note: You may have to install some additional dependcies, if they are not present on your system already.
```bash
sudo apt-get install ffmpeg libsm6 libxext6  -y
```
* Run the app
```bash
python manage.py runserver
```
Copy and paste the server link in browser.
