import schedule
import time
from src.predict import run_batch_prediction

schedule.every(5).minutes.do(run_batch_prediction)

print("Scheduler started. Running every 5 minutes...")
while True:
    schedule.run_pending()
    time.sleep(1)