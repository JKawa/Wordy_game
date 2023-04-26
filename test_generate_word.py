import pytest

from world import generate_word

def proper_result():
    return_value=generate_word(5).upper()
    assert isinstance(return_value,str)