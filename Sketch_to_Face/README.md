# GAN model for generating faces from sketches

This Project was made by Aayush Kumar, Core Member of Epoch (2022-2023)

## About the Project
An image generation system using GAN to turn face sketches into realistic photos

## Data Generation

I have used CFD for the face images. Sketches are generated using Get_Sketch file.

## Model

This GAN model is based on the pix2pix paper. The generator is a U-Net based architecture. The discriminator is a convolutional PatchGAN classifier.

## Setup:

To run this project, we need TensorFlow installed on our system.  
Run the following command to install tensorflow:  
```
pip install tensorflow
```

