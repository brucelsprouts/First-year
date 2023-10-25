"""
CS1026a 2023
Assignment 02 LIBRARY SYSTEM - library.py
Bruce
251368377
bli232
10/25/2023
"""

#Start function that runs code
def start():
    #All books in library
    allBooks = [
        ['9780596007126',"The Earth Inside Out","Mike B",2,['Ali']],
        ['9780134494166',"The Human Body","Dave R",1,[]],
        ['9780321125217',"Human on Earth","Jordan P",1,['David','b1','user123']]
    ]

    #Borrowed ISBNs (books that have been taken out)
    borrowedISBNs = []

    #Runs the menu screen and takes input
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
        elif user_input in ["5", "x"]:      #Exits code
            exit_program(allBooks, borrowedISBNs)
        else:       #Invalid case
            print("Wrong selection! Please select a valid option.")
            
#Prints the menu for the library
def printMenu():
    print('\n######################')
    print('1: (A)dd a new book.')
    print('2: Bo(r)row books.') 
    print('3: Re(t)urn a book.') 
    print('4: (L)ist all books.') 
    print('5: E(x)it.') 
    print('######################\n')

#Checks if the given ISBN meets the given criteria
def is_valid_isbn(isbn,allBooks):
    if len(isbn) != 13 or not isbn.isdigit(): #Character length
        print("Invalid ISBN!")
        return "case0" #Invalid input
    
    for book in allBooks:   
        if book[0] == isbn:
            print("Invalid ISBN!")
            return "case0" #Invalid input
    
    #Math to calculate the ISBN and validates if its a multiple of 10
    isbn_digits = []
    for digit in isbn:
        isbn_digits.append(int(digit))
    weights = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
    total = 0
    for weight, digit in zip(weights, isbn_digits):
        total += weight * digit
    if total % 10 == 0:
        return "case1"  #Valid input
    
    else:
        print("Invalid ISBN!")
        return "case2" #Invalid ISBN (exits add_book)

#Function to add books to the library
def add_book(allBooks):
    book_info = ['',"","",0,[]] #Default informaiton that gets filled by the new books

    #Validates input of book name
    while True:
        book_name = input("Book name> ")
        if '*' not in book_name and '%' not in book_name:
            book_info[1] = book_name
            break
        else:
            print("Invalid book name!")

    #Input for author name
    book_info[2] = input("Author name> ")

    #Validates input of edition of book
    while True:
        edition_input = input("Edition> ")
        if edition_input.isdigit():
            book_info[3] = int(edition_input)
            break
        else:
            print("Invalid book edition!")

    #Validates the input of ISBN
    while True:
        isbn_input = input("ISBN> ")
        case_number = is_valid_isbn(isbn_input, allBooks)
        if case_number == "case1":      #Adds book to allBooks
            book_info[0] = isbn_input
            book_info[4] = []
            allBooks.append(book_info)
            print("A new book is added successfully.")
            break
        elif case_number == "case2":    #Exists add_book if ISBN meets all criteria but the divisible condition
            break

#Function to borrow books from the library
def borrow_books(allBooks, borrowedISBNs):
    borrower_name = input("Enter the borrower name> ").strip()
    search_term = input("Search term> ").strip().lower()
    book_checker = 0    #Checker to see if the book was found and borrowed from allBooks

    for book in allBooks:   #Checks all books in allBooks
        unavailable_check = 0   #Checker for avaibility of book
        for borrowed in borrowedISBNs:  #Checks for each borrowed ISBN in borrowedISBNs to determine if a book is avaiable
            if borrowed == book[0]:
                unavailable_check += 1  #Checker to say that a book was found to be unaiable
        if unavailable_check == 0 and search_book(book, search_term) == True:
            book[4].append(borrower_name)
            borrowedISBNs.append(book[0])
            book_checker += 1
            print(f"-\"{book[1]}\" is borrowed!")

    if book_checker == 0:   #If no books were found then say none were found
        print("No books were found.")

#Searches for book with the search term in allBooks
def search_book(book, search_term):
    book_name = book[1].lower()
    search_term = search_term.lower()
    
    if search_term.endswith('*'):   #Case *
        search_term = search_term[:-1]
        if search_term in book_name:
            return True
    elif search_term.endswith('%'): #Case %
        search_term = search_term[:-1]
        if book_name.startswith(search_term):
            return True    
    elif book_name == search_term: #Exact case
        return True
    return False

#Return books to allBooks
def return_book(allBooks, borrowedISBNs):
    input_isbn = input("ISBN> ")
    borrowed_remove = 0 #Counter for if a book was found
    book_name = "" #Name of book beign takem out

    for borrowed in borrowedISBNs:
        if borrowed == input_isbn:
            for book in allBooks:   #Gets name of book
                if book[0] == borrowed:
                    book_name = book[1]
            borrowed_remove += 1
            borrowedISBNs.remove(borrowed)
            print(f"\"{book_name}\" is returned.")
    
    if borrowed_remove == 0:    #Checks if any books were found
        print("No book is found!")

#lists all books in allBooks in a format
def list_books(allBooks, borrowedISBNs):
    for book in allBooks:
        print("---------------")

        #Checks for avaibility of books 
        unavaible_check = 0     #Chekcer to see if a book was avaible
        for borrowed in borrowedISBNs:
            if borrowed == book[0]:
                unavaible_check += 1
                print("[Unavailable]")
        if unavaible_check == 0:
            print("[Available]")

        #Prints out information formated
        print(f"{book[1]} - {book[2]}")
        print(f"E: {book[3]} ISBN: {book[0]}")
        print(f"Borrowed by: {book[4]}")

#Exits the program
def exit_program(allBooks, borrowedISBNs):
    print("$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
    list_books(allBooks, borrowedISBNs)
    exit()

start() #Runs program