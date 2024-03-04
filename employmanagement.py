employee=[]

def addemployee():
    name=input("enter your name: ")
    age=int(input("enter your age: "))
    job=input("enter your job position: ")
    
    emp={
        'name':name,
        'age':age,
        'job':job
    }
    employee.append(emp)
    print(f"employee {name} added successfully")
    
def displayemp():
    print(" employ details are...")
    for employ in employee:
        print(f"name:{employ['name']},age:{employ['age']},job:{employ['job']}")
 
 
def searchemp():
    search_name=input("enter the user name ")
    
    for employ in employee:
        if employ['name'].lower() == search_name.lower():
            print("details fetched successfully")
            print(f"name: {employ['name']},age :{employ['age']},job :{employ['job']}")
        else:
            print("not found")  
            
def delemp():
    delete_name=input("enter name to delete: ")
    for employ in employee:
        if employ['name'].lower() == delete_name.lower():
            employee.remove(employ)
            print("deleted")
        
        else:
            print("not found")

while True:
    print("enter 1 to add employee details ")
    print("enter 2 to Display employee details ")
    print("enter 3 to Search employee  ")
    print("enter 4 to delete employee details ")
    print("enter 5 to exit ")

    value=input("enter the key here :")
    
    if value=='1':
        addemployee()
    elif value=='2':
        displayemp()
    elif value=='3':
        searchemp()
    elif value=='4':
        delemp()
    elif value=='5':
        print("have a nice day")
        break
    else:
        print("you have enterd wrong input pls try again")
