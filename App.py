import tkinter as tk
import tkinter.font
from tkinter import messagebox
from world import generate_word, lista_gener_word
from typing import List

text=""" Your goal is to guess a word in 5 tries.
Please write 5 letter word and press button.
The tile colors will guide you. 
green - correct letter at correct spot
yellow - corect letter at wrong spot
no change - letter not in this word
"""

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Wordly')
        self.geometry('240x445')
        self.config(bg='#90C6E5')
        self.tries = 0
        self.frame0 = tk.Frame(self, bg='#90C6E5', height=50, width=28)
        self.frame0.grid_propagate()
        self.frame1 = tk.Frame(self, bg='#90C6E5', height=50, width=28)
        self.frame1.grid_propagate()
        self.frame2 = tk.Frame(self, bg='#90C6E5', height=50, width=28)
        self.frame2.grid_propagate()
        self.entry = tk.Entry(self.frame2, width=38)
        self.text=tk.Label(self.frame0,text=text,anchor='center', bg='#90C6E5',fg='#606060',  height=8, width=34)
        self.frame0.grid(column=0, row=0)
        self.frame1.grid(column=0, row=1)
        self.frame2.grid(column=0, row=2)
        self.entry.grid(column=0, row=0)
        self.text.grid(column=0, row=1)
        self.title_font = tk.font.Font(family="Comic Sans MS", size=15, weight="bold")
        self.letter_font = tk.font.Font(family="Arial", size=12, weight="bold")
        final_word = generate_word(5)
        Label01 = [0 for z in range(25)]
        frames = []

        def clear_frame(frame):
            for widgets in frame.winfo_children():
                widgets.destroy()


        for i in range(5):
            for j in range(5):
                Label01[5 * i + j] = tk.Label(self.frame1,relief='groove',anchor='center', bg='#90C6E5',fg='grey',text=' ',  height=2, width=4,font=self.letter_font)
                Label01[5 * i + j].grid(column=j, row=i)
                frames.append(Label01[5 * i + j])


        def click():
            self.tries += 1
            final_list = lista_gener_word(final_word)
            guess = str(self.entry.get())
            if self.tries > 5:
                if guess == final_word:
                    tk.messagebox.showinfo(title=None, message="You won.")
                    self.button1.config(state='disabled')
                else:
                    tk.messagebox.showinfo(title=None, message=f"You used all tries. You loose. The word was: {final_word}")
                    self.button1.config(state='disabled')

            else:
                lista = []
                for letter in guess:
                    lista.append(letter)
                if len(guess)==5:
                    for index in range(len(lista)):
                        if final_list[index]==lista[index]:
                            Label01[(index + (self.tries - 1) * 5)].config(text=lista[index],bg="#98E590",fg='black')
                            final_list[index]='_'
                        elif (lista[index] in final_list and final_list[index]!=lista[index]):
                            Label01[(index + (self.tries - 1) * 5)].config(text=lista[index], bg="#DFE590",fg='black')
                        else:
                            Label01[(index + (self.tries - 1) * 5)].config(text=lista[index])
                    if guess==final_word:
                        tk.messagebox.showinfo(title=None, message="You won")
                        self.button1.config(state='disabled')
                    else:
                        pass
                else:
                    tk.messagebox.showinfo(title=None, message="Your word must contain 5 letters")
                    self.tries-=1
            self.entry.delete(0, 'end')


        self.button1 = tk.Button(self.frame2, text="Enter", bg='#82C4EB', height=2, width=31, command=click)
        self.button1.grid(column=0, row=1)


        self.title = tk.Label(self.frame0, text="Welcome to Wordly", bg='#90C6E5', fg="#0A659A",font=self.title_font,width=19)
        self.message=tk.Message
        self.title.grid(column=0, row=0)

        krok = 0


if __name__ == "__main__":
    app = App()
    app.mainloop()
