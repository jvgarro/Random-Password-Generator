from tkinter import *
from tkinter import ttk
import random

from numpy import delete

def main():
    global passForm, root
    root = Tk()
    root.title("Random Password Generator")
    root.geometry("720x480")
    root.resizable(False, False)
    title = ttk.Label(root, text="Random Password Generator!", font=('Arial', 20))
    title.grid(row=0, column=0, columnspan=3, padx=180, pady=20)
    generatePassButton = ttk.Button(root, text="Generate Password", command=generatePass)
    generatePassButton.grid(row=1, column=0, columnspan=3, padx=180, pady=20)
    
    passForm = ttk.Entry(root, width=50)
    passForm.grid(row=2, column=0, columnspan=3, padx=180, pady=20)
    
    copyButton = ttk.Button(root, text="Copy Password", command=copyPassword)
    copyButton.grid(row=3, column=0, columnspan=3, padx=180, pady=20)
    
    
    root.mainloop()

def generatePass():
    passForm.delete(0, END)
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "[]{}()*;/,_"
    all = lower + upper + numbers + symbols
    lenght = 16
    password = "".join(random.sample(all, lenght))
    print(password)
    passForm.insert(0, password)
    return password

def copyPassword():
    root.clipboard_append(passForm.get())
    
    
if __name__ == "__main__":
    main()
    
    
    
    

