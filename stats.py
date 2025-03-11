def get_num_words(book):
    return len(book.split())
def get_num_char(Book):
    books = {}
    arr = Book.split()
    for word in arr:
        for char in word:
            if(char.lower() in books):
                books[char.lower()] += 1
            else:
                books[char.lower()] = 1
    return books
def get_sorted_list(Book):
    arr = []
    for book in Book:
        arr.append((book,Book[book]))
    s = sorted(arr,key=lambda b: b[1],reverse=True)
    return s
    
