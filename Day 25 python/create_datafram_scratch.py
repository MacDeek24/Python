import pandas as pd

data_dict = {
    "students":["Amy","James","Angela"],
    "scores":[84,48,75]   
}

data =pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
# print(data)