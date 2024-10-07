#This is the original script prior to creating the GUI application.

import shutil
import os
import time
from tkinter import *

source = 'D:/School/The-Tech-Academy-Python-Course/Assignments/File Transfer Assignment/Created Files'
destination = 'D:/School/The-Tech-Academy-Python-Course/Assignments/File Transfer Assignment/Moved Files/'

for file in os.listdir(source):
    day = 24 * 60 * 60
    now = time.time()
    past = now - day
    source_file = os.path.join(source, file) 
    mod_time = os.path.getmtime(source_file)
    if mod_time > past: 
        destination_file = os.path.join(destination, file) 
        shutil.move(source_file, destination_file)
        print(f"{file} has been moved.") 