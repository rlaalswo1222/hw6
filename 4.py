from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
#김민재 2021041070
def keyEvent(event) :
    photo = PhotoImage(file = filename)
    if chr(event.keycode)== "&":
        photo = photo.zoom(2,2)
        pLabel.configure(image = photo)
        pLabel.image = photo
    elif chr(event.keycode)== "(":
        photo = photo.subsample(2,2)
        pLabel.configure(image = photo)
        pLabel.image = photo
       


def func_open() :
    global filename
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit() :
    window.quit()
    window.destroy()

window = Tk()
window.geometry("500x500")
window.title("명화 감상하기")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand=1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)
window.bind("<Key>",keyEvent) 
window.mainloop()
