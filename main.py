from stats import wordcount
from stats import get_book_test
from stats import meat
from stats import sortit
import sys


def sort_on(items):
    return items["num"]


def main():
 if(len(sys.argv)<2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
 ans=wordcount(get_book_test(sys.argv[1]))
 dick=meat(get_book_test(sys.argv[1]))
 sorteddick=sortit(dick)
 printit(ans,sorteddick)

def printit(ans,dick):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {ans} total words")
    print("--------- Character Count -------")
    for ch in dick:
        if(ch['char'].isalpha()):
            print(f"{ch['char']}: {ch['nums']}")
 



main()
