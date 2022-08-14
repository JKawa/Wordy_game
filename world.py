from random_word import RandomWords
from typing import List
from PyDictionary import PyDictionary
dictionary = PyDictionary()

def generate_word(length)->str:
    random_words = RandomWords()
    word = str(random_words.get_random_word(maxLength=length, minLength=length, hasDictionaryDef="true"))
    while (dictionary.meaning(word,True) is None) or (word=='none')or(word=='None'):
        word = str(random_words.get_random_word(maxLength=length, minLength=length, hasDictionaryDef="true"))
    dictionary.meaning(word, True)

    return word
def lista_gener_word(word)->List:
    word=word.lower()
    lista=[]
    for letter in word:
        lista.append(letter)
    return lista
def word_definition(word)->str:
    try:
        return (f"{word}: Verb: {(dictionary.meaning(word)['Verb'][0])}")
    except:
        return (f"{word}: Noun: {(dictionary.meaning(word)['Noun'][0])}")
