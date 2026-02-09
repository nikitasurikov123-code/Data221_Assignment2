import pandas as pd
#reads the csv and makes sure it meets the specified conditions
student_data = pd.read_csv("student.csv")
filter_students = student_data[(student_data["studytime"] >= 3) & (student_data["internet"] == 1) & (student_data["absences"] <= 5)]
#save results to a new csv
filter_students.to_csv("high_engagement_data.csv", index = False)
#computes average grade
average_grade = filter_students["grade"].mean()
#number of students saved to the new file
print("Number of students saved: " + str(len(filter_students)))
#print average grade of saved students
print("Average grade of students saved: " + str(average_grade))