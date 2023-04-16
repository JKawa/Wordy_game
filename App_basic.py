import tkinter as tk
import tkinter.font
from tkinter import messagebox
from tkinter import *
from world import generate_word, lista_gener_word,word_definition
from typing import List
import enchant

text=""" Your goal is to guess a word in 5 tries.
Please write 5 letter word and press button.
The tile colors will guide you. 
green - correct letter at correct spot
yellow - corect letter at wrong spot
no change - letter not in this word
"""
global expression
expression = ''


def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()

def create_playground(hieght:int,width:int,frame,font:str):
    label = [0 for z in range(hieght * width)]
    #frames = []
    for i in range(hieght):
        for j in range(width):
            label[5 * i + j] = tk.Label(frame, relief='groove', anchor='center', bg='#90C6E5', fg='grey',
                                          text=' ', height=2, width=4, font=font)
            label[5 * i + j].grid(column=j, row=i)
            #frames.append(label[5 * i + j])
    return label

# def create_buttons(hieght:int,width:int,frame,entry):
#     button = [0 for z in range(hieght * width)]
#     alfabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#
#     def press(num: str) -> str:
#
#         input_text = StringVar()
#
#         global expression
#         expression = expression + num
#         input_text.set(expression)
#
#         return expression
#
#     for i in range(hieght):
#         for j in range(width):
#             button[13 * i + j] = tk.Button(frame,text=alfabet[13 * i + j], height=2, width=4,command=lambda: press(alfabet[13 * i + j]))
#             button[13 * i + j].grid(column=j, row=i)
#             print(expression)
#             entry.config(text=expression)
#     return expression


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Wordly')
        self.geometry('500x600')
        self.config(bg='#90C6E5')
        self.tries = 0
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
        self.entry = tk.Label(self.frame2,width=38,anchor='center',text='',bg='red',fg='white')
        self.text=tk.Label(self.frame0,text=text,anchor='center', bg='#90C6E5',fg='#606060',  height=8, width=34)
        self.frame0.grid(column=0, row=0)
        self.frame1.grid(column=0, row=1)
        self.frame2.grid(column=0, row=2)
        self.frame3.grid(column=0, row=3)
        self.frame4.grid(column=0, row=4)
        self.entry.grid(column=0, row=0)
        self.text.grid(column=0, row=1)
        self.title_font = tk.font.Font(family="Comic Sans MS", size=15, weight="bold")
        self.letter_font = tk.font.Font(family="Arial", size=12, weight="bold")
        final_word = generate_word(5)
        self.Label01=create_playground(5,5,self.frame1,self.letter_font)

        #global expression
        #expression=''
        input_text = StringVar()
        def press(num:str,entry=self.entry)->str:

            global expression
            expression = expression + num
            input_text.set(expression)
            entry.config(text=expression)

            return expression



        B_A=tk.Button(self.frame3, text="A", bg='RED', height=1, width=2, command=lambda: press('a'))
        B_A.grid(column=1, row=0)
        B_B = tk.Button(self.frame3, text="B", bg='RED', height=1, width=2, command=lambda: press('b'))
        B_B.grid(column=2, row=0)
        B_C = tk.Button(self.frame3, text="C", bg='RED', height=1, width=2, command=lambda: press('c'))
        B_C.grid(column=3, row=0)
        B_D = tk.Button(self.frame3, text="D", bg='RED', height=1, width=2, command=lambda: press('d'))
        B_D.grid(column=4, row=0)
        B_E = tk.Button(self.frame3, text="E", bg='RED', height=1, width=2, command=lambda: press('e'))
        B_E.grid(column=5, row=0)
        B_F = tk.Button(self.frame3, text="F", bg='RED', height=1, width=2, command=lambda: press('f'))
        B_F.grid(column=6, row=0)
        B_G = tk.Button(self.frame3, text="G", bg='RED', height=1, width=2, command=lambda: press('g'))
        B_G.grid(column=7, row=0)
        B_H = tk.Button(self.frame3, text="H", bg='RED', height=1, width=2, command=lambda: press('h'))
        B_H.grid(column=8, row=0)
        B_I = tk.Button(self.frame3, text="I", bg='RED', height=1, width=2, command=lambda: press('i'))
        B_I.grid(column=0, row=1)
        B_J = tk.Button(self.frame3, text="J", bg='RED', height=1, width=2, command=lambda: press('j'))
        B_J.grid(column=1, row=1)
        B_K = tk.Button(self.frame3, text="K", bg='RED', height=1, width=2, command=lambda: press('k'))
        B_K.grid(column=2, row=1)
        B_L = tk.Button(self.frame3, text="L", bg='RED', height=1, width=2, command=lambda: press('l'))
        B_L.grid(column=3, row=1)
        B_M = tk.Button(self.frame3, text="M", bg='RED', height=1, width=2, command=lambda: press('m'))
        B_M.grid(column=4, row=1)
        B_N = tk.Button(self.frame3, text="N", bg='RED', height=1, width=2, command=lambda: press('n'))
        B_N.grid(column=5, row=1)
        B_O = tk.Button(self.frame3, text="O", bg='RED', height=1, width=2, command=lambda: press('o'))
        B_O.grid(column=6, row=1)
        B_P = tk.Button(self.frame3, text="P", bg='RED', height=1, width=2, command=lambda: press('p'))
        B_P.grid(column=7, row=1)
        B_Q = tk.Button(self.frame3, text="Q", bg='RED', height=1, width=2, command=lambda: press('q'))
        B_Q.grid(column=8, row=1)
        B_R = tk.Button(self.frame3, text="R", bg='RED', height=1, width=2, command=lambda: press('r'))
        B_R.grid(column=9, row=1)
        B_S = tk.Button(self.frame3, text="S", bg='RED', height=1, width=2, command=lambda: press('r'))
        B_S.grid(column=1, row=2)
        B_T = tk.Button(self.frame3, text="T", bg='RED', height=1, width=2, command=lambda: press('t'))
        B_T.grid(column=2, row=2)
        B_U = tk.Button(self.frame3, text="U", bg='RED', height=1, width=2, command=lambda: press('u'))
        B_U.grid(column=3, row=2)
        B_V = tk.Button(self.frame3, text="V", bg='RED', height=1, width=2, command=lambda: press('v'))
        B_V.grid(column=4, row=2)
        B_W = tk.Button(self.frame3, text="W", bg='RED', height=1, width=2, command=lambda: press('w'))
        B_W.grid(column=5, row=2)
        B_X = tk.Button(self.frame3, text="X", bg='RED', height=1, width=2, command=lambda: press('x'))
        B_X.grid(column=6, row=2)
        B_Y = tk.Button(self.frame3, text="Y", bg='RED', height=1, width=2, command=lambda: press('y'))
        B_Y.grid(column=7, row=2)
        B_Z = tk.Button(self.frame3, text="Z", bg='RED', height=1, width=2, command=lambda: press('z'))
        B_Z.grid(column=8, row=2)

        list_buttons=['B_A','B_B','B_C','B_D','B_E','B_F','B_G','B_H','B_I','B_J','B_K','B_L','B_M','B_N','B_O','B_P','B_Q','B_R','B_S','B_T','B_U','B_V','B_W','B_X','B_Y','B_Z']
        alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']


        def click():
            final_list = lista_gener_word(final_word)
            #x=0
            d = enchant.Dict("en_US")
            guess=expression
            #guess = str(self.entry.get())
            while d.check(guess) is False:
                tk.messagebox.showinfo(title=None, message="Choose a real word")
                self.entry.delete(0, END)
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
                        for index in range(len(lista)):
                            if final_list[index]==lista[index]:
                                self.Label01[(index + (self.tries - 1) * 5)].config(text=lista[index],bg="#98E590",fg='black')
                                final_list[index]='_'
                            elif (lista[index] in final_list and final_list[index]!=lista[index]):
                                self.Label01[(index + (self.tries - 1) * 5)].config(text=lista[index], bg="#DFE590",fg='black')
                            else:
                                self.Label01[(index + (self.tries - 1) * 5)].config(text=lista[index])
                        if guess==final_word:
                            tk.messagebox.showinfo(title=None, message="You won")
                            self.button1.config(state='disabled')
                        else:
                            pass
                    else:
                        tk.messagebox.showinfo(title=None, message="Your word must contain 5 letters")
                        self.tries-=1
                self.entry.delete(0, 'end')
                print("expression",expression)


        self.button1 = tk.Button(self.frame4, text="Enter", bg='#82C4EB', height=2, width=31, command=click)
        self.button1.grid(column=0, row=1)


        self.title = tk.Label(self.frame0, text="Welcome to Wordly", bg='#90C6E5', fg="#0A659A",font=self.title_font,width=19)
        self.message=tk.Message
        self.title.grid(column=0, row=0)



if __name__ == "__main__":
    app = App()
    app.mainloop()
