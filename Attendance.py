import numpy as np
import matplotlib.pyplot as plt

students = ["S1","S2","S3","S4","S5","S6","S7","S8",
            "S9","S10","S11","S12","S13","S14","S15","S16"]

attendance = [1,2,3,4,2,3,5,1,4,2,3,5,1,4,2,3]

subject1 = [55,68,72,85,60,74,88,52,80,65,70,92,58,83,62,75]

subject2 = [60,57,84,78,87,65,72,63,63,57,77,86,57,87,73,67]

subject3 = [73,54,65,57,85,67,64,67,78,57,64,76,85,75,68,73]

projects = [1,2,3,1,3,1,3,3,2,1,3,1,3,2,1,4]

print("Mean Marks =", np.mean(subject1))
print("Median Marks =", np.median(subject1))
print("Variance =", np.var(subject1))
print("Standard Deviation =", np.std(subject1))

print("Correlation Attendance vs Subject1")
print(np.corrcoef(attendance, subject1))

print("Correlation Attendance vs Subject2")
print(np.corrcoef(attendance, subject2))

print("Correlation Attendance vs Subject3")
print(np.corrcoef(attendance, subject3))

plt.figure(figsize=(10,5))
plt.bar(students, subject1)
plt.title("Student Marks in Subject 1")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

totals = [sum(subject1), sum(subject2), sum(subject3)]
labels = ["Subject1", "Subject2", "Subject3"]

plt.figure(figsize=(7,7))
plt.pie(totals, labels=labels, autopct="%1.1f%%")
plt.title("Marks Distribution")
plt.show()