from cProfile import label
from dis import Instruction
from lib2to3.pgen2.pgen import generate_grammar
import string
from tkinter import *

app = Tk()


Instructions = Label(app, text="Type in your message below and I will encode it for you.")
Instructions.pack()

e = Entry(app, width=50)
e.pack()




e.insert(0, "Type Here...")

def encoder():

    alphabet = list(string.ascii_letters)
    alphabet.append(" ")

    # this gives the index of the user input based on the position in the alphabet
    code_index_in_alp_list = []
    for j in e.get():
        for i in alphabet:
            if i == j:
                code_index_in_alp_list.append(alphabet.index(i))

    # this created an encoded list of the user input
    encoded_list = []
    for i in code_index_in_alp_list:
        if i < 20:
            new_index = i  + 5
        elif i == len(alphabet)-1:
            new_index = len(alphabet)-1
        else: 
            new_index = i - 5
        encoded_list.append(alphabet[new_index])

    #this changes encoded list into string format
    user_encoded = "".join(encoded_list)

    encoded = Label(app, text=f"Your Encoded message is\n {user_encoded}")
    encoded.pack()





generate_button = Button(app, text="Generate", padx=50, pady=50, command=encoder)
generate_button.pack()
app.mainloop()

