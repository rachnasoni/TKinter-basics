from tkinter import *
from PIL import ImageTk, Image

def handle_login():
    email= email_input.get()
    passw = pass_input.get()
    print(email,passw)
    
    if email== 'rachna' and passw=='2205':
        messagebax.showinfo("successful")
    else:
        messagebox.showerror("failed")

root = Tk()
root.title('my window')
root.iconbitmap("C:\RACHNA\photo\sign 2.0.png")
root.geometry('350x500')
root.configure(background='blue')

img= Image.open("C:\RACHNA\letsgoo.jpg")
resized_img = img.resize((100,100))
img= ImageTk.PhotoImage(resized_img)
img_label = Label(root,image=img)

text_label= Label(root,text= 'FLIPKART',fg='white',bg='blue')
text_label.pack(pady=(20,20))
text_label.config(font=('verdana',24))

email_label=Label(root,text='Enter Email',fg='white',bg='blue')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',14))

email_input=Entry(root,width=30)
email_input.pack(ipady=5,pady=(1,15))

pass_label=Label(root,text='Enter password',fg='white',bg='blue')
pass_label.pack(pady=(20,5))
pass_label.config(font=('verdana',14))

pass_input=Entry(root,width=30)
pass_input.pack(ipady=5,pady=(1,15))

login_btn= Button(root,text='Login here',bg='white',fg='black')
login_btn.pack(pady=(10,20))
print("code run success")

root.mainloop()

