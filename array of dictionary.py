employee=[]

def addemployee():
    name=input("enter your name: ")
    age=int(input("enter your age: "))
    position=input("enter your position: ")
    
    emp={
        'name':name,
        'age':age,
        'job':position
    }
    
    employee.append(emp)
    print(f"employee{name} added successfully")


  
while True:
    print("enter 1 to add employ details ")
    print("enter 2 to display employ details ")
    print("enter 3 to search employee ")
    print("enter 4 to delete employee details ")
    employee
    
    value=("enter the key here: ")
    
    
    if value=='1':
        addemployee()
        
    # elif value=='2':
    #     displayemp()
        
    # elif value=='3':
    #     searchemp()
        
    # elif value=='4':
    #     delemp()
        
    elif value=='5':
        print("have a nice day")
        break
    
    else:
        print("you have entered a wrong key, Try again")
        
         