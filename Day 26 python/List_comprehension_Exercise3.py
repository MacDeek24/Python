with open("file1.txt") as file1:
    File_1_data = file1.readlines()
    print(File_1_data)

with open("file2.txt") as file2:
    File_2_data = file2.readlines()
    print(File_2_data)

result = [int(num) for num in File_1_data if num in File_2_data]
print(result)