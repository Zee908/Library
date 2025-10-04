from index2 import Book,Library
def main():
    lib = Library()

    while True:
        print("\n========= منوی کتابخانه =========")
        print("1- اضافه کردن کتاب")
        print("2- حذف کتاب")
        print("3- نمایش همه کتاب‌ها")
        print("4- نمایش تعداد کل کتاب‌ها")
        print("5- نمایش تعداد کتاب‌های امانت داده شده")
        print("6- نمایش تعداد کتاب‌های موجود")
        print("7- جستجو بر اساس عنوان یا نویسنده")
        print("8- امانت دادن کتاب")
        print("9- بازگرداندن کتاب")
        print("10- نمایش کتاب‌های یک نویسنده")
        print("0- خروج")
        choice = input("انتخاب کنید: ")

        if choice == "1":
            title = input("عنوان کتاب: ")
            author = input("نویسنده: ")
            pages = int(input("تعداد صفحات: "))
            lib.add_book(Book(title, author, pages))

        elif choice == "2":
            title = input("عنوان کتاب برای حذف: ")
            lib.remove_book(title)

        elif choice == "3":
            lib.show_all_books()

        elif choice == "4":
            print("تعداد کل کتاب‌ها:", lib.total_books_count())

        elif choice == "5":
            print("تعداد کتاب‌های امانت داده شده:", lib.borrowed_books_count())

        elif choice == "6":
            print("تعداد کتاب‌های موجود:", lib.available_books_count())
        elif choice == "7":
            keyword = input("عنوان یا نویسنده موردنظر: ")
            lib.search(keyword)

        elif choice == "8":
            title = input("عنوان کتاب برای امانت: ")
            lib.borrow_book(title)

        elif choice == "9":
            title = input("عنوان کتاب برای بازگرداندن: ")
            lib.return_book(title)

        elif choice == "10":
            author = input("نام نویسنده: ")
            lib.books_by_author(author)

        elif choice == "0":
            print("خداحافظ!")
            break

        else:
            print("انتخاب نامعتبر است.")