import pandas as pd
import numpy as np
#read csv file
students = pd.read_csv("student.csv")
#create list of grade bands
grade_band = []
#go through each student and assign them a grade
for grade in students['grade']:
    if grade <= 9:
        grade_band.append("Low")
    elif 10 <= grade <= 14:
        grade_band.append("Medium")
    else:
        grade_band.append("High")
#add the grades as a new column in the data-frame
students["grade_band"] = grade_band
bands = ["Low", "Medium", "High"]
data = []
#loop through each band and summarize
for band in bands:
    subsets = students[students['grade_band'] == band]
    number_of_students = len(subsets)
    #compute student stats if there are students in the band
    if number_of_students > 0:
        internet_count = (subsets["internet"] == 1).sum()
        internet_percentage = (internet_count / number_of_students) * 100
        average_absences = subsets["absences"].mean()
        #if no students set everything to 0 to not divide by 0
    else:
        internet_percentage = 0
        average_absences = 0
    #store the results as a row for the summary table
    data.append({"grade_band": band, "number_of_students": number_of_students,
                 "internet_percentage": internet_percentage, "average_absences": average_absences})
summary_table = pd.DataFrame(data)
summary_table.to_csv("student_bands.csv", index = False)
print(summary_table)

