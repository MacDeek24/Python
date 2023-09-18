try:
    file = open("a_file.txt") 
    dictionary = {"key" : "value"}
    value = dictionary["non_existent_key"]
except FileNotFoundError:
    file = open("a_file.txt","w")
    file.write("somthing")
except KeyError as error_message:
    print(f"That key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was close")
