def start():
    allBooks = [
        ['9780596007126',"The Earth Inside Out","Mike B",2,['Ali']],
        ['9780134494166',"The Human Body","Dave R",1,[]],
        ['9780321125217',"Human on Earth","Jordan P",1,['David','b1','user123']]
    ]

    borrowedISBNs = ["9780321125217"]

    while True:
        printMenu()
        user_input = input("Your selection> ").strip().lower()

        if user_input in ["1", "a"]:
            add_book(allBooks)
        elif user_input in ["2", "r"]:
            borrow_books(allBooks, borrowedISBNs)
        elif user_input in ["3", "t"]:
            return_book(allBooks, borrowedISBNs)
        elif user_input in ["4", "l"]:
            list_books(allBooks, borrowedISBNs)
        elif user_input in ["5", "x"]:
            exit_program(allBooks, borrowedISBNs)
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
            allBooks.append(book_info)
            print("A new book is added successfully.")
            break
        elif case_number == "case2":
            break

def borrow_books(allBooks, borrowedISBNs):
    borrower_name = input("Enter the borrower name> ").strip()
    search_term = input("Search term> ").strip().lower()
    book_checker = 0

    for book in allBooks:
        unavailable_check = 0
        for borrowed in borrowedISBNs:
            if borrowed == book[0]:
                unavailable_check += 1
        if unavailable_check == 0 and search_book(book, search_term) == True:
            book[4].append(borrower_name)
            borrowedISBNs.append(book[0])
            book_checker += 1
            print(f"-\"{book[1]}\" is borrowed!")

    if book_checker == 0:
        print("No books were found.")

def search_book(book, search_term):
    book_name = book[1].lower()
    search_term = search_term.lower()
    
    if search_term.endswith('*'):
        search_term = search_term[:-1]
        if search_term in book_name:
            return True
    elif search_term.endswith('%'):
        search_term = search_term[:-1]
        if book_name.startswith(search_term):
            return True    
    elif book_name == search_term:
        return True
    return False

def return_book(allBooks, borrowedISBNs):
    input_isbn = input("ISBN> ")
    item_remove = 0
    book_name = ""

    for borrowed in borrowedISBNs:
        if borrowed == input_isbn:
            for book in allBooks:
                if book[1] == borrowed:
                    book_name = book[0]
            item_remove += 1
            borrowedISBNs.remove(borrowed)
            print(f"\"{book_name}\" is returned.")
    
    if item_remove == 0:
        print("No book is found!")

def list_books(allBooks, borrowedISBNs):
    for book in allBooks:
        print("---------------")
        unavaible_check = 0
        for borrowed in borrowedISBNs:
            if borrowed == book[0]:
                unavaible_check += 1
                print("[Unavailable]")
        if unavaible_check == 0:
            print("[Available]")

        print(f"{book[1]} - {book[2]}")
        print(f"E: {book[3]} ISBN: {book[0]}")
        print(f"Borrowed by: {book[4]}")

def exit_program(allBooks, borrowedISBNs):
    print("$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
    list_books(allBooks, borrowedISBNs)
    exit()

start()