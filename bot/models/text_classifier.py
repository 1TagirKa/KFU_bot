from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from .data_processing import load_data, preprocess_text

def train_model(filepath):
    data = load_data(filepath)
    data['processed_text'] = data['Пример запроса'].apply(preprocess_text)
    X_train, X_test, y_train, y_test = train_test_split(data['processed_text'], data['Подтема'], test_size=0.2, random_state=42)

    model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('classifier', LogisticRegression())
    ])
    model.fit(X_train, y_train)
    return model

model = train_model('bot/data/TechnicalProblemsRequest.xlsx')

def classify_text(text):
    # Предполагаемая логика для определения успешности классификации
    processed_text = preprocess_text(text)
    probabilities = model.predict_proba([processed_text])[0]
    max_prob = max(probabilities)
    threshold = 0.5  # порог уверенности, который можно настроить

    if max_prob < threshold:
        return None  # Классификация неудачна
    else:
        prediction = model.predict([processed_text])[0]
        return prediction

