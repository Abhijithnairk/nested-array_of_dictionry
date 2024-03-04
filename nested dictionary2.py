employee_data={
    'employee1':{
        'name':'alice',
        'age':28,
        'position':'software engineer'
    },
    'employee2':{
        'name':'bob',
        'age':35,
        'position':'data scientist'
    },
    'employee3':{
        'name':'charlie',
        'age':42,
        'position':'product manager'
    }
}    

newdata={
    'name':'sanjay',
    'age':19,
    'position':'actor'
}

employee_data['employee4']=newdata
print(employee_data)