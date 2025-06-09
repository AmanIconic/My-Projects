import random
import string
import customtkinter as ctk

a=["High","Medium","Low"]
#setting apperance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#fuction
def randompass():
    length=l3.get()
    complexity = c1.get()

    if not length:
        result.configure(text="Enter A Valid Length")
        return
    
    length=int(length)
    if length<=0:
        result.configure(text="Enter Length In Positve Interger")
        return
    
    if complexity=="Low":
        chracter = string.ascii_lowercase
    elif complexity=="Medium":
        chracter = string.ascii_letters + string.digits
    else:
        chracter = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(chracter) for i in range(length))
    result.configure(text=f"Your Password is -> {password}")
    
#making window
window = ctk.CTk()
window.title("RANDOM PASSWORD GENERATOR")
window.geometry("500x500")
window.resizable(False,False)

l1=ctk.CTkLabel(window,text="RANDOM PASSWORD GENERATOR" , font=("Arial Rounded MT Bold",24))
l1.pack(pady=10)

l2=ctk.CTkLabel(window,text="Secure your digital world—one strong password at a time.",font=("Arial",18))
l2.pack(pady=15)

l3=ctk.CTkEntry(window,placeholder_text="Enter the length of your password",font=("Arial",16),width=300)
l3.pack(pady=20)

l4=ctk.CTkLabel(window,text="Choose Complexity For Your Password",font=("Arial",18))
l4.pack()
c1=ctk.CTkOptionMenu(window,values=a,width=300,height=30,font=("Arial",16))
c1.pack(pady=15)
c1.set('High')

button=ctk.CTkButton(window,text="Generate",command=randompass,font=("Arial Bold",20),width=200)
button.pack(pady=20)

result=ctk.CTkLabel(window,text="Your Generated Pass Will Show Here..",font=("Arial",18))
result.pack(pady=15)

window.mainloop()