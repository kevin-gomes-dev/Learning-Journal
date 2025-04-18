class Phonebook:
    
    def __init__(self):
        self.numbers = {}
    
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