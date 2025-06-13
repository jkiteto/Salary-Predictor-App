import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Sample dataset
data = pd.DataFrame({
    'Age': [25, 30, 45, 35, 22],
    'Gender': [1, 0, 1, 0, 1],  # 1 = Male, 0 = Female
    'Education': [1, 2, 2, 3, 0],  # 0 = High School, 1 = Bachelor, etc.
    'JobLen': [6, 10, 8, 12, 4],
    'Experience': [2, 5, 10, 8, 1],
    'Salary': [30000, 50000, 85000, 75000, 25000]
})

X = data[['Age', 'Gender', 'Education', 'JobLen', 'Experience']]
y = data['Salary']

model = LinearRegression()
model.fit(X, y)

# Save the trained model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("✅ Model saved as model.pkl")
