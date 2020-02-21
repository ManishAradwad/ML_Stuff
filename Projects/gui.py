from tkinter import *
import numpy as np
import tensorflow as tf
from PIL import Image, ImageDraw

remodel = tf.keras.models.load_model("HandWritten_Digit_Recognizer.h5")

# Function which gets drawn number image as input and gives the prediction as output
def predict_image(img):
  img = np.array(img.resize(28,28).convert('L')) # Resizing and converting it to GrayScale and converting it to np array
  img = img.reshape(1,28,28,1)/255.0 # Reshaping to create a batch and normalizing
  res = remodel.predict([img])[0] # Predicting the number
  return np.argmax(res), max(res)

class main:
    def __init__(self,master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.drawWidgets()
        self.c.bind('<B1-Motion>',self.paint)#drawing the line 
        self.c.bind('<ButtonRelease-1>',self.reset)

    def save_as_png(self, image, fileName = "digit.png"):
    # save postscipt image 
    # canvas.postscript(file = fileName + '.eps') 
    # # use PIL to convert to PNG 
    # img = Image.open(fileName + '.eps') 
    # img.save(fileName + '.JPEG', 'JPEG') 
        image.save(fileName)


    def paint(self,e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x,self.old_y,e.x,e.y,width=self.penwidth,fill=self.color_fg,capstyle=ROUND,smooth=True)
            self.draw.line(self.old_x,self.old_y,e.x,e.y,width=self.penwidth,fill=self.color_fg)

        self.old_x = e.x
        self.old_y = e.y

    def reset(self,e):    #reseting or cleaning the canvas 
        self.old_x = None
        self.old_y = None             

    def clear(self):
        self.c.delete(ALL)

    def drawWidgets(self):
        self.controls = Frame(self.master,padx = 5,pady = 5)
        Label(self.controls, text='Pen Width:',font=('arial 18')).grid(row=0,column=0)
        
        self.c = Canvas(self.master,width=500,height=400,bg=self.color_bg,)
        self.c.pack(fill=BOTH,expand=True)   
                
        self.image1 = Image.new("RGB", (500, 400), self.color_bg)
        self.draw = ImageDraw.Draw(self.image1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        optionmenu = Menu(menu)
        menu.add_cascade(label='Options',menu=optionmenu)
        optionmenu.add_command(label='Recognise',command=self.save_as_png(self.image1))
        optionmenu.add_command(label='Clear Canvas',command=self.clear)

if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('Handwritten Digit Recogniser')
    root.mainloop()