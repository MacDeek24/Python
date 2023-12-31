import pandas as pd

data = pd.read_csv("2018_Central_Park.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"]== "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"]== "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"]== "Black"])
# print(grey_squirrel_count)
# print(red_squirrel_count)
# print(black_squirrel_count)

data_dict = {
    "Fur color": ["Grey", "Red","Black"], 
    "Count": [grey_squirrel_count, red_squirrel_count , black_squirrel_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")