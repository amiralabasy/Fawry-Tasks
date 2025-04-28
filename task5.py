'''Write a cron job which prints current time to run daily at 8 am'''
########################################################################################################
import schedule
import time
from datetime import datetime

def print_current_time():
    print("Current date and time:", datetime.now())

schedule.every().day.at("08:00").do(print_current_time)
print("Current date and time:", datetime.now())