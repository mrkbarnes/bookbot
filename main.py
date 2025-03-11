from stats import get_num_words,get_num_char,get_sorted_list
import sys
def get_book_text(fp):
    book = ''
    with open(fp) as f:
        book = f.read()
        return book
def main():
    if(len(sys.argv) < 1):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    lis = get_num_char(book)
    tup = get_sorted_list(lis)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")
    print("----------- Character Count ----------")
    for l in tup:
        print(f"{l[0]}: {l[1]}")
    print("============= END ===============")
main()
