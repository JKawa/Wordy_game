import tkinter as tk
import tkinter.font
from tkinter import messagebox
from world import generate_word, lista_gener_word, word_definition
from typing import List

#to do deactivate radio button after use

text=""" Your goal is to guess a word in 5 tries.
Please write word and press button.
The tile colors will guide you. 
green - correct letter at correct spot
yellow - corect letter at wrong spot
no change - letter not in this word
"""
class NewWindow():

    def __init__(self, word, message):
        self.window = tk.Tk()
        self.won_loose_font=tk.font.Font(family="Comic Sans MS", size=15, weight="bold")
        self.message_font=tk.font.Font(family="Arial", size=12, weight="bold")
        self.window.config(bg='#90C6E5')
        self.window.title(message)
        self.mes = tk.Label(self.window, text=message,font=self.won_loose_font, fg='#606060',bg='#90C6E5')
        self.mes.grid(column=0,row=0)
        self.word = tk.Label(self.window, text=word_definition(word), fg='#606060',bg='#90C6E5',font=self.message_font)
        self.word .grid(column=0,row=1)
        self.window.mainloop()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Wordly')
        self.resizable(height = '240', width = '445')
        self.config(bg='#90C6E5')
        self.tries = 0
        self.frame0 = tk.Frame(self, bg='#90C6E5', height=50, width=28)
        self.frame0.grid_propagate()
        self.frame1 = tk.Frame(self, bg='#90C6E5', height=50, width=28)
        self.frame1.grid_propagate()
        self.frame2 = tk.Frame(self, bg='#90C6E5', height=50, width=28)
        self.frame2.grid_propagate()
        self.frame01=tk.Frame(self.frame0, bg='#90C6E5', height=50, width=28)
        self.frame011 = tk.Frame(self.frame01, bg='#90C6E5', height=50, width=30)
        self.frame2.grid_propagate()
        self.entry = tk.Entry(self.frame2, width=38)
        self.text=tk.Label(self.frame0,text=text,anchor='center', bg='#90C6E5',fg='#606060',  height=8, width=34)
        self.frame0.grid(column=0, row=0)
        self.frame1.grid(column=0, row=1)
        self.frame2.grid(column=0, row=2)
        self.frame01.grid(column=0, row=3)
        self.frame011.grid(column=0, row=1)
        self.entry.grid(column=0, row=0)
        self.text.grid(column=0, row=1)
        self.title_font = tk.font.Font(family="Comic Sans MS", size=15, weight="bold")
        self.letter_font = tk.font.Font(family="Arial", size=12, weight="bold")
        self.message_font=tk.font.Font(family="Arial", size=10, weight="bold")
        self.choose_text=tk.Label(self.frame01, text="Choose number of letters", bg='#90C6E5', fg="#0A659A",width=19, font=self.message_font)
        var=tk.IntVar()
        self.radio5=tk.Radiobutton(self.frame011, text="5",variable=var, value=5)
        self.radio5.grid(column=0, row=0)
        self.radio6=tk.Radiobutton(self.frame011, text="6",variable=var, value=6)
        self.radio6.grid(column=1, row=0)
        self.radio7=tk.Radiobutton(self.frame011, text="7",variable=var, value=7)
        self.radio7.grid(column=2, row=0)
        self.choose_text.grid(column=0, row=0)
        self.word = ""
        self.word_length = 0



        Label01 = [0 for z in range(50)]
        frames = []

        def clear_frame(frame):
            for widgets in frame.winfo_children():
                widgets.destroy()

        def click2():
            clear_frame(self.frame1)
            n = var.get()
            final_word = generate_word(n)
            for i in range(5):
                for j in range(n):
                    Label01[n * i + j] = tk.Label(self.frame1,relief='groove',anchor='center', bg='#90C6E5',fg='grey',text=' ',  height=2, width=4,font=self.letter_font)
                    Label01[n * i + j].grid(column=j, row=i)
                    frames.append(Label01[n * i + j])
            self.button1.config(state='active', bg='#82C4EB',activebackground='#82C4EB')
            self.word = final_word
            self.word_length = n
            self.tries=0

        def click():
            n=self.word_length
            final_word=self.word
            self.tries += 1
            final_list = lista_gener_word(final_word)
            guess = str(self.entry.get())
            if self.tries > 5:
                if guess.lower() == final_word.lower():
                    self.button1.config(state='disabled')
                    message="You won"
                    NewWindow(final_word, message)
                else:
                    self.button1.config(state='disabled')
                    message=f"You used all tries. You loose. The word was: {final_word}"
                    NewWindow(final_word, message)
            else:
                lista = []
                for letter in guess:
                    lista.append(letter)
                if len(guess)==n:
                    for index in range(len(lista)):
                        if final_list[index]==lista[index]:
                            Label01[(index + (self.tries - 1) * n)].config(text=lista[index],bg="#98E590",fg='black')
                            final_list[index]='_'
                        elif (lista[index] in final_list and final_list[index]!=lista[index]):
                            Label01[(index + (self.tries - 1) * n)].config(text=lista[index], bg="#DFE590",fg='black')
                        else:
                            Label01[(index + (self.tries - 1) * n)].config(text=lista[index])
                    if guess.lower()==final_word.lower():
                        self.button1.config(state="disabled")
                        message = "You won"
                        NewWindow(final_word, message)
                    else:
                        pass
                else:
                    tk.messagebox.showinfo(title=None, message=f"Your word must contain {n} letters")
                    self.tries-=1
            self.entry.delete(0, 'end')

        self.button0 = tk.Button(self.frame01, text="OK", bg='#82C4EB', height=1, width=13,command=click2)
        self.button0.grid(column=0, row=2)
        self.button1 = tk.Button(self.frame2, text="Enter", bg='#82C4EB',state='disabled', height=2, width=31, command=click)
        self.button1.grid(column=0, row=1)
        self.title = tk.Label(self.frame0, text="Welcome to Wordly", bg='#90C6E5', fg="#0A659A",font=self.title_font,width=19)
        self.title.grid(column=0, row=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()
