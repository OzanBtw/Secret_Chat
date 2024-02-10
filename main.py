from tkinter import *
import codeMain as c
from os import urandom
from binascii import hexlify

"""         Welcome to secret message.exe
            Use English KEYBOARD
                            -OzanBtw
"""


seed = "0x00000000"

#function Setup
def set_seed():
    global seed
    s = Seed.get()
    if " " in s:
        pass
    elif "" == s:
        pass
    else:
        seed = s

def generateSeed():
    global seed
    new = "0x" + hexlify(urandom(4)).decode()
    Seed.delete(0,END)
    Seed.insert(0, new)
    seed = new

def encode():
    text = Encode0.get()
    final = c.encode(text, seed)

    Encode1.delete(0, END)
    Encode1.insert(0, final)

def decode():
    text = Decode0.get()
    final = c.decode(text,seed)

    Decode1.delete(0, END)
    Decode1.insert(0, final)

large_font = ('Verdana',20)

#Window Setup
window = Tk()
window.geometry("1160x240")
window.title("Secret Chat")
icon = PhotoImage(file='/Users/ozandora/Desktop/Dosya/Codes/Odev/023 - Secret Chat/logo.png')
window.iconphoto(True, icon)

#Title & Texts
title = Label(window, text="Welcome to the Secret Chat",font=('Verdana',25,'bold'),fg='#00FF00').grid(row=0,column=1)
text1 = Label(window, text="Seed",font=large_font).grid(row=1,column=0)
text2 = Label(window, text="Encoder",font=large_font).grid(row=2,column=0)
text3 = Label(window, text="Decoder",font=large_font).grid(row=3,column=0)
text4 = Label(window, text="by OzanBtw",font=(('Comic Sans MS',15,'italic'))).grid(row=0,column=3)

#Inputs
Seed = Entry(window, width=30,font=large_font)
Encode0 = Entry(window, width=30,font=large_font)
Decode0 = Entry(window, width=30,font=large_font)
Encode1 = Entry(window, width=30,font=large_font)
Decode1 = Entry(window, width=30,font=large_font)

Seed.insert(0,f"{seed}")
Encode0.insert(0,"Enter a message to encode.")
Decode0.insert(0,"Enter a coded message to decode.")
Encode1.insert(0,"")
Decode1.insert(0,"")


Seed.grid(row=1,column=1)
Encode0.grid(row=2,column=1)
Decode0.grid(row=3,column=1)
Encode1.grid(row=2,column=2)
Decode1.grid(row=3,column=2)


#Buttons

seedButton = Button(window, text="Set Seed" ,command=set_seed,width=15,height=1,font=large_font)
generateButton = Button(window, text="Generate", command=generateSeed,width=15,height=1,font=large_font)
encodeButton = Button(window, text="Translate" ,command=lambda: encode(),width=15,height=1,font=large_font)
decodeButton = Button(window, text="Translate" ,command=lambda: decode(),width=15,height=1,font=large_font)

seedButton.grid(row=1,column=2)
generateButton.grid(row=1,column=3)
encodeButton.grid(row=2,column=3)
decodeButton.grid(row=3,column=3)

#     ===START===
window.resizable(width=False, height=False)
window.mainloop()