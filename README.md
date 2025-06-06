# Job Scheduling System - Backend

## Overview
This project is a backend job scheduling system built in Python.  
It allows scheduling simple jobs ("Hello World") to run at specific times or repeatedly at intervals:
- Hourly (run at specific minute of each hour)  
- Daily (run at specific time of day)  
- Weekly (run on specific day and time of week)

The scheduler uses the APScheduler Python library and prints "Hello World" to the console when a job runs.

---

## How to Run

1. Make sure you have Python 3 installed (tested with Python 3.11.5).  
2. Install dependencies by running:  pip install apscheduler
3. Save the script as job_scheduler.py and Run the script:  python job_scheduler.py
4. Keep the terminal open. The scheduler will print messages at the configured times.

---

## Features Implemented
- Scheduling jobs hourly, daily, and weekly.  
- Console output on job execution.  
- Uses Cron-like scheduling for flexibility.

---

## Assumptions
- Job schedules are configured directly in code (no user input interface).  
- Job task is simplified to console printing for demonstration.  
- Script needs to run continuously to trigger scheduled jobs.

---

## Author
Aayush Agrawal  
Final Year BTech, IIT Jodhpur  
