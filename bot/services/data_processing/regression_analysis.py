import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt

def logistic_regression_analysis(data):
    X = data.drop('success', axis=1)
    y = data['success']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)
    scores = cross_val_score(model, X, y, cv=5)
    return scores.mean()

def plot_regression_results(model, X_test, y_test):
    predictions = model.predict(X_test)
    plt.scatter(y_test, predictions)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.show()
