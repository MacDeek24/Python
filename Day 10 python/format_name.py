#format name using function with output
def format_name():
    first_name= input("Enter Your First Name : ").title()
    Last_name= input("Enter Your Last Name : ").title()
    return first_name +" "+ Last_name
print(format_name())