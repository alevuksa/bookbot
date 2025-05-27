from stats import number_of_words
from stats import number_of_char
from stats import sorted_format  
import sys
if len(sys.argv) < 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
def main():
    book_text = get_book_text(sys.argv[1])
    count = number_of_words(book_text)
    number = number_of_char(book_text)
    sorted = sorted_format(number)
    print ("============ BOOKBOT ============") 
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    print(f"Debug: sorted list has {len(sorted)} items")
    for dict_item in sorted:
        char = dict_item["char"]
        char_count = dict_item["num"] 
        if char.isalpha():
            print(f"{char}: {char_count}")
    
    print("============= END ===============")

main()       
