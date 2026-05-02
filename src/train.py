import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import pandas as pd

def train_and_save_model():
    os.makedirs('models', exist_ok=True)
    
    X, y = make_classification(n_samples=100, n_features=2, n_informative=2, 
                               n_redundant=0, random_state=42)
    
    X_df = pd.DataFrame(X, columns=['feature_1', 'feature_2'])
    model = RandomForestClassifier(n_estimators=10)
    model.fit(X_df, y)
    
    model_path = 'models/model.joblib'
    joblib.dump(model, model_path)
    print(f"Model trained and saved to {model_path}")

if __name__ == "__main__":
    train_and_save_model()