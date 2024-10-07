from tkinter import *
import tkinter as tk
from tkinter import messagebox
import transfer_script_gui
import transfer_script_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.maxsize(615, 390)
        self.master.minsize(615, 390)
        self.master.title("File Transfer")
        self.master.configure(bg="#333")
        self.master.protocol('WM_DELETE_WINDOW',
        lambda: transfer_script_func.ask_quit(self)(self))
        transfer_script_func.center_window(self, 650, 500)
        transfer_script_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()