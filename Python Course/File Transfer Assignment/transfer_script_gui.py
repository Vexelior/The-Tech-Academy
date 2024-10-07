# Imports
from tkinter import *
import tkinter as tk
import transfer_script_main
import transfer_script_func

def load_gui(self):
    self.src_lbl = tk.Label(
        self.master,
        font=("Vani", 16),
        fg="#fff",
        bg="#333",
        text="Choose Source Directory",
    )
    self.src_lbl.grid(row=0, column=0, padx=(
        160, 0), pady=(50, 0), sticky=NSEW)
    self.src_lbl.grid_rowconfigure(0, weight=1)

    self.src_ent = tk.Entry(self.master, width=40)
    self.src_ent.grid(row=1, column=0, padx=(160, 0), pady=(5, 0), sticky=NSEW)
    self.src_ent.grid_rowconfigure(0, weight=1)

    self.src_btn = tk.Button(
        self.master,
        highlightbackground="#333",
        text="Browse",
        command=lambda: transfer_script_func.src_dir(self),
    )
    self.src_btn.grid(row=2, column=0, padx=(
        160, 0), pady=(10, 0), sticky=NSEW)
    self.src_btn.grid_rowconfigure(0, weight=1)

    self.dest_lbl = tk.Label(
        self.master,
        font=("Vani", 16),
        fg="#fff",
        bg="#333",
        text="Choose Destination Directory",
    )
    self.dest_lbl.grid(row=3, column=0, padx=(
        160, 0), pady=(50, 0), sticky=NSEW)
    self.dest_lbl.grid_rowconfigure(0, weight=1)

    self.dest_ent = tk.Entry(self.master, width=40)
    self.dest_ent.grid(row=4, column=0, padx=(
        160, 0), pady=(5, 0), sticky=NSEW)
    self.dest_ent.grid_rowconfigure(0, weight=1)

    self.dest_btn = tk.Button(
        self.master,
        highlightbackground="#333",
        text="Browse",
        command=lambda: transfer_script_func.dest_dir(self),
    )
    self.dest_btn.grid(row=5, column=0, padx=(
        160, 0), pady=(10, 0), sticky=NSEW)
    self.dest_btn.grid_rowconfigure(0, weight=1)

    self.check_files_btn = tk.Button(
        self.master,
        highlightbackground="#333",
        text="Check Files",
        command=lambda: transfer_script_func.check_files(self),
    )
    self.check_files_btn.grid(row=6, column=0, padx=(
        160, 0), pady=(40, 0), sticky=NSEW)
    self.check_files_btn.grid_rowconfigure(0, weight=1)

if __name__ == "__main__":
    pass
