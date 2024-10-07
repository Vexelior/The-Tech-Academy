# Imports
from tkinter import *
import tkinter as tk
import html_tool_main
import html_tool_func

def load_gui(self):
    #Input field for a new body
    self.lbl_body = tk.Label(self.master,text='New Body:')
    self.lbl_body.grid(row=0,column=1,padx=(25,0),pady=(10,0),sticky=N+W)
    
    #These are our boxes for outputs and inputs.
    self.txt_body = tk.Entry(self.master,text='')
    self.txt_body.grid(row=1,column=1,rowspan=1,columnspan=4,padx=(30,40),pady=(0,0),sticky=N+W)

    #Buttons
    self.btn_create = tk.Button(self.master,width=10,height=1,text='Create',command=lambda: html_tool_func.create_file(self))
    self.btn_create.grid(row=5,column=1,padx=(25,0),pady=(35,10),sticky=W)
    self.btn_open = tk.Button(self.master,width=10,height=1,text='Open',command=lambda: html_tool_func.open_html(self))
    self.btn_open.grid(row=5,column=2,padx=(25,0),pady=(35,10),sticky=W)
    self.btn_open = tk.Button(self.master,width=10,height=1,text='Submit',command=lambda: html_tool_func.new_body(self))
    self.btn_open.grid(row=5,column=3,padx=(25,0),pady=(35,10),sticky=W)

if __name__ == "__main__":
    pass