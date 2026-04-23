EX.NO.07
1.) Decision Tree Classifier:
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree from sklearn.metrics import
accuracy_score
# Load dataset
data = pd.read_csv("/content/placement_data.csv")
# Features and Target
X =
data[['cgpa','communication_skills','projects_completed','iq','internsh ip_experience']]
y = data['placement']
# Split dataset
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2,
random_state=42
)
# Create model
model = DecisionTreeClassifier()
# Train
model.fit(X_train,y_train) # Predict

y_pred = model.predict(X_test)
# Accuracy
accuracy = accuracy_score(y_test, y_pred) print("Model Accuracy:",
accuracy)
# Predict new candidate new_candidate =
pd.DataFrame(
[[8.1, 7, 3, 110, 1]],
columns=X.columns
)
prediction = model.predict(new_candidate)
if prediction[0] == 1:
print("Candidate will likely be PLACED") else:
print("Candidate will likely NOT be placed")
plt.figure(figsize=(12,8))
plot_tree(model, feature_names=X.columns, class_names=["No", "Yes"], filled=True)
plt.title("Decision Tree for Placement Prediction") plt.show()
