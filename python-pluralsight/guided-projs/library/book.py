# BOOK CLASS
class Book:
    __slots__ = ('_title','_author','_available')
    def __init__(self,title: str,author: str):
        self.title = title
        self.author = author
        self.available = True

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def available(self):
        return self._available

    @title.setter
    def title(self,title:str):
        self._title = title

    @author.setter
    def author(self,author:str):
        self._author = author

    @available.setter
    def available(self,available: bool):
        if isinstance(available,bool):
            self._available = available
        else:
            print("Boolean not passed, default to False")
            self._available = False
