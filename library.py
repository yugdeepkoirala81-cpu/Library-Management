'''
Library Management System 
#features
register and login users 
only valid users can view book,issue book, search book, add book, return book
'''

#Creating files user.txt and books.txt to store userdata and bookdata 

import os

if not os.path.exists('users.txt'):
    with open('users.txt',"w") as f:
        pass

if not os.path.exists('books.txt'):
    with open('books.txt',"w") as f:
        pass

# for user data from users.txt into a dict

def load_user():
    user_dict = {}

    try:
        with open("users.txt", "r") as x:
            for line in x:
                line = line.strip()  # Strip newline and extra spaces
                if line:
                    username, password = line.split(',')
                    user_dict[username] = password
    except FileNotFoundError:  # Correct exception type
        print("File not found!")
    return user_dict
# book_id, title, author, quantity

def load_book():
    book_list = []

    try:
        with open("books.txt", "r") as x:
            for line in x:
                line = line.strip()  # Strip newline and extra spaces
                if line:
                    book_id, title, author, quantity = line.split(',')
                    book = {
                        'id': book_id,
                        'title': title,
                        'author': author,
                        'quantity': int(quantity)
                    }
                    book_list.append(book)
    except FileNotFoundError:  # Correct exception type
        print("File not found!")
    return book_list

def get_ids(book_list):
    book_ids = set()  # Use a set for unique IDs
    for book in book_list:
        book_ids.add(book['id'])
    return book_ids

## user registration

def registration(user_dict):
    '''Register new user'''
    print('''\n 
          ---Registration''')
    username=input("Enter username").strip()
    password= input("Enter password").strip()
    if username in user_dict:
        print("User already exists")
        return False
    if not username or not password:
        print("Fields cannot be empty")
        return False
    user_dict[username]=password

    # saving the registered user in users.txt
    with open("users.txt","a") as f:
        f.write(f"{username},{password}\n")

user_dict=load_user()
print(user_dict)
