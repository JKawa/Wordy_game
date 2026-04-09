from random_word import RandomWords
from typing import List
from PyDictionary import PyDictionary
dictionary = PyDictionary()

def generate_word(length: int) -> str:
    rw = RandomWords()
    word = rw.get_random_word()

    # powtarzaj, dopóki słowo nie ma znaczenia lub długość się nie zgadza
    while (dictionary.meaning(word) is None) or (len(word) != length):
        word = rw.get_random_word()

    return word

def lista_gener_word(word:str)->List:
    word=word.upper()
    lista=[]
    for letter in word:
        lista.append(letter)
    return lista
def word_definition(word:str)->str:
    try:
        return (f"{word}: Verb: {(dictionary.meaning(word)['Verb'][0])}")
    except Exception:
        return (f"{word}: Noun: {(dictionary.meaning(word)['Noun'][0])}")
