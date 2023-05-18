import tkinter as tk
import tkinter.font
from tkinter import messagebox
from tkinter import *
from world import generate_word, lista_gener_word,word_definition
from typing import List
import enchant

text=""" Your goal is to guess a word in 5 tries.
Please choose 5 letter word and press button.
The tile colors will guide you. 
green - correct letter at correct spot
yellow - corect letter at wrong spot
no change - letter not in this word
"""
global expression
expression = ''
#input_text = StringVar()


def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()

def create_playground(hieght:int,width:int,frame,font:str)->list:
    label = [0 for z in range(hieght * width)]
    for i in range(hieght):
        for j in range(width):
            label[hieght * i + j] = tk.Label(frame, relief='groove', anchor='center', bg='#90C6E5', fg='grey',
                                          text=' ', height=3, width=6, font=font)
            label[hieght * i + j].grid(column=j, row=i)
    return label

def get_letter_button(letter, list_letter,buttons):

    index = list_letter.index(letter.upper())
    button = buttons[index]
    return button

def press(num: str, entry) -> str:
    global expression
    input_text = StringVar()
    expression = expression + num
    input_text.set(expression)
    entry.config(text=expression)

    return expression



def create_buttons(hieght:int,width:int,frame,label):
    button = [0 for z in range(hieght * width)]
    alfabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(hieght):
        for j in range(width):
            letter=str(alfabet[width * i + j])
            button[width * i + j] = tk.Button(frame,text=letter,bg='#90C6E5', height=1, width=2,command=lambda letter=letter: press(letter,label))
            button[width * i + j].grid(column=j, row=i)
    return button


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Wordly')
        self.geometry('380x610')
        self.config(bg='#90C6E5')
        self.tries = 0
        self.title_font = tk.font.Font(family="Comic Sans MS", size=15, weight="bold")
        self.letter_font = tk.font.Font(family="Arial", size=12, weight="bold")
        self.frame0 = tk.Frame(self, bg='#90C6E5', height=50, width=28)
        self.frame0.grid_propagate()
        self.frame1 = tk.Frame(self, bg='#90C6E5', height=50, width=28)
        self.frame1.grid_propagate()
        self.frame2 = tk.Frame(self, bg='#90C6E5', height=50, width=28)
        self.frame2.grid_propagate()
        self.frame3 = tk.Frame(self, bg='red', height=50, width=28)
        self.frame3.grid_propagate()
        self.frame4 = tk.Frame(self, bg='red', height=50, width=28)
        self.frame4.grid_propagate()

        self.label20 = tk.Label(self.frame2,width=38,anchor='center',text='',bg='#90C6E5',fg='white',font=self.letter_font)
        self.text=tk.Label(self.frame0,text=text,anchor='center', bg='#90C6E5',fg='#606060',  height=8, width=34)
        self.frame0.grid(column=0, row=0)
        self.frame1.grid(column=0, row=1)
        self.frame2.grid(column=0, row=2)
        self.frame3.grid(column=0, row=3)
        self.frame4.grid(column=0, row=4)
        self.label20.grid(column=0, row=0)
        self.text.grid(column=0, row=1)
        self.alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        final_word = generate_word(5)
        #final_word="world"
        self.Label01=create_playground(5,5,self.frame1,self.letter_font)

        # global expression
        # expression=''
        input_text = StringVar()
        def clear(entry=self.label20):
            global expression
            expression = ""
            input_text.set("")
            entry.config(text="")

        buttons=create_buttons(2,13,self.frame3,self.label20)




        def click():
            final_list = lista_gener_word(final_word)
            d = enchant.Dict("en_US")
            expression = self.label20.cget("text")
            guess=expression
            while guess=='':
                tk.messagebox.showinfo(title=None, message="Choose a word")
                break
            while d.check(guess) is False:
                tk.messagebox.showinfo(title=None, message="Choose a real word")
                self.label20.config(text="")
                clear()
                break
            else:
                self.tries += 1
                if self.tries > 5:
                    if guess == final_word:
                        tk.messagebox.showinfo(title=None, message="You won.")
                        self.button1.config(state='disabled')
                    else:
                        tk.messagebox.showinfo(title=None, message=f"You used all tries. You loose. The word was: {final_word}")
                        self.button1.config(state='disabled')

                else:
                    lista = [letter for letter in guess]
                    if len(guess)==5:
                        for element in lista:
                            if element in final_list and lista.index(element)!=final_list.index(element):
                                get_letter_button(element,self.alfabet,buttons).config(background='#DFE590',fg='black')
                            elif element in final_list and lista.index(element)==final_list.index(element):
                                get_letter_button(element,self.alfabet,buttons).config(background='#98E590',fg='white')
                            else:
                                get_letter_button(element,self.alfabet,buttons).config(background='grey',fg='white')
                        for index in range(len(lista)):
                            if final_list[index]==lista[index]:
                                self.Label01[(index + (self.tries - 1) * 5)].config(text=lista[index],bg="#98E590",fg='black')
                                final_list[index]='_'
                            elif (lista[index] in final_list and final_list[index]!=lista[index]):
                                self.Label01[(index + (self.tries - 1) * 5)].config(text=lista[index], bg="#DFE590",fg='black')
                            else:
                                self.Label01[(index + (self.tries - 1) * 5)].config(text=lista[index])
                        if guess.upper()==final_word.upper():
                            tk.messagebox.showinfo(title=None, message="You won")
                            self.button_enter.config(state='disabled')
                        else:
                            pass
                    else:
                        tk.messagebox.showinfo(title=None, message="Your word must contain 5 letters")
                        self.tries-=1
                self.label20.config(text="")
                clear()

        self.button_enter = tk.Button(self.frame4, text="Enter", bg='#82C4EB', height=1, width=31, command=click)
        self.button_enter.grid(column=0, row=2)
        self.button_clear = tk.Button(self.frame4, text="Clear", bg='#82C4EB', height=1, width=31, command=clear)
        self.button_clear.grid(column=0, row=1)


        self.title = tk.Label(self.frame0, text="Welcome to Wordly", bg='#90C6E5', fg="#0A659A",font=self.title_font,width=19)
        self.message=tk.Message
        self.title.grid(column=0, row=0)



if __name__ == "__main__":
    app = App()
    app.mainloop()
