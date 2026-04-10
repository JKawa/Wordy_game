import tkinter as tk
import tkinter.font
import tkinter.messagebox
from tkinter import *
from world import generate_word, lista_gener_word
import enchant

text = """ Your goal is to guess a word in 5 tries.
Please choose 5 letter word and press button.
The tile colors will guide you. 
green - correct letter at correct spot
yellow - corect letter at wrong spot
no change - letter not in this word
"""
global expression
expression = ""
# input_text = StringVar()


def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()


def create_playground(hieght: int, width: int, frame, font: str) -> list:
    label = [0 for z in range(hieght * width)]
    for i in range(hieght):
        for j in range(width):
            label[hieght * i + j] = tk.Label(
                frame,
                relief="groove",
                anchor="center",
                bg="#90C6E5",
                fg="grey",
                text=" ",
                height=3,
                width=6,
                font=font,
            )
            label[hieght * i + j].grid(column=j, row=i)
    return label


def get_letter_button(letter, list_letter, buttons):
    index = list_letter.index(letter.upper())
    button = buttons[index]
    return button


def press(num: str, entry):
    entry.insert(tk.END, num)


def create_buttons(hieght: int, width: int, frame, entry, alfabet):
    button = [0 for z in range(hieght * width)]
    for i in range(hieght):
        for j in range(width):
            letter = str(alfabet[width * i + j])
            button[width * i + j] = tk.Button(
                frame,
                text=letter,
                bg="#90C6E5",
                height=1,
                width=2,
                command=lambda letter=letter: press(letter, entry),
            )
            button[width * i + j].grid(column=j, row=i)
    return button


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Wordly")
        self.geometry("570x650")
        self.config(bg="#90C6E5")
        self.tries = 0
        self.title_font = tk.font.Font(family="Comic Sans MS", size=15, weight="bold")
        self.letter_font = tk.font.Font(family="Arial", size=12, weight="bold")
        self.frame0 = tk.Frame(self, bg="#90C6E5", height=50, width=28)
        self.frame0.grid_propagate()
        self.frame1 = tk.Frame(self, bg="#90C6E5", height=50, width=28)
        self.frame1.grid_propagate()
        self.frame2 = tk.Frame(self, bg="#90C6E5", height=50, width=28)
        self.frame2.grid_propagate()
        self.frame3 = tk.Frame(self, bg="red", height=50, width=28)
        self.frame3.grid_propagate()
        self.frame4 = tk.Frame(self, bg="red", height=50, width=28)
        self.frame4.grid_propagate()

        self.input_text = tk.Entry(
            self.frame2,
            width=38,
            justify="center",
            bg="#B8CAD4",
            fg="black",
            font=self.letter_font,
        )

        def to_uppercase(event):
            text = self.input_text.get().upper()
            self.input_text.delete(0, tk.END)
            self.input_text.insert(0, text)

        self.input_text.bind("<KeyRelease>", to_uppercase)
        self.text = tk.Label(
            self.frame0,
            text=text,
            anchor="center",
            bg="#90C6E5",
            fg="#606060",
            height=8,
            width=34,
        )
        self.frame0.grid(column=0, row=0)
        self.frame1.grid(column=0, row=1)
        self.frame2.grid(column=0, row=2)
        self.frame3.grid(column=0, row=3)
        self.frame4.grid(column=0, row=4)
        self.input_text.grid(column=0, row=0)
        self.text.grid(column=0, row=1)
        self.alfabet = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]
        self.word_list = []
        final_word = generate_word(5)
        # final_word="world"
        self.Label01 = create_playground(5, 5, self.frame1, self.letter_font)

        def clear():
            global expression
            expression = ""
            self.input_text.delete(0, tk.END)

        buttons = create_buttons(
            2, 13, self.frame3, self.input_text, alfabet=self.alfabet
        )

        def change_colors(element, background: str, text_color: str):
            get_letter_button(element, self.alfabet, buttons).config(
                background=background, fg=text_color
            )

        def click():
            final_list = lista_gener_word(final_word)
            d = enchant.Dict("en_US")
            guess = self.input_text.get()
            while guess == "":
                tk.messagebox.showinfo(title=None, message="Choose a word")
                break
            while d.check(guess) is False:
                tk.messagebox.showinfo(title=None, message="Choose a real word")
                self.input_text.config(text="")
                clear()
                break
            else:
                self.tries += 1
                if self.tries > 5:
                    if guess == final_word:
                        tk.messagebox.showinfo(title=None, message="You won.")
                        self.button_enter.config(state="disabled")
                    else:
                        tk.messagebox.showinfo(
                            title=None,
                            message=f"You used all tries. You loose. The word was: {final_word}",
                        )
                        self.button_enter.config(state="disabled")

                else:
                    lista = [letter for letter in guess]
                    if len(guess) == 5 and guess not in self.word_list:
                        self.word_list.append(guess)
                        print(self.word_list)
                        for element in lista:
                            if element in final_list and lista.index(
                                element
                            ) != final_list.index(element):
                                change_colors(
                                    element, background="#DFE590", text_color="black"
                                )
                            elif element in final_list and lista.index(
                                element
                            ) == final_list.index(element):
                                change_colors(
                                    element, background="#98E590", text_color="black"
                                )
                            else:
                                change_colors(
                                    element, background="grey", text_color="white"
                                )
                        for index in range(len(lista)):
                            if final_list[index] == lista[index]:
                                self.Label01[(index + (self.tries - 1) * 5)].config(
                                    text=lista[index], bg="#98E590", fg="black"
                                )
                                final_list[index] = "_"
                            elif (
                                lista[index] in final_list
                                and final_list[index] != lista[index]
                            ):
                                self.Label01[(index + (self.tries - 1) * 5)].config(
                                    text=lista[index], bg="#DFE590", fg="black"
                                )
                            else:
                                self.Label01[(index + (self.tries - 1) * 5)].config(
                                    text=lista[index]
                                )
                        if guess.upper() == final_word.upper():
                            tk.messagebox.showinfo(title=None, message="You won")
                            self.button_enter.config(state="disabled")
                        else:
                            pass
                    elif guess in self.word_list:
                        tk.messagebox.showinfo(
                            title=None, message="You have already used this word"
                        )
                        self.tries -= 1
                    else:
                        tk.messagebox.showinfo(
                            title=None, message="Your word must contain 5 letters"
                        )
                        self.tries -= 1
                self.input_text.config(text="")
                clear()

        self.button_enter = tk.Button(
            self.frame4, text="Enter", bg="#82C4EB", height=1, width=31, command=click
        )
        self.button_enter.grid(column=0, row=2)
        self.button_clear = tk.Button(
            self.frame4, text="Clear", bg="#82C4EB", height=1, width=31, command=clear
        )
        self.button_clear.grid(column=0, row=1)

        self.title = tk.Label(
            self.frame0,
            text="Welcome to Wordly",
            bg="#90C6E5",
            fg="#0A659A",
            font=self.title_font,
            width=19,
        )
        self.message = tk.Message
        self.title.grid(column=0, row=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()
