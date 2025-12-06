from stats import wordcount
from stats import get_book_test
from stats import meat
from stats import sortit

def sort_on(items):
    return items["num"]

def printit(ans,dick):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {ans} total words")
    print("--------- Character Count -------")
    for ch in dick:
        print(f"{ch}: {dick[ch]}")

def main():
 ans=wordcount(get_book_test("books/frankenstein.txt"))
 dick=meat(get_book_test("books/frankenstein.txt"))
 sorteddick=sortit(dick)
 printit(ans,sorteddick)

def printit(ans,dick):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {ans} total words")
    print("--------- Character Count -------")
    for ch in dick:
        if(ch['char'].isalpha()):
            print(f"{ch['char']}: {ch['nums']}")
 



main()
