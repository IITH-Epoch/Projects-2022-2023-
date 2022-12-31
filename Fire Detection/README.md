# Fire Detection

This Project was developed by [Nelakuditi Rahul Naga](https://github.com/Rahul27n) , Core Member of [Epoch](https://github.com/IITH-Epoch) (2022-2023). The brief outline of the contents of this project is as follows :
- The InceptionV3 folder contains an **InceptionV3** model that outputs a probability regarding the presence (or) absence of fire in an image.
- The Yolov5 folder contains an **Yolov5** model that detects the presence of fire in both images and videos. It provides an appropriate output with bounding boxes around
the fire region if it is present. It also contains a weights file named **best.pt** which is obtained after training the model on a GPU. There is also a file named
**configuration.yaml** that contains information about paths to training and validation data.
- The test data used for testing the models is present in the Data folder. The information about datasets used to train the models has been mentioned in the Jupyter
notebooks itself.
- The results obtained after training and testing the models are present in the Results folder.
