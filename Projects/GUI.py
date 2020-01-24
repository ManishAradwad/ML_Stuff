# Imports
from tkinter import *
import tkinter as tk
from PIL import ImageGrab, Image
import win32gui
import numpy as np

# Creating an Interactive GUI on which user will draw a number and our model will predict that number

remodel = tf.keras.models.load_model("HandWritten_Digit_Recognizer.h5")
remodel.summary()

# Function which gets drawn number image as input and gives the prediction as output
def predict_image(img):
  img = np.array(img.resize(28,28).convert('L')) # Resizing and converting it to GrayScale and converting it to np array
  img = img.reshape(1,28,28,1)/255.0 # Reshaping to create a batch and normalizing
  res = remodel.predict([img])[0] # Predicting the number
  return np.argmax(res), max(res)

class App(tk.Tk):
  def __init__(self):
    tk.Tk.__init__(self)
    self.x = self.y = 0

    # Creating elements
    self.canvas = tk.Canvas(self, width = 300, height = 300, bg = "white", cursor = "cross")
    self.label = tk.Label(self, text="Handwritten Digit Recogniser", font = "Lobster", size = 48)
    self.classify_button = tk.Button(self, text = "Recognise", command = self.classify_handwriting)
    self.clr_button = tk.Button(self, text = "Clear", command = self.clear_all)
    
    # Grid structure
    self.canvas.grid(row = 0, column = 0, pady = 2, sticky = W)
    self.label.grid(row = 0, column = 1, pady = 2, padx = 2)
    self.classify_button.grid(row = 1, column = 1, pady = 2, padx = 2)
    self.clr_button.grid(row = 1, column = 0, pady = 2)

    self.canvas.bind("<B1-Motion>", self.draw_lines)

  def clear_all(self):
    self.canvas.delete("all")

  def classify_handwriting(self):
    HWND = self.canvas.winfo_id() # Get the handle of canvas
    rect = win32gui.GetWindowRect(HWND) # Get the coordinates of canvas
    im = ImageGrab.grab(rect)

    digit, acc = predict_image(im)
    self.label.configure(text=str(digit)+', '+str(int(acc*100))+'%')

  def draw_lines(self,event):
      self.x = event.x
      self.y = event.y
      r = 8
      self.canvas.create_oval(self.x-r, self.y-r, self.x+r, self.y+r, fill='black')

app = App()
mainloop()