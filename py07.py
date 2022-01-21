
# -*- coding: utf-8 -*-

class Book:
    publisher = "HarperCollins"

    def __init__(self,title,author):
        self.title = title
        self.__author = author

    def __str__(self):
        return "Book {} {}".format(self.title,self.__author)

    def get_publisher():
         return Book.publisher