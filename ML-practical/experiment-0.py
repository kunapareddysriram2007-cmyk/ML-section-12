# 1
x = 5              # an integer (whole number)
y = 3.14           # a float (decimal number)
name = "CGPA"      # a string (text) - always in quotes
is_placed = True   # a boolean (True/False)

print(x, type(x))
print(y, type(y))
print(name, type(name))
print(is_placed, type(is_placed))

# 2
a = 7
b = 2

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a ** 2 =", a ** 2)

cgpa = 8.4
print("cgpa == 8.4 :", cgpa == 8.4)
print("cgpa > 8    :", cgpa > 8)
print("cgpa < 6    :", cgpa < 6)

attendance = 85
placed = (cgpa > 8) and (attendance > 80)

print("placed :", placed)

# 3
model_name = "Logistic Regression"
accuracy = 0.87345

print("Accuracy of " + model_name + " is " + str(accuracy))
print(f"Accuracy of {model_name} is {accuracy}")
print(f"Accuracy of {model_name} is {accuracy:.3f}")

# 4
features = ["CGPA", "AptitudeTestScore", "CodingTestScore", "MockInterviewScore"]

print(features)
print(features[0])
print(features[1])
print(features[-1])
print(len(features))

print(features[0:2])

features.append("Internships")
print(features)

# 5
from sklearn.linear_model import Ridge, Lasso, ElasticNet

models = {
    "Ridge": Ridge(alpha=1.0),
    "Lasso": Lasso(alpha=0.01),
    "ElasticNet": ElasticNet(alpha=0.01),
}

print(models)
print(models["Ridge"])

for name, model in models.items():
    print(f"Model name: {name} -> Object: {model}")

# 6
cgpa = 8.2

if cgpa >= 9:
    tier = "High"
elif cgpa >= 7:
    tier = "Mid"
else:
    tier = "Low"

print(f"CGPA {cgpa} falls into tier: {tier}")

missing_count = 0

if missing_count == 0:
    print("No missing values - safe to proceed.")
else:
    print("Missing values found - impute before modelling.")

# 7
depths = [2, 4, 6, 8, 10]

for depth in depths:
    print(f"Training a tree with max_depth = {depth}")

for epoch in range(5):
    print(f"Epoch {epoch}: computing gradient...")

for i, d in enumerate(depths):
    print(f"Sweep step {i}: depth={d}")

# 8
def classify_cgpa(cgpa):
    if cgpa >= 9:
        return "High"
    elif cgpa >= 7:
        return "Mid"
    else:
        return "Low"

print(classify_cgpa(9.5))
print(classify_cgpa(7.8))
print(classify_cgpa(5.2))

def describe_model(name, accuracy):
    return f"{name} achieved {accuracy:.1%} accuracy"

print(describe_model("Random Forest", 0.913))

# 9
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("pandas version:", pd.__version__)
print("numpy version :", np.__version__)

