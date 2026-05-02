import sqlite3
import pandas as pd
import joblib
from datetime import datetime

def run_batch_prediction():
    conn = sqlite3.connect('data/ml_pipeline.db')
    
    # 1. ONLY read rows where processed is 0
    query = "SELECT * FROM input_data WHERE processed = 0"
    df = pd.read_sql_query(query, conn)
    
    if df.empty:
        print(f"[{datetime.now()}] No new data found. Skipping...")
        conn.close()
        return

    # 2. Load model
    model = joblib.load('models/model.joblib')
    
    # 3. Predict
    features = df[['feature_1', 'feature_2']]
    predictions = model.predict(features)
    
    # 4. Record results and update 'processed' status
    cursor = conn.cursor()
    try:
        for idx, row in df.iterrows():
            # Insert prediction
            cursor.execute(
                "INSERT INTO predictions (id, prediction, prediction_timestamp) VALUES (?, ?, ?)",
                (row['id'], float(predictions[idx]), datetime.now().isoformat())
            )
            # Mark input as processed
            cursor.execute(
                "UPDATE input_data SET processed = 1 WHERE id = ?",
                (row['id'],)
            )
        
        conn.commit()
        print(f"[{datetime.now()}] Processed {len(df)} new records.")
    except Exception as e:
        conn.rollback()
        print(f"Error during batch update: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    run_batch_prediction()