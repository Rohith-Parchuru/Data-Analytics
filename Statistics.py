import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

marks = [80,85,84,80,83,84,81,78]
hours = [6,6,6.5,7,8,7,8,5]

students = ["Anudeep","Rohith","Charan","Ravi",
            "Bhanu","Sasi","Sasidhar","Bharath"]


print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Variance:", np.var(marks))
print("Standard Deviation:", np.std(marks))
print("Correlation:", np.corrcoef(marks, hours)[0,1])

plt.figure(figsize=(8,5))
plt.bar(students, marks)

plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()