from stats import wordcount
from stats import get_book_test
from stats import meat


def main():
 ans=wordcount(get_book_test("books/frankenstein.txt"))
 
 print(meat(get_book_test("books/frankenstein.txt")))
 



main()
