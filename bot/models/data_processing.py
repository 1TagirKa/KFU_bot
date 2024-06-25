import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.model_selection import train_test_split

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    words = text.split()
    words = [word for word in words if word not in stopwords.words('russian')]
    stemmer = SnowballStemmer('russian')
    words = [stemmer.stem(word) for word in words]
    return ' '.join(words)

def load_data(filepath):
    data = pd.read_excel(filepath)
    data['processed_text'] = data['Пример запроса'].apply(preprocess_text)
    return data