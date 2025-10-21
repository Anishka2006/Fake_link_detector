import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report
import joblib

#Load dataset
df = pd.read_csv('dataset.csv')

#feature extraction
def extract_features(url):
    url = url.lower()
    features = {
        'url_length': len(url),
        'num_dots': url.count('.'),
        'num_hyphens': url.count('-'),
        'has_https': int(url.startswith('https://')),
        'has_ip': int(any(c.isdigit() for c in url.split('//')[-1].split('/')[0].split('.'))),
        'has_winner': int('winner' in url),
        'has_jackpot': int('jackpot' in url),
        'has_freegift': int('freegift' in url),
        'has_claim': int('claim' in url)
    }
    return features

# Numeric features for ML
X_numeric = pd.DataFrame(df['url'].apply(extract_features).tolist())
y = df['verdict']



# Split for numeric ML model
X_train_num, X_test_num, y_train, y_test = train_test_split(X_numeric, y, test_size=0.2, random_state=42)

#Train numeric ML model
numeric_model = RandomForestClassifier(n_estimators=200, random_state=42)
numeric_model.fit(X_train_num, y_train)

# Evaluate numeric model
y_pred_num = numeric_model.predict(X_test_num)
#print("Numeric ML Accuracy:", accuracy_score(y_test, y_pred_num))
#print(classification_report(y_test, y_pred_num))



#Train TF-IDF + Logistic Regression
pipe = make_pipeline(
    TfidfVectorizer(analyzer='char_wb', ngram_range=(3,6), max_features=20000),
    LogisticRegression(max_iter=1000)
)
pipe.fit(df.loc[X_train_num.index, 'url'], y_train)

# Evaluate TF-IDF model
y_pred_tfidf = pipe.predict(df.loc[X_test_num.index, 'url'])
print("TF-IDF + LR Accuracy:", accuracy_score(y_test, y_pred_tfidf))
print(classification_report(y_test, y_pred_tfidf))



#Save models
joblib.dump(numeric_model, 'numeric_model.pkl')
joblib.dump(pipe, 'tfidf_model.pkl')
print("Models saved: numeric_model.pkl and tfidf_model.pkl")



#URL checker
def is_fake_url(url, numeric_model, tfidf_model):
    url_lower = url.lower()
    #Rule-based check
    suspicious_keywords = ['winner', 'jackpot', 'freegift', 'claim', 'urgent', 'verify', 'login', 'update']
    for word in suspicious_keywords:
        if word in url_lower:
            return True, f"Contains suspicious keyword '{word}'"
    
    #Numeric feature ML check
    features = extract_features(url_lower)
    df_features = pd.DataFrame([features])
    if numeric_model.predict(df_features)[0] == 1:
        return True, "Numeric ML predicted phishing"
    
    #TF-IDF ML check
    if tfidf_model.predict([url_lower])[0] == 1:
        return True, "TF-IDF ML predicted phishing"
    
    return False, "Safe URL"



# Test
test_url = input("Enter a URL to test: ")
is_fake, reason = is_fake_url(test_url, numeric_model, pipe)
if is_fake:
    print("The URL is likely FAKE or MALICIOUS. Reason:", reason)
else:
    print("The URL is likely SAFE. Reason:")
