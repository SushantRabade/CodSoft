# Random Password Generator!

from tkinter import *
from random import randint

root = Tk()
root.title("Password Generator!")
root.geometry("500x300")
my_password = chr(randint(33, 126))


# Generate random strong password
def new_rand():
    # Clear our entry box
    pw_entry.delete(0, END)

    # Get pw length and convert to int
    pw_length = int(my_entry.get())

    # Create a variable to hold password
    my_pass = ''

    # loop through pass length
    for x in range(pw_length):
        my_pass += chr(randint(33, 126))

    # Output password to the screen
    pw_entry.insert(0, my_pass)


# Copy to clipboard
def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())


# Label Frame
lf = LabelFrame(root, text="How many Characters? ")
lf.pack(pady=20)

# Create entry box
my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

# Create entry box return password
pw_entry = Entry(root, font=("Helvetica", 24))
pw_entry.pack(pady=20)

# Create frame of button
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create a buttons
my_btn = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_btn.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy", command=clipper)
clip_button.grid(row=0, column=1, padx=10)
root.mainloop()