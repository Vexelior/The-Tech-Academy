import os
import shutil
import os
import time
import tkinter as tk
from os import listdir
from os.path import isfile, join
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from tkinter import filedialog
import transfer_script_main
import transfer_script_gui

def center_window(self, w, h):  # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo
  
# Catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Are you sure you want to exit?"):
        # This closes app
        self.master.destroy()
        os._exit(0)

def src_dir(self):
    dirpath = filedialog.askdirectory()
    self.src_ent.insert(END, dirpath)
    if self.src_ent.get() == "":
        messagebox.showinfo("Error", "Please select a folder.")

def dest_dir(self):
    dirpath = filedialog.askdirectory()
    self.dest_ent.insert(END, dirpath)
    if self.dest_ent.get() == "":
        messagebox.showinfo("Error", "Please select a folder.")

def check_files(self):
    day = 24 * 60 * 60
    now = time.time()
    past = now - day
    source = self.src_ent.get()
    destination = self.dest_ent.get()
    moved_files = False
    if source == "" or destination == "":
        messagebox.showinfo("Error", "Please select folders for source and destination.")
        return

    for file in os.listdir(self.src_ent.get()):
        source_file = os.path.join(source, file) 
        mod_time = os.path.getmtime(source_file)
        if mod_time > past: 
            destination_file = os.path.join(destination, file)
            shutil.move(source_file, destination_file)
            moved_files = True
            print(f"{file} has been moved.")
            
    if moved_files == True:
        messagebox.showinfo("Success", "Files have been moved.")
    else:
        messagebox.showinfo("Error", "No files to be moved.")

if __name__ == "__main__":
    pass