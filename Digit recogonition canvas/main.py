import tkinter as tk
from PIL import Image, ImageDraw
import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class ImageGenerator:
    def __init__(self, parent, posx, posy, *kwargs):
        self.parent = parent
        self.posx = posx
        self.posy = posy
        self.sizex = 280
        self.sizey = 280

        self.penColor = "white"  
        self.backColor = "black"  
        self.penWidth = 5
        self.drawing_area = tk.Canvas(
            self.parent, width=self.sizex, height=self.sizey, bg=self.backColor
        )
        self.drawing_area.place(x=self.posx, y=self.posy)
        self.drawing_area.bind("<B1-Motion>", self.motion)
        self.button = tk.Button(
            self.parent, text="Predict", width=5, bg="white", command=self.predict
        )
        self.button.place(x=self.sizex / 7, y=self.sizey + 20)
        self.button1 = tk.Button(
            self.parent, text="Clear", width=5, bg="white", command=self.clear
        )
        self.button1.place(x=(self.sizex / 7) + 80, y=self.sizey + 20)

        self.image = Image.new("RGB", (self.sizex, self.sizey), (0, 0, 0))
        self.draw = ImageDraw.Draw(self.image)
        self.prediction_var = tk.StringVar()
        self.prediction_var.set("Draw a single digit number at the center")
        self.label = tk.Entry(textvariable=self.prediction_var,bg="white",width=100,state="readonly")
        self.label.place(x=(self.sizex / 7 ), y=self.sizey + 60)

    def predict(self):
        from src.predictor import predict
        output,prob = predict(self.image)
        if prob < 0.7:
            self.prediction = "The model can't understand the handwritting properly but it guess the output is {} with probability {}%".format(output,prob*100)
            
        else:
            self.prediction = "Output is {} with probability {}%".format(output,prob*100)

        self.prediction_var.set("Draw a single digit number at the center")
        self.prediction_var.set(self.prediction)

    def clear(self):
        self.drawing_area.delete("all")
        self.image = Image.new("RGB", (self.sizex, self.sizey), (0, 0, 0))
        self.draw = ImageDraw.Draw(self.image)
        self.prediction_var.set("Draw a single digit number at the center")

    def motion(self, event):
        self.drawing_area.create_oval(
            event.x,
            event.y,
            event.x + self.penWidth,
            event.y + self.penWidth,
            fill=self.penColor,
            outline=self.penColor,
        )  

        self.draw.ellipse(
            (
                (event.x, event.y),
                (event.x + self.penWidth, event.y + self.penWidth),
            ),
            fill=self.penColor,
            outline=self.penColor,
            width=self.penWidth,
        ) 



if __name__ == "__main__":
    
    if not os.path.exists("./src/myModel.h5") or (len(sys.argv) >= 2 and sys.argv[1] == "rebuild"):
        if not os.path.exists("./src/myModel.h5"):
            print("Model Not Found")
            print("Building model:")
        else:
            print("Rebuilding Model:")
        from src.Model_Generator import CreateModel
        CreateModel()

    root = tk.Tk()
    root.wm_geometry("%dx%d+%d+%d" % (900, 400, 10, 10))
    root.config(bg="white")
    ImageGenerator(root, 10, 10)
    root.mainloop()