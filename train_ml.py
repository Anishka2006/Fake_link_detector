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
#creates a dictionary for every 
features = df['url'].apply(extract_features).
