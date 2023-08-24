import streamlit as st
import cv2
import torch
from torchvision import transforms
import os
from PIL import Image
import numpy as np


FPATH = os.path.join(os.getcwd(), '..', 'Model Training')
PATH = os.path.join(FPATH, 'model.pt')
model = torch.load(PATH)


class ContrastiveLoss:
    def __init__(self, margin = 1.0) :
        self.margin = margin

    def __call__(self, output1, output2, label) :
        euclidean_distance = F.pairwise_distance(output1, output2)
        loss_contrastive = torch.mean(label * torch.pow(euclidean_distance, 2) + (1 - label) * torch.pow(torch.clamp(self.margin - euclidean_distance, min = 0.0), 2))
        return loss_contrastive


def identify(img):
    classifier = cv2.CascadeClassifier(cv2.data.haarcascades + '/Users/tej/Documents/IITH/Projects/Personal'
                                                               '/FacialRecognition/GUI/haarcascade_frontalface_default'
                                                               '.xml')
    x, y, width, height = classifier.detectMultiScale(img, minNeighbors=0)[0]
    return cv2.cvtColor(img[y: (y + height)][x: (x + width)], cv2.COLOR_BGR2GRAY)


def compare(imgA, imgB_arr):
    imgB = identify(imgB_arr)
    # Converting the NumPy array into an Image
    imgA = Image.fromarray(imgA)
    imgB = Image.fromarray(imgB)
    # Applying transformation to Resize (64, 64) and Converting the Images into a Tensor
    trnfrms = transforms.Compose([transforms.Resize((64, 64)), transforms.ToTensor()])

    imgA = trnfrms(imgA)
    imgB = trnfrms(imgB)

    outputA = model(imgA)
    outputB = model(imgB)

    criterion = ContrastiveLoss()
    return criterion(outputA, outputB, torch.tensor(1.))


def Register():
    st.title("Register if you haven't already!")
    username = st.text_input("Enter Username")
    # capture = st.button("Capture Photo")
    capture = st.camera_input("Capture Photo")

    if capture:
        img = Image.open(capture)
        img_arr = np.array(img)
        captured_image_path = f"known_images/{username}.png"
        os.makedirs(os.path.dirname(captured_image_path), exist_ok=True)
        cv2.imwrite(captured_image_path, identify(img_arr))


def MarkAttendance():
    st.title("Mark your Attendance!")
    username = st.text_input("Enter Username")
    capture = st.camera_input("Capture Photo")

    if capture:
        imgB = Image.open(capture)
        imgB_arr = np.array(imgB)
        known_image_path = f"known_images/{username}.png"
        imgA = cv2.imread(known_image_path)
        if compare(imgA, imgB_arr) > 0.8:
            st.write("Attendance Marked!")



if __name__ == "__main__":
    st.sidebar.title("Attendance System")
    option = st.sidebar.radio("Select Option:", ("Register New Person", "Mark Attendance"))

    if option == "Register New Person":
        Register()

    elif option == "Mark Attendance":
        MarkAttendance()
