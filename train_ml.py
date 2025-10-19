import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib


df = pd.read_csv('dataset.csv')
df = df[['url', 'verdict']]

def extract_features(url):
    url = str(url).lower()
    suspicious_words = ['free', 'win', 'click', 'offer', 'buy', 'cheap',
                        'login', 'update', 'secure', 'account', 'verify']
    return {
        'length' : len(url),
        'num_dots' : url.count('.'),
        'num_hyphens' : url.count('-'),
        'has_at' : int('@' in url),
        'has_https' : int(url.startswith('https')),
        'has_digits' : int(any(char.isdigit() for char in url)),
        'num_suspicious_words' : int(any(word in url for word in suspicious_words))
    }
#creates a dictionary for every url with features
features = df['url'].apply(extract_features)

#convert that dictionrr into tables
X = pd.DtaFrame(features.tolist())
y = df['verdict']

#split and train test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)

#learn from dataset
model.fit(X_train, y_train)

#make predictions
y_pred = model.predict(X_test)
accuracy = "accuracy", accuracy_score(y_test, y_pred)
