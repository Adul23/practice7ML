import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect('data/ml_pipeline.db')
    cursor = conn.cursor()
    
    # Create input table (Example features: age, income)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS input_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            feature_1 REAL,
            feature_2 REAL,
            processed INTEGER DEFAULT 0  -- 0 = No, 1 = Yes       
        )
    ''')
    
    # Create predictions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY,
            prediction REAL,
            prediction_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Insert some dummy data if empty
    cursor.execute("SELECT COUNT(*) FROM input_data")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO input_data (feature_1, feature_2) VALUES (25.5, 50000.0)")
        cursor.execute("INSERT INTO input_data (feature_1, feature_2) VALUES (30.0, 60000.0)")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()