#Importing required Libraries
from tkinter import *
from PIL import Image, ImageDraw, ImageFont
import textwrap
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring

def convert():

    # Create a new blank image
    image = Image.new('RGB', (800, 600), color='white')

    # Define a font for the handwriting
    font = ImageFont.truetype(f'Font/{fonted}', 20)

    # Define the text to be converted to handwriting
    text = f'{paragraph.get()}'

    # Create a draw object for the image
    draw = ImageDraw.Draw(image)

    # Wrap the text and draw it on the image
    lines = textwrap.wrap(text, width=60)
    y_text = 10
    for line in lines:
        _, _, width, height = draw.textbbox((50, y_text), line, font=font)
        draw.text((50, y_text), line, font=font, fill='blue')
        y_text = height

    # Save the image
    image.save(f'{imgname}.png')
    im = Image.open(f'{imgname}.png')
    im.show() 
    # root.destroy()

    print('***END***')
    print(fonted)

#Asking for the file name
def fileName():
    name = askstring('fileName', 'Rename the Image') 
    if name:
        global imgname
        imgname=name
        showinfo('fileName', f'File renamed as {name}')
        convert()

    elif name is None:
        print('no name')
        
    else:
        showinfo('fileName', 'Please enter a Valid filName')
    
def kristan():
    global fonted
    fonted='ITCKRIST.ttf'
    foname= 'Kristan-ITC'
    showinfo('Font', f'Font changed to {foname}')

def handwrid():
    global fonted
    fonted='HANDWRID.TTF'
    foname= 'Dakota-Handwriting'
    showinfo('Font', f'Font changed to {foname}')

def faculty():
    global fonted
    fonted='wr.otf'
    foname= 'Faculty'
    showinfo('Font', f'Font changed to {foname}')

def lucida():
    global fonted
    fonted='lucidaBold.TTF'
    foname= 'Lucida Bold'
    showinfo('Font', f'Font changed to {foname}')

def noteworthy():
    global fonted
    fonted='Noteworthy-Lt.ttf'
    foname= 'Noteworthy'
    showinfo('Font', f'Font changed to {foname}')    

def marker():
    global fonted
    fonted='Marker Felt.ttf'
    foname= 'Marker Felt'
    showinfo('Font', f'Font changed to {foname}')

def viner():
    global fonted
    fonted='VINERITC.TTF'
    foname= 'Viner-ITC'
    showinfo('Font', f'Font changed to {foname}')

def segoe():
    global fonted
    fonted='segoesc.ttf'
    foname= 'Segoe Script'
    showinfo('Font', f'Font changed to {foname}')

def about():
    showinfo('About','''This is a Simple Text to Handwriting Converter APP.

It takes Text as an Input and gives a PNG file of the Text which is converted into Handwriting as an output.
    ''')

root = Tk()
root.title()

root.geometry("733x434")
root.minsize(250 , 300)
root.configure(background='grey')


mainMenu = Menu(root)

subMenu = Menu(mainMenu, tearoff=0)
subMenu.add_command(label='Dakota(Default)',command=handwrid)
subMenu.add_command(label='Segoe Script',command=segoe)
subMenu.add_command(label='Kristan-ITC',command=kristan)
subMenu.add_command(label='Marker Felt',command=marker)
subMenu.add_command(label='Faculty',command=faculty)
subMenu.add_command(label='Noteworthy',command=noteworthy)
subMenu.add_command(label='Viner-ITC',command=viner)
subMenu.add_command(label='Lucida Bold',command=lucida)
root.config(menu = mainMenu)
mainMenu.add_cascade(label='Fonts', menu=subMenu)

subMenu2 = Menu(mainMenu , tearoff=0)
subMenu2.add_command(label='About', command=about)
root.config(menu = mainMenu)
mainMenu.add_cascade(label='Help', menu=subMenu2)


title = Label(root, text="Text to HandWriting Converter", font="comicsansm 19 bold" , pady=15, padx=15,bg='grey')
title.pack()


para=Label(root, text='Text-Content',font="comicsansms 15",bg='grey')
para.pack(pady=5)

paragraph= StringVar()

paragraphcon =Entry(root, textvariable=paragraph,width=50)
paragraphcon.insert(0, '''Python is a high-level, interpreted programming language. It was first released in 1991 by Guido van Rossum and has since become one of the most popular programming languages in the world. Python is designed to be easy to read and write, with a simple syntax and a focus on code readability.''')
paragraphcon.pack(ipady=20)
fonted = 'HANDWRID.TTF'

Button(text='Convert',command=fileName).pack(pady=5)

root.mainloop()