from tkinter import *
from tkinter import simpledialog, filedialog
from tkmacosx import Button


window = Tk()
window.title("Notepad")
window.geometry("650x800")
window.resizable(False, False)


scrolly = Scrollbar(window, orient = VERTICAL) 
scrolly.pack(side = RIGHT, fill = Y) 


note_text = Text(window, width = 85, height = 55, wrap = WORD, undo = True, yscrollcommand = scrolly.set)
note_text.place(x = 10, y = 60)

scrolly.config(command = note_text.yview) 

def file_save():
    notes = note_text.get(1.0, END)
    file_name = simpledialog.askstring("File Name", "Enter the file name you would like:")
    with open(file_name + ".txt", "w") as q:
        q.write(notes)
        q.close()

def open_file():
    global note_text
    file = filedialog.askopenfile(title = "Select a file to open:", defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])
    file.name
    if file == "":
        file = None
    else:
        note_text.delete(1.0, END)
        file = file.read()
        note_text.insert(1.0, file)


save_f = Button(window, text = "Save File", font= ("arial", 18), bg = "red", fg = "black", borderless = True, command=file_save)
save_f.place(y = 10, x = 10)


open_f = Button(window, text = "Open", bg = "green", fg = "black", font= ("arial", 18), command=open_file)
open_f.place(y = 10, x = 140)
