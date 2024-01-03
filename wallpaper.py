from tkinter import *
from PIL import ImageTk, Image
import os

def rotate_img():
  global counter
  img_label.config(image=img_arr[counter%len(img_arr)])
  counter= counter+1
  
counter=1
root= Tk()
root.title("wallpaper viewer")

root.geometry('500x500')
root.configure(background='black')

files= os.listdir(r"C:\RACHNA\photo")
img_arr=[]
for file in files:
    path = os.path.join(r"C:\RACHNA\photo",file)
    img = Image.open(path)
    resized_img= img.resize((200,300))
    img_arr.append(ImageTk.PhotoImage(resized_img))
print(img_arr)

img_label=Label(root,image=img_arr[0])
img_label.pack(pady=(15,10))

next_btn=Button(root,text='Next',bg='white',fg='black',width=25,height=2,command=rotate_img)
next_btn.pack()

root.mainloop()
