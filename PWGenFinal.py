#Joseph Dirik
#Special Topics and Programming Project


from tkinter import *
from tkinter import ttk, messagebox
from random import *
from string import *

class PasswordGen:
    def password(self):

        d1 = choice(ascii_letters + digits) #these just make a random character being either a lett or number
        d2 = choice(ascii_letters + digits)
        d3 = choice(ascii_letters + digits)
        d4 = choice(ascii_letters + digits)
        ds1= choice(ascii_letters + digits + punctuation) #these just add the option of special characcter

        ds2= choice(ascii_letters + digits + punctuation)
        ds3= choice(ascii_letters + digits + punctuation)
        ds4= choice(ascii_letters + digits + punctuation)


        if self.length.get().isdigit() and int(self.length.get()) in range(5, 21):
            notSpecial = d1 + d2 + d3 + d4
            special = ds1 + ds2 + ds3 + ds4

            count = 4

            while count < int(self.length.get()):
                x = choice(ascii_uppercase + ascii_lowercase + digits)
                y = choice(ascii_uppercase + ascii_lowercase + digits + punctuation)

                special += y
                notSpecial += x
                count += 1
            if self.var.get():
                self.gen.set(special)
            else:
                self.gen.set(notSpecial)
        elif self.length.get().isdigit():
            messagebox.showerror(message="Length should be in the range of 5 to 20")
        else:
            messagebox.showwarning(message="Please input a number")


    def __init__(self):
        obj = Tk()
        obj.title("Password self.generator")
        obj.resizable(width=False, height=False)


        frame = ttk.Frame(obj)
        frame.grid()
        frame.rowconfigure(0)
        frame.columnconfigure(0)

        self.length = StringVar()
        self.gen = StringVar()
        self.var = IntVar()

        len_entry = ttk.Entry(frame, textvariable=self.length)
        len_entry.config(font=("arial", "15", "bold"), foreground="Black")  # Change Fonts
        len_entry.grid(row=1, column=2)

        label = ttk.Label(frame, text="Enter Length ", relief="flat")
        label.config(font=("verdana", "11", "bold"), foreground="green", background="black")
        label.grid(row=1, column=1)

        label1 = ttk.Label(frame, textvariable=self.gen, wraplength="6.5c", relief="flat", state = 'readonly')
        label1.config(font=("verdana", "12", "italic"), foreground="black")
        label1.grid(row=3, column=2, sticky=W)
        label1.config(state = 'readonly')

        checkbutton = ttk.Checkbutton(frame, text="Special Characters?", variable=self.var)
        checkbutton.grid(row=2, column=1)

        button = ttk.Button(frame, text="generate", command=self.password, width=20)
        button.grid(row=2, column=2, sticky="W")

        button1 = ttk.Button(frame, text="Exit", width=10, command=obj.destroy)
        button1.grid(row=2, column=2, sticky="E")

        for child in frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

        len_entry.focus()
        obj.bind("<Return>", self.password)
        obj.mainloop()

mainwindow = PasswordGen()
