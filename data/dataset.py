import pandas as pd
import random

names = [f'Student{i}' for i in range(1, 201)]
scores = [random.randint(50, 100) for _ in range(200)]
grades = []

for s in scores:
    if s >= 90:
        grades.append('A')
    elif s >= 80:
        grades.append('B')
    elif s >= 70:
        grades.append('C')
    elif s >= 60:
        grades.append('D')
    else:
        grades.append('F')

df = pd.DataFrame({'StudentID': range(1,201), 'Name': names, 'Score': scores, 'Grade': grades})
df.to_csv('students_data.csv', index=False)
