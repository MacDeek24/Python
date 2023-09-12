#only print even number
number = [1,1,2,3,5,8,13,21,34,55]
new_list = [n for n in number if n%2 == 0]
print(new_list)