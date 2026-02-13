from sklearn.linear_model import LinearRegression
import numpy as np

model = LinearRegression()

def train_model(data):
    X = np.arange(len(data)).reshape(-1,1)
    y = data.values.reshape(-1,1)
    model.fit(X,y)
    return model

def predict_next(data):
    X_future = np.array([[len(data)]])
    prediction = model.predict(X_future)
    return prediction[0][0]

# LinearRegression simple pour prédire le prix suivant.