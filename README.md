# 🔍 Hybrid Fake Link Detector

A Python-based URL phishing detector that combines **rule-based keyword checking**, **numeric feature machine learning**, and **TF-IDF + Logistic Regression** to accurately identify fake or malicious links.

---

## Features

1. **Rule-based detection**
   - Checks URLs for suspicious keywords like `winner`, `jackpot`, `freegift`, `claim`, `verify`, `login`, `update`.
   - Instantly flags obvious phishing attempts.

2. **Numeric Feature ML**
   - Features include URL length, number of dots, number of hyphens, presence of HTTPS, IP addresses, and suspicious keywords.
   - Uses a **RandomForestClassifier** for predicting phishing URLs.
   - **Accuracy:** 78.9%

3. **TF-IDF + Logistic Regression**
   - Uses character-level TF-IDF features from URLs.
   - Captures textual patterns in URLs that may indicate phishing.
   - **Accuracy:** 95.3%

4. **Hybrid Approach**
   - Flags a URL as phishing if **any one method** detects it.
   - Provides better overall accuracy and catches tricky phishing URLs.

---

## Requirements

- Python 3.9+
- pandas
- scikit-learn
- joblib
