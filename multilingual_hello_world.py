# multilingual_hello_world.py
# this is a copy of multilingual_hello_world_tk.py (local),
# linking it to GitHub

import tkinter as tk


class MyGUI:

    def __init__(self):
                    
        self.root = tk.Tk()

        self.root.geometry("250x100")
        self.root.title("Multilingual Hello World")

        self.label = tk.Label(self.root, text="What's that you say?")
        self.label.pack(padx=20, pady=20)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)

        self.btn1 = tk.Button(self.buttonframe, text="French", command=self.print_french)
        self.btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.btn2 = tk.Button(self.buttonframe, text="German", command=self.print_german)
        self.btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.btn3 = tk.Button(self.buttonframe, text="English", command=self.print_english)
        self.btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

        self.buttonframe.pack() # fill='x' as perameter changes layout


        self.root.mainloop()

    def print_french(self):
        self.label.config(text="Bonjour, le monde!")
        #label.pack(padx=20, pady=20)
        # print ("Bonjour, le monde!")

    def print_german(self):
        self.label.config(text="Hallo, welt!")
        # print ("Hallo, welt!")

    def print_english(self):
        self.label.config(text="Hello, world!")
        # print ("Hello, world!")

MyGUI()

# musical inspiration: Dobby Dobson, Carry That Weight
# test line, see if this shows up in local version in VS Code
