#!/usr/bin/python3
import schedule
import time



def schedulejob():
    now = time.localtime()
    current_time = time.strftime("%H:%M:%S", now)
    print("sheduled task ", current_time)
    with open('output.txt', 'a') as f: 
        print("sheduled task ", current_time, file=f)
schedule.every(60).minutes.do(schedulejob)

while True:
    print("hello world igen")
    schedule.run_pending()
    time.sleep(1)
   # pass
