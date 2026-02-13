import numpy as np
from sklearn.linear_model import LogisticRegression

def train_model():
    # Fake dataset pour exemple
    X = np.array([[100], [105], [102], [110], [115], [108]])
    y = np.array([0, 1, 0, 1, 1, 0])  # 1 = Buy, 0 = Sell
    
    model = LogisticRegression()
    model.fit(X, y)
    
    return model

model = train_model()

def predict(price):
    prediction = model.predict([[price]])
    return "BUY" if prediction[0] == 1 else "SELL"
