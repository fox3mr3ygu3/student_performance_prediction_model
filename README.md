Student Grade Prediction Model
📌 Project Overview

This project focuses on predicting students' academic performance using a machine learning classification model. Based on various demographic, behavioral, and academic features, the model predicts a student's final grade class.

The goal is to understand how different factors such as study habits, parental involvement, and extracurricular activities influence academic success.

📊 Dataset Description
🔑 Student Information
StudentID: Unique identifier (1001–3392)
⚠️ Dropped during training because it has no impact on prediction.
👤 Demographic Details
Age: 15–18
Gender:
0 → Male
1 → Female
Ethnicity:
0 → Caucasian
1 → African American
2 → Asian
3 → Other
ParentalEducation:
0 → None
1 → High School
2 → Some College
3 → Bachelor’s
4 → Higher
📚 Study Habits
StudyTimeWeekly: 0–20 hours
Absences: 0–30
Tutoring:
0 → No
1 → Yes
👨‍👩‍👧 Parental Involvement
ParentalSupport:
0 → None
1 → Low
2 → Moderate
3 → High
4 → Very High
🎯 Extracurricular Activities
Extracurricular:
0 → No
1 → Yes
Sports:
0 → No
1 → Yes
Music:
0 → No
1 → Yes
Volunteering:
0 → No
1 → Yes
📈 Academic Performance
GPA: 2.0 – 4.0
🎯 Target Variable
GradeClass:
0 → A (GPA ≥ 3.5)
1 → B (3.0 ≤ GPA < 3.5)
2 → C (2.5 ≤ GPA < 3.0)
3 → D (2.0 ≤ GPA < 2.5)
4 → F (GPA < 2.0)
🤖 Model Information
Model Used: Decision Tree Classifier
Selected because it achieved the best performance compared to other models during experimentation.
⚙️ Training Approach
🔄 Cross Validation
Used K-Fold Cross Validation to ensure the model generalizes well.
The dataset is split into K subsets, and the model is trained and validated multiple times using different splits.
🔍 Hyperparameter Tuning
Applied Grid Search to find the best model parameters.
Combined with K-Fold Cross Validation to systematically evaluate parameter combinations.
🧠 Key Decisions
❌ Dropped StudentID (no predictive value)
🎯 Target variable: GradeClass
✅ Used classification instead of regression (since output is categorical grades)
🔍 Used cross-validation + grid search for robust model selection
🚀 How to Run
# Install dependencies
pip install -r requirements.txt

# Run training script
python train.py
