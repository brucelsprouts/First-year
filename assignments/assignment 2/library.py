def start():
    allBooks = [
        ['9780596007126',"The Earth Inside Out","Mike B",2,['Ali']],
        ['9780134494166',"The Human Body","Dave R",1,[]],
        ['9780321125217',"Human on Earth","Jordan P",1,['David','b1','user123']]
    ]

    while True:
        printMenu()
        user_input = input("Your selection> ").strip().lower()

        if user_input in ["1", "a"]:
            add_book(allBooks)
        elif user_input in ["2", "r"]:
            borrow_books(allBooks)
        elif user_input in ["3", "t"]:
            return_book(allBooks)
        elif user_input in ["4", "l"]:
            list_books(allBooks)
        elif user_input in ["5", "x"]:
            exit_program(allBooks)
        else:
            print("Wrong selection! Please select a valid option.")
            
def printMenu():
    print('\n######################')
    print('1: (A)dd a new book.')
    print('2: Bo(r)row books.') 
    print('3: Re(t)urn a book.') 
    print('4: (L)ist all books.') 
    print('5: E(x)it.') 
    print('######################\n')

def is_valid_isbn(isbn,allBooks):
    if len(isbn) != 13 or not isbn.isdigit():
        print("Invalid ISBN!")
        return "case0"
    
    for book in allBooks:
        if book[0] == isbn:
            print("Invalid ISBN!")
            return "case0"
    
    isbn_digits = []
    for digit in isbn:
        isbn_digits.append(int(digit))

    weights = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
    total = 0
    for weight, digit in zip(weights, isbn_digits):
        total += weight * digit

    if total % 10 == 0:
        return "case1"
    else:
        print("Invalid ISBN!")
        return "case2"

def add_book(allBooks):
    book_info = ['',"","",0,[]]

    while True:
        book_name = input("Book name> ")
        if '*' not in book_name and '%' not in book_name:
            book_info[1] = book_name
            break
        else:
            print("Invalid book name!")

    book_info[2] = input("Author name> ")

    while True:
        edition_input = input("Edition> ")
        if edition_input.isdigit():
            book_info[3] = int(edition_input)
            break
        else:
            print("Invalid book edition!")

    while True:
        isbn_input = input("ISBN> ")
        case_number = is_valid_isbn(isbn_input, allBooks)
        if case_number == "case1":
            book_info[0] = isbn_input
            book_info[4] = []
            allBooks.append(book_info.copy())  # Use a copy of the dictionary
            print("A new book is added successfully.")
            break
        elif case_number == "case2":
            break

def borrow_books(allBooks):
    return

def return_book(allBooks):
    return

def list_books(allBooks):
    for book in allBooks:
        print("---------------")
        if not book[4]:
            print("[Available]")
        else:
            print("[Unavailable]")

        print(f"{book[1]} - {book[2]}")
        print(f"E: {book[3]} ISBN: {book[0]}")
        print(f"Borrowed by: {book[4]}")

def exit_program(allBooks):
    print("$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
    list_books(allBooks)
    exit()

start()