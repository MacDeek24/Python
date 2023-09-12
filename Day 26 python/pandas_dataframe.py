import pandas

student_dict = {
    "student":["Angela","james","lily"],
    "score":[85,44,78]
}

#Looping Through dicionaries
# for (key,value) in student_dict.items():
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#Loop through a dataframe
# for (key,value) in student_data_frame.items():
#     print(value)

#Loop through row of dataframe
for (index,row) in student_data_frame.iterrows():
    print(row)