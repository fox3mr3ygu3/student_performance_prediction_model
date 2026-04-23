import numpy as np
import joblib


model = joblib.load("model.pkl")
feature_names = [
    "Age", "Gender", "Ethnicity", "ParentalEducation",
    "StudyTimeWeekly", "Absences", "Tutoring",
    "ParentalSupport", "Extracurricular", "Sports",
    "Music", "Volunteering", "GPA"
]

print("Example Input Format:")
print("""
Age: 17
Gender: 1
Ethnicity: 0
ParentalEducation: 2
StudyTimeWeekly: 19.8
Absences: 7
Tutoring: 1
ParentalSupport: 2
Extracurricular: 0
Sports: 0
Music: 1
Volunteering: 0
GPA: 2.9
""")
print("Enter your data:")

user_data = []

for feature in feature_names:
    value = float(input(f"{feature}: "))
    user_data.append(value)

# Convert to correct shape
user_data = np.array(user_data).reshape(1, -1)
#predict
prediction = model.predict(user_data)

print(" Predicted Grade:", int(prediction[0]))