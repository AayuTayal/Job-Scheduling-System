from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import time

# This is the job that will run
def hello_world(job_name):
    print(f"[{job_name}] Hello World at {time.strftime('%Y-%m-%d %H:%M:%S')}")

# Creating Scheduler
scheduler = BackgroundScheduler()

# --- HOURLY JOB --- (runs at the 20th minute of every hour)
scheduler.add_job(
    hello_world,
    trigger=CronTrigger(minute=20),
    args=["Hourly Job"],
    id="hourly_job"
)

# --- DAILY JOB --- (runs daily at 11:30 AM)
scheduler.add_job(
    hello_world,
    trigger=CronTrigger(hour=11, minute=30),
    args=["Daily Job"],
    id="daily_job"
)

# --- WEEKLY JOB --- (runs every Monday at 10:15 AM)
scheduler.add_job(
    hello_world,
    trigger=CronTrigger(day_of_week='mon', hour=10, minute=15),
    args=["Weekly Job"],
    id="weekly_job"
)

# Starting scheduler
scheduler.start()
print("Scheduler started. Jobs are scheduled in the background.\nPress Ctrl+C to stop.\n")

# Keeping the script alive
try:
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
    print("Scheduler stopped.")
