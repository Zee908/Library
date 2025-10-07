class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"کتاب '{self.title}' امانت داده شد.")
        else:
            print(f"کتاب '{self.title}' در حال حاضر امانت داده شده است.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"کتاب '{self.title}' بازگردانده شد.")
        else:
            print(f"کتاب '{self.title}' در امانت نبود.")

    def __str__(self):
        status = "امانت داده شده" if self.is_borrowed else "موجود"
        return f"{self.title} | نویسنده: {self.author} | صفحات: {self.pages} | وضعیت: {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"کتاب '{book.title}' به کتابخانه اضافه شد.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"کتاب '{title}' حذف شد.")
                return
        print(f"کتاب '{title}' یافت نشد.")

    def show_all_books(self):
        if not self.books:
            print("کتابی در کتابخانه موجود نیست.")
        for book in self.books:
            print(book)

    def borrowed_books_count(self):
        return len([b for b in self.books if b.is_borrowed])

    def total_books_count(self):
        return len(self.books)

    def available_books_count(self):
        return len([b for b in self.books if not b.is_borrowed])

    def search(self, keyword):
        results = [b for b in self.books if keyword.lower() in b.title.lower() or keyword.lower() in b.author.lower()]
        if results:
            print(f"نتایج جستجو برای '{keyword}':")
            for b in results:
                print(b)
        else:
            print(f"کتابی با '{keyword}' یافت نشد.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.borrow()
                return
        print(f"کتاب '{title}' یافت نشد.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(f"کتاب '{title}' یافت نشد.")

    def books_by_author(self, author):
        results = [b for b in self.books if b.author.lower() == author.lower()]
        if results:
            print(f"کتاب‌های نویسنده '{author}':")
            for b in results:
                print(b)
        else:
            print(f"کتابی از نویسنده '{author}' یافت نشد.")
