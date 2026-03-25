import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

data = {'attendance': [95, 80, 70, 90, 60, 85, 78, 92, 67, 80],
    'previous_grades': [85, 70, 75, 88, 65, 90, 80, 85, 78, 72],
    'study_hours': [10, 8, 6, 12, 4, 14, 7, 11, 5, 9],
    'participation': [9, 6, 7, 9, 5, 10, 8, 9, 6, 7],
    'marks': [90, 55, 60, 92, 50, 95, 78, 85, 62, 70]  }

df = pd.DataFrame(data)

X = df[['attendance', 'previous_grades', 'study_hours', 'participation']]
y = df['marks']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

marks_model = LinearRegression()
marks_model.fit(X_train_scaled, y_train)

print("\nEnter student details to predict marks:")

attendance = float(input("Attendance (%): "))
previous_grades = float(input("Previous Grades: "))
study_hours = float(input("Study Hours: "))
participation = float(input("Participation (1-10): "))

user_data = np.array([[attendance, previous_grades, study_hours, participation]])
user_data_scaled = scaler.transform(user_data)
predicted_marks = marks_model.predict(user_data_scaled)[0]


if predicted_marks < 40:
    print(f"Predicted Marks: {predicted_marks:.2f} -> Fail")
else:
    print(f"Predicted Marks: {predicted_marks:.2f} -> Pass")
