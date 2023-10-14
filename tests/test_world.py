import pytest
from src.world import *

#from world import generate_word

def test_generate_word():
    actual=generate_word(5).upper()
    assert isinstance(actual,str)
    
def test_lista_gener_word():
    actual=lista_gener_word("world")
    assert isinstance(actual,list)
    assert len(actual)==5
    
def test_word_definition():
    actual=word_definition("world")
    assert isinstance(actual,str)