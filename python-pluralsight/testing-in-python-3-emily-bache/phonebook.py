import os
class Phonebook:
    
    def __init__(self):
        self.numbers = {}
        self.filename = 'phonebook.txt'
        self.cache = open(self.filename,'w')
    
    def add(self,name: str,number: str):
        self.numbers[name] = number

    def lookup_name(self,name: str) -> str:
        return self.numbers[name]
    
    def is_consistent(self):
        for name1, number1 in self.numbers.items():
            for name2,number2 in self.numbers.items():
                if name1 == name2:
                    continue
                if number1.startswith(number2):
                    return False
        return True
    
    def all_names(self):
        return set(self.numbers.keys())
    
    def all_numbers(self):
        return set(self.numbers.values())
    
    def clear(self):
        self.cache.close()
        os.remove(self.filename)