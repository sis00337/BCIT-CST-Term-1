"""
04. Lab 04 / Assignment 2
Book collection manager
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : Delivery_KiKi
"""


def books_manager() -> None:
    """ Execute the book management program.

    :precondition: other functions that are used in books_manager must correctly work while the program is executing.
    :precondition: the user_input from the starting_menu() must be valid
    :postcondition: the function will execute the book management program that
                    the user can search for books, move books, and terminate the program with a new text file.
    :postcondition: the function will repeatedly show the main menu until the program is terminated.
    :postcondition: If the user's input from the starting menu is between 1 to 6 inclusive, the function will provide
                    searching function to the user.
                    If the user's input is 7, the function will make the user can move a book.
                    If the user's input is 8, the function will terminate the program.
    """
    books_tuple = open_file()
    while True:
        user_input = starting_menu()
        try:
            if 1 <= user_input <= 6:
                search(user_input, books_tuple)
            elif user_input == 7:
                move_book(books_tuple)
            elif user_input == 8:
                terminate_sys(books_tuple)
        except TypeError:
            print("You entered a wrong input. Please Try again :(\n")


def move_book(books_tuple: tuple) -> None:
    """ Show the user a searching menu for moving a book and move a book depending on the search result.

    :precondition: other functions that are used in move_book must correctly work until move_book ends.
    :precondition: the search_by from the move_menu() must be valid
    :postcondition: Show the user a searching menu and prompt the user for how the user want to search books.
    :postcondition: the function will be iterated until the user successfully moves a book.
    :postcondition: If the user's input is valid, the function will show the search result and allow the user can move
                    a book within the search result.
    """
    search_by = move_menu()
    try:
        search_result = search(search_by, books_tuple)
        shelf_options = find_valid_shelves(books_tuple)
        move_book_to_different_shelf(search_result, shelf_options)
    except TypeError:
        print("You entered a wrong input. Please Try again :(\nReturn to the Main Menu...\n")


def open_file() -> tuple:
    """ Read a text file line by line and change it to a dictionary and store all dictionaries to a tuple.

    :precondition: the text file must be correctly encoded
    :precondition: other functions that are used in open_file must correctly work until open_file ends.
    :postcondition: return a tuple containing the information of books that is expressed with dictionaries.
    :postcondition: store the dictionaries to a tuple
    :return: a tuple containing the dictionaries
    """
    original_list = []
    key = ['Author', 'Title', 'Publisher', 'Shelf', 'Category', 'Subject']
    filename = "Books UTF-16.txt"
    with open(filename, encoding="UTF-16") as file_object:
        for line in file_object:
            line_list = list_maker(line)
            books_dic = dictionary_maker(key, line_list)
            original_list.append(books_dic)
    original_list = original_list[1:]
    original_tuple = convert_book_list_to_tuple(original_list)

    return original_tuple


def list_maker(line: str) -> list:
    """ Change a line of text into a list format.

    :param line: a line of text
    :postcondition: the function will divide the text by <Tab> keys ('\t) and get rid of <Enter> keys ('\n')
                    and put the divided text in a list
    :postcondition: if there is no use of <Tab> key in line, the function will put the whole line of text into a list
    :postcondition: return a list of strings divided by <Tab> keys
    :return: a list

    >>> list_maker('')
    ['']
    >>> list_maker('I am a boy')
    ['I am a boy']
    >>> list_maker('Author\\tTitle\\tPublisher\\tShelf\\n')
    ['Author', 'Title', 'Publisher', 'Shelf']
    >>> list_maker('1\\t2\\t3\\t\\t5\\t6\\t7\\n')
    ['1', '2', '3', '', '5', '6', '7']
    >>> list_maker('\\t\\t\\t\\t\\t\\n\\n\\n\\n')
    ['', '', '', '', '', '']
    """
    line_list = line.replace('\n', '').split('\t')
    return line_list


def dictionary_maker(key: list, line_list: list) -> dict:
    """ Change a list of strings into a dictionary format.

    :param key: a list contains strings that corresponds the keys for a dictionary
    :param line_list: a list of strings
    :precondition: key and line_list must have the same length
    :precondition: key must be a list of strings and every element in key must be different
    :postcondition: return a dictionary made up of key as keys and line_list as values
    :return: a dictionary

    >>> dictionary_maker([1, 2, 3], ['', '', ''])
    {1: '', 2: '', 3: ''}
    >>> dictionary_maker(['1', '2', '3'], ['Author', 'Title', 'Publisher'])
    {'1': 'Author', '2': 'Title', '3': 'Publisher'}
    >>> dictionary_maker(['Name', 'Age'], ['Johnson', '27'])
    {'Name': 'Johnson', 'Age': '27'}
    >>> dictionary_maker(['Country', 'City', 'Favorite food'], ['South Korea', 'Seoul', 'Korean BBQ'])
    {'Country': 'South Korea', 'City': 'Seoul', 'Favorite food': 'Korean BBQ'}
    """
    books_dic = dict(zip(key, line_list))
    return books_dic


def convert_book_list_to_tuple(original_list: list) -> tuple:
    """ Transform the list into a tuple of dictionaries after preprocessing and removing the first dictionary.

    Every 'null' value in dictionaries will be changed into 'None'

    :param original_list: a list of dictionaries including the whole information of books
    :precondition: original_list must include the whole information of the entire given text file
    :postcondition: return a tuple of dictionaries that are preprocessed
    :return: a tuple of dictionaries

    >>> convert_book_list_to_tuple([{'Author': 'Author', 'Title': 'Title'}])
    ({'Author': 'Author', 'Title': 'Title'},)
    >>> convert_book_list_to_tuple([{'Author': 'Author'}, {'Author': 'Mike'}, {'Author': 'Mike', 'Title': ''}])
    ({'Author': 'Author'}, {'Author': 'Mike'}, {'Author': 'Mike', 'Title': 'None'})
    >>> convert_book_list_to_tuple([{'0': 'Zero'}, {'1': 'One'}, {'2': 'Two'}, {'3': 'Three'}, {'4': ''}, {'5': ''}])
    ({'0': 'Zero'}, {'1': 'One'}, {'2': 'Two'}, {'3': 'Three'}, {'4': 'None'}, {'5': 'None'})
    """
    for number in range(len(original_list)):
        for key, value in original_list[number].items():
            if value == '':
                original_list[number][key] = 'None'
    original_tuple = tuple(original_list)
    return original_tuple


def find_valid_shelves(books_tuple: tuple) -> list:
    """ Remove duplicates of shelves and store the values in the sorted list.

    :param books_tuple: a tuple of dictionaries including the whole information of books
    :precondition: every dictionary in books_tuple must have the key named 'Shelf'
    :precondition: every values of 'Shelf' must be a string
    :postcondition: remain each unique values of the shelves and store the values in a sorted list and return it
    :return: a sorted list that contains every unique value of shelves

    >>> find_valid_shelves(({'Shelf': '10'}, {'Author': 'Mike', 'Shelf': '10'}, {'Shelf': '10'}))
    ['10']
    >>> find_valid_shelves(({'Shelf': 'Gaby'}, {'Author': 'Mike', 'Shelf': '1'}, {'Shelf': '10'}))
    ['1', '10', 'Gaby']
    >>> find_valid_shelves(({1:'Dog', 'Shelf': 'Reading'}, {'Author': 'Mike', 'Shelf': '11'}, {'Shelf': '20'}))
    ['11', '20', 'Reading']
    >>> find_valid_shelves(({1:'Dog', 'Shelf': 'A'}, {'Author': 'Mike', 'Shelf': 'B'}, {'Shelf': 'C'}))
    ['A', 'B', 'C']
    """
    shelf_numeric_set = set()
    shelf_alphabetic_set = set()
    for index in range(len(books_tuple)):
        if books_tuple[index]['Shelf'].isdigit():
            shelf_numeric_set.add(int(books_tuple[index]['Shelf']))
        elif books_tuple[index]['Shelf'].isalpha():
            shelf_alphabetic_set.add(books_tuple[index]['Shelf'])
    sorted_numeric_list = sorted(list(shelf_numeric_set))
    sorted_numeric_list = [str(element) for element in sorted_numeric_list]
    sorted_alphabetic_list = sorted(list(shelf_alphabetic_set))
    total_list = sorted_numeric_list + sorted_alphabetic_list
    return total_list


def starting_menu() -> int:
    """ Show the menu to the user and prompt the user for what the user wants to do.

    :postcondition: If the user's input is an integer between 1 to 8 inclusive, return the input as an integer.
                    If not, print an error message.
    :return: an integer between 1 to 8 inclusive
    """
    print("---------- Main Menu ----------")
    print("What do you want to do?")
    choice_list = ['1', '2', '3', '4', '5', '6', '7', '8']
    user_choice = input("1) Search Books by Author\n"
                        "2) Search Books by Title\n"
                        "3) Search Books by Publisher\n"
                        "4) Search Books by Shelf\n"
                        "5) Search Books by Category\n"
                        "6) Search Books by Subject\n"
                        "7) Move a Book to another Shelf\n"
                        "8) Quit the program\n")
    user_choice = user_choice.strip()
    if user_choice in choice_list:
        return int(user_choice)


def search(user_input: int, books_tuple: tuple) -> list:
    """ Search for books

    Except for searching by shelf, the function will show the list of books corresponding to your keyword
    even though your search keyword contains a part of the whole data.

    :param user_input: an integer
    :param books_tuple: a tuple of dictionaries including the whole information of books
    :precondition: books_tuple must include the whole information of the entire given text file
    :precondition: user_input must be in range of 1 to 6 inclusive
    :postcondition: find and show the book information that corresponds to the search keyword
    """
    for menu_num in range(1, 7):
        if user_input == menu_num:
            keyword = input("\nPlease enter a search keyword:\n")
            keyword = keyword.lower().strip()
            search_result = search_helper(books_tuple, keyword, menu_num, user_input)
            print(f"\n{len(search_result)} result(s) found\n")
            for number in range(len(search_result)):
                print(f"{number + 1}. {search_result[number]}")
            print('\r')
            return search_result


def search_helper(books: tuple, keyword: str, menu_num: int, user_input: int) -> list:
    """ Search for books depending on the user's input from the menu.

    :param books: a tuple of dictionaries including the whole information of books
    :param keyword: a keyword that user entered for searching for books
    :param menu_num: an integer between 1 to 6 inclusive
    :param user_input: an integer
    :precondition: menu_num must be between 1 to 6 inclusive
    :precondition: user_input must be in range of 1 to 6 inclusive
    :precondition: books must include the whole information of the entire given text file
    :postcondition: search for books depending on user_input and return the result as a list
    :return: a list including the search result
    """
    search_result = []
    for index in range(len(books)):
        key = list(books[index].keys())
        if user_input != 4 and keyword in books[index][key[menu_num - 1]].lower():
            search_result.append(books[index])
        elif user_input == 4:
            if keyword.isdigit() and keyword == books[index][key[menu_num - 1]]:
                search_result.append(books[index])
            elif keyword == '' or keyword.isalpha() and keyword in books[index][key[menu_num - 1]].lower():
                search_result.append(books[index])
    return search_result


def move_menu() -> int:
    """ Show the menu that only contains searching options to the user
        and prompt the user for what the user wants to do.

    :postcondition: If the user's input is an integer between 1 to 6 inclusive, return the input as an integer
                    Otherwise, print an error message
    :return: an integer in range of 1 to 6 inclusive
    """
    print('\r')
    print("---------- Search Menu ----------")
    print("Please search books that you want to change the shelf number.")
    choice_list = ['1', '2', '3', '4', '5', '6']
    user_choice = input("1) Search Books by Author\n"
                        "2) Search Books by Title\n"
                        "3) Search Books by Publisher\n"
                        "4) Search Books by Shelf\n"
                        "5) Search Books by Category\n"
                        "6) Search Books by Subject\n")
    user_choice = user_choice.strip()
    if user_choice in choice_list:
        return int(user_choice)


def move_book_to_different_shelf(search_result: list, shelf_options: list) -> None:
    """ Change the shelf of a book.

    :param search_result: a list of dictionaries that is the result of a searching activity
    :param shelf_options: a sorted list that contains every valid shelves
    :precondition: books_tuple must include the whole information of the entire given text file
    :precondition: every dictionaries in search_result must have the key named 'Shelf'
    :postcondition: If the length of search_result is greater than zero,
                    the user will choose a book within search_result and change the shelf of that book,
                    and the function will return a tuple of dictionaries containing the changed book.
                    Otherwise, the program will go back to the main menu.
    :return: a tuple of dictionaries with the changed book information
    """
    if len(search_result) > 0:
        result_number = select_from_list(search_result)
        print(f"\nThe book is currently on shelf {search_result[result_number]['Shelf']}.\n")
        move_book_helper(search_result, result_number, shelf_options)
        return
    else:
        print("Return to the Main Menu...\n")


def move_book_helper(search_result: list, result_number: int, shelf_options: list) -> None:
    """ Move the book only when the user entered the correct shelf.

    :param search_result: a list of dictionaries that is the result of a searching activity
    :param result_number: an integer returned from the function called select_from_list
    :param shelf_options: a sorted list that contains every valid shelves
    :precondition: the length of search_result must be equal to or greater than one
    :precondition: result_number must be equal to or greater than one
    :precondition: shelf_options must include every shelf
    :precondition: every dictionaries in search_result must have the key named 'Shelf'
    :postcondition: If the user enters the valid shelf, the function will
                    return a tuple of dictionaries containing the changed book.
                    Otherwise, the function will print an error message
    :return: nothing
    """
    change_shelf = input("Please enter the whole letters of the destination shelf from below.\n"
                         "You can choose either shelf number or shelf name\n"
                         "Shelf # : 1 - 38\n"
                         "Shelf Name : Gaby, Island, Lego, Noguchi, Reading, Students\n")
    change_shelf = change_shelf.lower().strip()
    for number in range(len(shelf_options[:])):
        if change_shelf == shelf_options[number].lower():
            print(f"\nYou moved the book from "
                  f"'{search_result[result_number]['Shelf']}' to '{shelf_options[number]}'\n")
            search_result[result_number]['Shelf'] = shelf_options[number]
            print(f"{search_result[result_number]}\n")
            return
    print("You entered the wrong shelf...\nReturn to the Main Menu...\n")


def select_from_list(search_result: list) -> int:
    """ Prompt user for which book the user wants to move within the search result and validate the user's input.

    :param search_result: a list of dictionaries corresponding to the search result
    :precondition: the length of search_result must be equal to or greater than 1
    :postcondition: return the user's input as an integer after minus 1
    :return: the user's input as an integer after minus 1
    """
    result_number = input("Please enter the number of the book you want to change from above...\n")
    if result_number.isalpha() or result_number == '':
        print("\nPlease enter a number...\n")
    elif int(result_number) < 1 or int(result_number) > len(search_result):
        print("\nYou chose the wrong number...\n")
    else:
        return int(result_number) - 1


def terminate_sys(books_tuple: tuple) -> None:
    """ Write a new file and terminate the program.

    :param books_tuple: a tuple of dictionaries reflecting the result of moving books
    :precondition: books_tuple must contains the change if the user moved some books
    :postcondition: If the user did not move any books,
                    the function will write a new file as same as the given text file
                    If the user moved some books,
                    the function will write a new file with the result of moving books
    :return: nothing
    """
    print("System shutdown...")
    new_file = "Books UTF-16.txt"
    with open(new_file, 'w', encoding="UTF-16") as file_object:
        file_object.write('Author\tTitle\tPublisher\tShelf\tCategory\tSubject\n')
        for length in range(len(books_tuple)):
            for key, value in books_tuple[length].items():
                if key != 'Subject':
                    value += '\t'
                elif key == 'Subject':
                    value += '\n'
                file_object.write(str(value))
    quit()


def main() -> None:
    """
    Drives the program.
    """
    # import doctest
    # doctest.testmod(verbose=True)
    print("Welcome to the Book Manager v1.0.0.")
    books_manager()


if __name__ == "__main__":
    main()
