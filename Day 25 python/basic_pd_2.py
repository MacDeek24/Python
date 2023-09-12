import pandas as pd
df=pd.read_csv("weather_data.csv")
# data_dict = df.to_dict()
# print(data_dict)
# data_list = df["temp"].to_list()
# sum = 0
# count =0
# for i in data_list:
#     sum += i
#     count +=1
# avg=(float)(sum/count)
# print(avg)

# print(df["temp"].mean())
# print(df["temp"].max())
# print(df["condition"])
# print(df.condition)

# print(df[df.day == "Monday"])
# print(df[df.temp == df.temp.max()])

monday = df[df.day == "Monday"]
A = monday.temp 
print(A)
#covert into fahrenheit 
B = (9*A)/5 +32

print(B)