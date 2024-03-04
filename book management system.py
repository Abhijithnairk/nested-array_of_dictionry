books=[]

def addbook():
    title=input("enter book title: ")
    author=input("enter author name: ")
    genre=input("enter book genre: ")
    
    bk={
        'title':title,
        'author':author,
        'genre':genre
    }
    books.append(bk)
    
    print(f"book {title} added successfully.")
    
def displaybook():
    print("book details are...")
    
    for i in books:
        print(f"title:{i['title']},author:{i['author']},genre:{i['genre']}")
        
        
def searchbook():
    search_book=input("enter book title: ")
    
    for i in books:
        if i['title'].lower()==search_book.lower():
            print("details fettched successfully.")
            print(f"tilte:{i['title']},author:{i['author']},genre:{i['genre']}")
        else:
            print("not found")    
            
def delbook():
    del_book=input("enter book to delete: ")
    
    for i in books:
        if i['title'].lower()==del_book.lower():
            books.remove(i)
            print("deleted.")
            
        else:
            print("not found.")
            
while True:
    print("enter 1 to add book details: ")
    print("enter 2 to diplay book deatails: ")
    print("enter 3 to search for books: ")
    print("enter 4 to delete books: ")
    print("enter 5 to exit: ")
    
    value=input("enter the key here: ")
    
    if value=='1':
        addbook()
        
    elif value=='2':
        displaybook()
        
    elif value=='3':
        searchbook()
        
    elif value=='4':
        delbook()
        
    elif value=='5':
        print("Have a nice day.")
        
    else:
        print("You have entered a wrong input, try again...")