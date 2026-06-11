import joblib

model = joblib.load("credit_risk_model.pkl")

print("Model loaded successfully!")
print(model)