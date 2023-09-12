# Basic intro of List comprehension
a = [1, 2 ,3]
b=[n+1 for n in a ]
print(b)

name = "Deek"
new_list = [letter for letter in name ]
print(new_list)

l=["Xyzdwd", "Abcs", "Pqrsd","idfnvj","hsvj"]
new_list1 = [letter for letter in l if len(letter)<5]
print(new_list1)