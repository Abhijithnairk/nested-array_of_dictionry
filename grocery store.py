import os

def clear():
    os.system("clear")
    
products=[]

def addproduct():
    name=input("enter product name: ")
    price=int(input("enter price of product: "))
    quantity=input("enter quqntity: ")
    
    pro={
        'name':name,
        'price':price,
        'quantity':quantity
    }
    
    products.append(pro)
    clear()
    print(f"product {name} added successfully.")
    
def displaypro():
    clear()
    print("product deatails are...")
    
    for i in products:
        print(f"name:{i['name']},price:{i['price']},quantity:{i['quantity']}")
        
def searchpro():
    search_product=input("enter name of product: ")
    
    for i in products:
        if i['name'].lower()==search_product.lower():
            clear()
            print("product fetched successfully...")
            
            print(f"name:{i['name']},price:{i['price']},quantity:{i['quantity']}")
            
        else:
            print("not found")
            
def updatepro():
    name=input("enter name of product: ")
    update_product=input("enter product qnt to update: ")
    
    for i in  products:
        if i['name'].lower()==name.lower():
            i['quantity']=update_product
            clear()
            print("updated successfully.")
            
            print(f"name:{i['name']},price:{i['price']},quantity:{i['quantity']}")
            
        else:
            print("not found")
            
def delpro():
    del_pro=input("enter product name to delete: ")
    
    for i in products:
        if i['name'].lower()==del_pro.lower():
            products.remove(i)
            print("deleted")
            clear()
        else:
            print("not found")
            
def main():
    clear()
            
    while True:
        print("enter 1 to add product details: ")
        print("enter 2 to display product details: ")
        print("enter 3 to search product: ")
        print("enter 4 to update product: ")
        print("enter 5 to delete product: ")
        print("enter 6 to exit: ")
        
        value=input("enter key: ")
        
        if value=='1':
            addproduct()
            
        elif value=='2':
            displaypro() 
            
        elif value=='3':
            searchpro()
            
        elif value=='4':
            updatepro()
            
        elif value=='5':
            delpro()
            
        elif value=='6':
            print("have a nice day.")
            
        else:
            print("wrong input, try again.")   
        
        
if __name__=="__main__":
    main()
