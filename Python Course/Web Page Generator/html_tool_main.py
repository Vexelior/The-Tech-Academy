from tkinter import *
import tkinter as tk
from tkinter import messagebox


import html_tool_gui
import html_tool_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

         # Defining our master frame configuration.
        self.master = master
        self.master.minsize(350,150) #(Height, Width)
        self.master.maxsize(350,150)

        # This CenterWindow method will center our app on the user's screen.
        html_tool_func.center_window(self,500,400)
        self.master.title("HTML Tool")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: html_tool_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module, 
        # keeping the code comparmentalized and clutter free
        html_tool_gui.load_gui(self)

        # Instantiate the Tkinter menu dropdown object
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: html_tool_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This HTML Tool") # add_command is a child menubar item of the add_cascde parent item
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)
       
        self.master.config(menu=menubar, borderwidth='1')


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
