# Information Of header in Hypertexts
import subprocess
def open_file(event):
    file_path = r'C:\Users\LENOVO\Downloads\python.txt'
    subprocess.run(['start', file_path], shell=True)

import tkinter as tk
root = tk.Tk()
button = tk.Button(root, text="click", command=lambda: open_file(None))
button.pack()
root.mainloop()
