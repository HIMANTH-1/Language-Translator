from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox



root = tk.Tk()
root.title("Language Translator")
root.geometry("590x370")
frame1 = Frame(root, width=590, height=370, relief=RIDGE, borderwidth=5, bg='lightgreen')
frame1.place(x=0, y=0)

text_1 = Text(frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=('Verdana', 15))
text_1.place(x=10, y=100)

Label(root, text="           Enter the text", font=("Helvica 15 bold"), fg="black", bg="lightgreen").place(x=15,y=60)


l = tk.StringVar()
choose_lang = ttk.Combobox(frame1, width=27, textvariable=l, state='readonly', font=('verdana', 10, 'bold'))
choose_lang['values'] = ('English', 'Hindi', 'Telugu', 'Tamil', 'Malayalam', 'Punjabi', 'Sanskrit', 'Marathi',
                          'Kannada', 'Bengali', 'Gujarati', 'Urdu')
choose_lang.place(x=305, y=60)
choose_lang.current(0)

Label(root, text="Translator", font=("Helvica 20 bold"), fg="black", bg="lightgreen").pack(pady=10)

text_2 = Text(frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=('Verdana', 15))
text_2.place(x=300, y=100)


def Translate():
    input_text = text_1.get("1.0", "end-1c")
    target_lang = choose_lang.get()

    if input_text.strip() == '':
        messagebox.showerror("Wrong Input", "Please enter text to translate.")
        return
    translator = Translator()
    translation = translator.translate(input_text, dest=target_lang)
    translated_text = translation.text
    text_2.delete(1.0, 'end')
    text_2.insert("end", translated_text)
    
def clear():
    text_1.delete(1.0, "end")
    text_2.delete(1.0, "end")


button1 = Button(frame1, text="Translate", borderwidth=5, relief=RIDGE, font=('Verdana', 10, 'bold'),
                 bg='#248aa2', fg='white', cursor='hand2', command=Translate)
button1.place(x=185, y=300)

button2 = Button(frame1, text="Clear", borderwidth=5, relief=RIDGE, font=('Verdana', 10, 'bold'),
                 bg='#248aa2', fg='white', cursor='hand2', command=clear)
button2.place(x=300, y=300)

root.mainloop()
