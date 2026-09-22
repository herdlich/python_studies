class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


book_info = Book("Demons", "F. Dostoevsky")

print(book_info.title)   # output: Demons
print(book_info.author)  # output: F. Dostoevsky
