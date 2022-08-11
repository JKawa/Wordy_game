from random_word import RandomWords
from typing import List
def generate_word(length)->str:
    random_words = RandomWords()
    word=str(random_words.get_random_word(maxLength=length, hasDictionaryDef="true"))
    return word
def lista_gener_word(word)->List:
    word=word.lower()
    lista=[]
    for letter in word:
        lista.append(letter)
    return lista
word=generate_word(5)
lista=lista_gener_word(generate_word(5))
print(word)

