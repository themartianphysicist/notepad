from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0, END)
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All files", "*.*"),
                                                              ("Text Documents",
                                                               "*.txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Document1.txt', defaultextension=".txt", filetypes=[("All files", "*.*"),
                                                              ("Text Documents",
                                                               "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")

    else:
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

def cut():
    textarea.event_generate("<<Cut>>")

def copy():
    textarea.event_generate("<<Copy>>")

def paste():
    textarea.event_generate("<<Paste>>")

def about():
    showinfo("About Notepad", "Notepad created by Kartikaye")

if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("note.png")
    root.geometry("644x788")


    textarea = Text(root, font="lucida 19")
    textarea.pack(fill=BOTH, expand=True)
    file = None

    # Menubar
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    # Open new file
    filemenu.add_command(label="New", command=newFile)

    # Open a file
    filemenu.add_command(label="Open", command=openFile)

    # To save the current file

    filemenu.add_command(label="Save", command=saveFile)
    filemenu.add_separator()
    
    filemenu.add_command(label="Exit", command=quitApp)
    menubar.add_cascade(label="File", menu=filemenu)
    


    # Edit menu
    editmenu = Menu(menubar, tearoff=0)
    # Cut, copy and paste
    editmenu.add_command(label="Cut", command=cut)
    editmenu.add_command(label="Copy", command=copy)
    editmenu.add_command(label="Paste", command=paste)
    menubar.add_cascade(label="Edit", menu=editmenu)

    # Help menu
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About notepad", command=about)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)

    # Scrollbar
    scrollbar = Scrollbar(textarea)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=textarea.yview)
    textarea.config(yscrollcommand=scrollbar.set)

    root.mainloop()