from tkinter import *
from tkinter import messagebox
import pandas as pd
import os
 
window = Tk()
 
window.title("Usuwanie dużej ilości KW")
 
window.geometry('300x200')

class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        try:
            # For Mac OS
            tw.tk.call("::tk::unsupported::MacWindowStyle",
                       "style", tw._w,
                       "help", "noActivates")
        except TclError:
            pass
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def createToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
 
def clicked():
 
    messagebox.showinfo('Komunikat', 'Dane zostały wygenerowane')
def clicked2():
    messagebox.showerror('Error', 'Plik nie został wygenerowany')

def script():
    if os.path.exists('./x1.txt'):
        k = pd.read_csv('x1.txt', sep=" ")
        d = k.iloc[:, 1:2]
        d.to_csv('Cif do wyzerowania.txt', sep=' ', index=False, header=False)
    else:
        messagebox.showerror('Error', 'Brak pliku o nazwie x1.txt')


btn = Button(window,text='Wygeneruj zapytanie SQL', command= lambda: [script(), check()])
createToolTip(btn, "Funckja wymaga pliku x1 w folderze docelowym")


btn2 = Button(window,text='Wygeneruj update', command= lambda: [script(), check()])
createToolTip(btn2, "Kicuś ma seksi pupku")

btn3 = Button(window,text='Sprawdź dane', command= lambda: [script(), check()])
createToolTip(btn3, "Funckja wymaga xxxxxx")


def check():
    if os.path.exists('./Cif do wyzerowania.txt'):
        messagebox.showinfo('Komunikat', 'Dane zostały wygenerowane')
    else:
        messagebox.showerror('Error', 'Plik nie został wygenerowany')

 
btn.pack(side="top", fill="x")
btn2.pack(side="top", fill="x")
btn3.pack(side="top", fill="x")

lr = Label(window, text='Zerowanie dużej ilośći CIFów 2019')
lr.place(relx=1.0, rely=1.0, anchor='se')
window.mainloop()