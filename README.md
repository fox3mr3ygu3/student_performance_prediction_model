<h1>📌 Student Grade Prediction Model</h1>

<h2>📌 Project Overview</h2>
<p>
This project focuses on predicting students' academic performance using a machine learning classification model. 
Based on various demographic, behavioral, and academic features, the model predicts a student's final grade class.
</p>

<p>
The goal is to understand how different factors such as study habits, parental involvement, and extracurricular activities influence academic success.
</p>

<hr>

<h2>📊 Dataset Description</h2>

<h3>🔑 Student Information</h3>
<ul>
  <li><b>StudentID:</b> Unique identifier (1001–3392)</li>
  <li>⚠️ Dropped during training because it has no impact on prediction.</li>
</ul>

<h3>👤 Demographic Details</h3>
<ul>
  <li><b>Age:</b> 15–18</li>
  <li><b>Gender:</b>
    <ul>
      <li>0 → Male</li>
      <li>1 → Female</li>
    </ul>
  </li>
  <li><b>Ethnicity:</b>
    <ul>
      <li>0 → Caucasian</li>
      <li>1 → African American</li>
      <li>2 → Asian</li>
      <li>3 → Other</li>
    </ul>
  </li>
  <li><b>ParentalEducation:</b>
    <ul>
      <li>0 → None</li>
      <li>1 → High School</li>
      <li>2 → Some College</li>
      <li>3 → Bachelor’s</li>
      <li>4 → Higher</li>
    </ul>
  </li>
</ul>

<h3>📚 Study Habits</h3>
<ul>
  <li><b>StudyTimeWeekly:</b> 0–20 hours</li>
  <li><b>Absences:</b> 0–30</li>
  <li><b>Tutoring:</b> 0 → No, 1 → Yes</li>
</ul>

<h3>👨‍👩‍👧 Parental Involvement</h3>
<ul>
  <li><b>ParentalSupport:</b>
    <ul>
      <li>0 → None</li>
      <li>1 → Low</li>
      <li>2 → Moderate</li>
      <li>3 → High</li>
      <li>4 → Very High</li>
    </ul>
  </li>
</ul>

<h3>🎯 Extracurricular Activities</h3>
<ul>
  <li>Extracurricular: 0 → No, 1 → Yes</li>
  <li>Sports: 0 → No, 1 → Yes</li>
  <li>Music: 0 → No, 1 → Yes</li>
  <li>Volunteering: 0 → No, 1 → Yes</li>
</ul>

<h3>📈 Academic Performance</h3>
<ul>
  <li><b>GPA:</b> 2.0 – 4.0</li>
</ul>

<h3>🎯 Target Variable</h3>
<ul>
  <li>0 → A (GPA ≥ 3.5)</li>
  <li>1 → B (3.0 ≤ GPA < 3.5)</li>
  <li>2 → C (2.5 ≤ GPA < 3.0)</li>
  <li>3 → D (2.0 ≤ GPA < 2.5)</li>
  <li>4 → F (GPA < 2.0)</li>
</ul>

<hr>

<h2>🤖 Model Information</h2>
<p><b>Model Used:</b> Decision Tree Classifier</p>
<p>
Selected because it achieved the best performance compared to other models during experimentation.
</p>

<h3>⚙️ Training Approach</h3>

<h4>🔄 Cross Validation</h4>
<p>
Used K-Fold Cross Validation to ensure the model generalizes well. 
The dataset is split into K subsets, and the model is trained and validated multiple times using different splits.
</p>

<h4>🔍 Hyperparameter Tuning</h4>
<p>
Applied Grid Search to find the best model parameters. Combined with K-Fold Cross Validation to systematically evaluate parameter combinations.
</p>

<h3>🧠 Key Decisions</h3>
<ul>
  <li>❌ Dropped StudentID (no predictive value)</li>
  <li>🎯 Target variable: GradeClass</li>
  <li>✅ Used classification instead of regression (since output is categorical grades)</li>
  <li>🔍 Used cross-validation + grid search for robust model selection</li>
</ul>

<hr>

<h2>🚀 How to Run</h2>

<pre>
# Install dependencies
pip install -r requirements.txt

# Run training script
python train.py
</pre>
