import schedule
import time
import os

def run_pipeline():
    print("[+] Running scraping...")
    os.system("python scraping.py")

    print("[+] Running sentiment classification...")
    os.system("python model.py")

# Schedule: every 3 days at 10:00 AM
schedule.every(1).days.at("10:00").do(run_pipeline)

print("⏱️ Scheduler started. Waiting for job...")
while True:
    schedule.run_pending()
    time.sleep(60)

# Note: This script uses the `schedule` library to run the scraping and sentiment classification scripts every 3 days at 10:00 AM.

# How this works?
# 1. os.system("python scraping.py") tells operating system to run spraping.py script. (e.g using NewsAPI, saving to csv) 
# 2. os.system("python model.py") runs the sentiment classification script, which reads the CSV, classifies headlines, and saves results.
# 3. schedule.every(3).days.at("10:00").do(run_pipeline) schedules the full pipeline to run every 3 days at 10:00 AM.
# 4. The while loop keeps the script running, checking every minute if it's time to run the scheduled job.
#    This allows the pipeline to run automatically without manual intervention.