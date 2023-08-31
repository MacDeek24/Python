#format name using function with output ---> (Not valid input)
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid input"
    first_name= f_name.title()
    Last_name= l_name.title()
    return first_name +" "+ Last_name
print(format_name(input("Enter Your First Name : "),input("Enter Your Last Name : ")))