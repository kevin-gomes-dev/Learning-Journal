import unittest
from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):
    def setUp(self):
        self.phonebook = Phonebook()

    # If resources are tied up, use this to release
    def tearDown(self):
        pass
    
    def test_add(self):
        number = '2312341234'
        name = 'Sam'
        self.phonebook.add(name,number)
        self.assertEqual(self.phonebook.numbers.get(name),number)
    
    def test_look_by_name(self):
        self.phonebook.add('Bob','1234567890')
        number = self.phonebook.lookup_name('Bob')
        self.assertEqual(number,'1234567890')
        
    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup_name('missing')
            
    # @unittest.skip('Hold')
    def test_empty_phonebook_consistent(self):
        is_consistent = self.phonebook.is_consistent()
        self.assertTrue(is_consistent)
        
    def test_single_consistent(self):
        self.phonebook.add('Michelle','123')
        self.assertTrue(self.phonebook.is_consistent())
        
    def test_multiple_consistent(self):
        self.phonebook.add('Bob','12343')
        self.phonebook.add('Jane','94235')
        self.phonebook.add('John','342213')
        self.assertTrue(self.phonebook.is_consistent())
    
    def test_identical_number_consistent(self):
        self.phonebook.add('Bob','12343')
        self.phonebook.add('Sarah','12343')
        self.assertFalse(self.phonebook.is_consistent())
        
    def test_identical_prefix_consistent(self):
        self.phonebook.add('Bob','911842398')
        self.phonebook.add('Jack','911')
        self.assertFalse(self.phonebook.is_consistent())

if __name__ == "__main__":
    unittest.main()