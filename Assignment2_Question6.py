import pandas as pd
import numpy as np

data_frame = pd.read_csv("crime.csv")
#create a list to label risk level
risk_list = []
#label as high crime or low crime
for i in data_frame["ViolentCrimesPerPop"]:
    if i >= 0.50:
        risk_list.append("HighCrime")
    else:
        risk_list.append("LowCrime")
#add risk labels to a new column
data_frame["Risk"] = risk_list
groups_of_crime = ["HighCrime", "LowCrime"]
#calculate unemployment average unemployment in each crime group
for group in groups_of_crime:
    subsets = data_frame[data_frame["Risk"] == group]
    count = len(subsets)

    if count > 0:
        average_unemployment = subsets["PctUnemployed"].mean()
    else:
        average_unemployment = 0
    print(group, average_unemployment)