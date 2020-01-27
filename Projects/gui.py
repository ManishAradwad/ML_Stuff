from tkinter import *
import tkinter as tk
import PIL.Image, PIL.ImageDraw

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
        self.penwidth = 10
        self.drawWidgets()
        self.c.bind('<B1-Motion>',self.paint)#drawing the line 
        self.c.bind('<ButtonRelease-1>',self.reset)

    def paint(self,e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x,self.old_y,e.x,e.y,width=self.penwidth,fill=self.color_fg,capstyle=ROUND,smooth=True)

        self.old_x = e.x
        self.old_y = e.y

    def reset(self,e):    #reseting or cleaning the canvas 
        self.old_x = None
        self.old_y = None      

    def clear(self):
        self.c.delete(ALL)

    def classify(self):
        ps = self.canvas.postscript(colormode="color")
        img = PIL.Image.open(io.BytesIO(ps.encode('utf-8')))
        digit, acc = predict_image(img)
        # self.label.configure(text = str(digit) + ', ' + str(int(acc*100)) + '%')

    def drawWidgets(self):
        self.controls = Frame(self.master,padx = 5,pady = 5)
        self.c = Canvas(self.master,width=300,height=300,bg=self.color_bg,cursor='dot',)
        # self.label = tkinter.Label(self, text="Handwritten Digit Recogniser", font = "Lobster", size = 48)
        # self.c.title("Handwritten_Image_Recogniser")
        self.c.pack(fill=BOTH,expand=True)
        self.clr_button = self.tk.Button(self, text = "Clear", command = self.clear)
        self.classify_button = self.tk.Button(self, text = "Recognise", command = self.classify)

if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('Application')
    root.mainloop()
