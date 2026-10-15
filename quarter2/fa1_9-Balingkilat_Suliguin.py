"""
#15 - Suliguin, Jose Santiago T.
9-Balingkilat
October 15, 2026
CS3 - SG9 - Formative Assessment 1
"""

class Publication:
    __title = ""
    __author = ""
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
    def set_title(self, title):
        self.__title = title
    def set_author(self, author):
        self.__author = author
    def getTitle(self):
        return self.__title
    def getAuthor(self):
        return self.__author
    def displayInfo(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")

class Book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.__number_pages = number_pages
        Book.set_number_of_pages(self, number_pages)
    def set_number_of_pages(self, number_pages):
        if self.__number_pages > 0:
            self.__number_pages = number_pages
        else:
            print("Number of pages must be positive.")
            self.__number_pages = abs(self.__number_pages) 
    def get_number_of_pages(self):
        return f"Number of pages: {self.__number_pages}"

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = issue_number
        Magazine.set_issue_number(self, issue_number)
    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("Issue Number must be positive.")
            self.__issue_number = abs(self.__issue_number)
    def get_issue_number(self):
        return f"Issue Number: {self.__issue_number}"
    

pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")

print("Publication Information:")
pub1.displayInfo()
print()

print("Book Information:")
book1 = Book("The Hobbit", "J.R.R Tolkien", -310)
book1.displayInfo()
print(book1.get_number_of_pages())
print()

print("Magazine Information:")
magazine1 = Magazine("National Geographic", "Various Authors", 202)
magazine1.displayInfo()
print(magazine1.get_issue_number())