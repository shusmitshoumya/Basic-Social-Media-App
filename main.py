from tkinter import *
from customtkinter import *

root = CTk()
#set_default_color_theme("blue")

frame = Frame(root, bg="#1B3C53")
frame.pack(fill=BOTH, expand=TRUE, side="top")

root.geometry("1000x700")
root.title("Social Media App")
root.resizable(0,0)


def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()


def home_screen() :


    heading = Label(frame, text="Welcome to (App Name)", bg = "#1B3C53", fg="white", font="Roboto")
    heading.place(relx = 0.5, rely = 0.2, anchor = CENTER)

    UserLabel = CTkLabel(master = frame, text='Username', width=40, height=28, fg_color='transparent')
    UserLabel.place(relx = 0.3, rely=0.4)

    userEntry = CTkEntry(master=frame, placeholder_text="Username", width=250)
    userEntry.place(relx = 0.4, rely =0.4)

    passwordLabel = CTkLabel(master = frame, text='Password', width=40, height=28, fg_color='transparent')
    passwordLabel.place(relx = 0.3, rely=0.5)

    passwordEntry = CTkEntry(master=frame, placeholder_text="Password", show = "*", width=250)
    passwordEntry.place(relx = 0.4, rely=0.5)

    def register():

        #pass
        clear_frame()

        userName = userEntry.get()
        password = passwordEntry.get()

    def login() :

        clear_frame()

        userName = userEntry.get()
        password = passwordEntry.get()

    loginBtn = CTkButton(master = frame, text='Log in', fg_color="#0D5EA6", command=login, corner_radius=30, height = 30) 
    loginBtn.place(relx = 0.3, rely=0.65)

    regBtn = CTkButton(master=frame, text="Register", fg_color="#0D5EA6", command=register, corner_radius=30, height = 30)
    regBtn.place(relx=0.51, rely =0.65)


home_screen()

root.mainloop()