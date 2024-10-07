import os
import webbrowser
from tkinter import *
from tkinter import messagebox


# Imported files needed for functionalities.
import html_tool_main
import html_tool_gui


def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

    # catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Are you sure you want to exit?"):
        # This closes app
        self.master.destroy()
        os._exit(0)


#Creates the html file if it does not already exist.
def create_file(self):
    if messagebox.showinfo("New File", "Continue to create a new HTML file."):
        f = open("main.html", "w")
        f.write("<html> <body> <h1> Stay tuned for our amazing summer sale! </h1> </body> </html>")
    else:
        pass


#Opens html in the browser, new tab.
def open_html(self):
    new = 2
    url = "main.html"
    webbrowser.open(url,new=new)

    

def new_body(self):
    if messagebox.askyesno("WARNING", "This will replace the body of the HTML file! Continue?"):
        f = open("main.html","w")
        body = """<html> <body> <h1> {} </h1> </body> </html>""".format(self.txt_body.get())
        f.write(body)
        f.close()
    



if __name__ == "__main__":
    pass