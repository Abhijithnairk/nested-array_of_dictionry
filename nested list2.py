nested_list=[
    [1,2,3],
    [4,5,6],
    [7,8,[9,10]],
    [11,[12,13],14]]

print("element at row 2,column 1:",nested_list[1][0])

print("element at row 3,column 2:",nested_list[2][2][1])

nested_list[0][0]=100
print(nested_list)

newlist=[10,20,30]
nested_list.append(newlist)
print(nested_list)