# Dirty way to resolve imports, just adds the preceding folder of this file to the path
import sys,os,pytest,unittest
import unittest.mock
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from phonebook import Phonebook

@pytest.fixture
def pb():
    """Create a phone book with 2 items

    Yields:
        Phonebook: The phonebook
    """
    pb = Phonebook()
    yield pb
    pb.clear()

# This calls the is_consistent() and uses the add func with entry1,entry2. Uses *
@pytest.mark.parametrize('entry1,entry2,is_consistent',[
    (('Bob','12345'),('Jen','32411'),True),
    (('Bob','12345'),('Jen','12345'),False),
    (('Bob','12345'),('Jen','1234'),False),
])
def test_is_consistent(pb,entry1,entry2,is_consistent):
    pb.add(*entry1)
    pb.add(*entry2)
    assert pb.is_consistent() == is_consistent

def test_lookup_by_name(pb):
    pb.add('Bob','12345')
    number = pb.lookup_name('Bob')
    assert number == '12345'
    
def test_contains_all_name(pb):
    pb.add('Bob','12345')
    pb.add('Jen','32411')
    assert pb.all_names() == {'Bob','Jen'}

def test_contains_all_numbers(pb):
    pb.add('Bob','12345')
    pb.add('Jen','32411')
    assert pb.all_numbers() == {'12345','32411'}
    
def test_missing_name():
    # Note that this pb is different from the fixture as we don't have in args
    # If we had in args, this would still overwrite exactly like normal variables work
    pb = Phonebook()
    with pytest.raises(KeyError):
        pb.lookup_name('Bob')
        
def test_stub():
    # Now stub is an instance of the class Phonebook, but its lookup_name
    # method does nothing and returns our value
    stub = unittest.mock.Mock(Phonebook)
    stub.lookup_name.return_value = 'James'
    assert stub.lookup_name('a') == "James"