import unittest.mock
import pytest
import sys,os,pytest,unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from fizzbuzz import give_fizz,doit
def test_three():
    assert give_fizz(3) == 'Fizz'
    
def test_five():
    assert give_fizz(5) == 'Buzz'

def test_fifteen():
    assert give_fizz(15) == 'FizzBuzz'
    
def test_other():
    assert give_fizz(4) == 4
    
def test_up_to_three(capsys):
    doit(3)
    out = capsys.readouterr()
    assert out[0] == '1\n2\nFizz\n'