import time
import schedule
import numpy as np
import re

from datetime import datetime

while (datetime.now()  < datetime(2000,1,1)):
    time.sleep(1)
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

times = np.load('raspored.npy')

def ring_bell():
    print("Zvoniii")
    GPIO.output(17, GPIO.HIGH)
    time.sleep(3.5)
    GPIO.output(17, GPIO.LOW)

def load_weekend():
    weekend = np.load('vikend.npy')
    for j in weekend:
        if bool(re.match("(([0-9])|([0-9][0-9]))[:][0-9][0-9]", j)):
            schedule.every().saturday.at(j).do(ring_bell)
            schedule.every().sunday.at(j).do(ring_bell)

def load_schedule():
    schedule.clear()
    load_weekend()
    for j in times:
        if bool(re.match("(([0-9])|([0-9][0-9]))[:][0-9][0-9]", j)):
            schedule.every().monday.at(j).do(ring_bell)
            schedule.every().tuesday.at(j).do(ring_bell)
            schedule.every().wednesday.at(j).do(ring_bell)
            schedule.every().thursday.at(j).do(ring_bell)
            schedule.every().friday.at(j).do(ring_bell)
    np.save("raspored.npy", times)

load_schedule()

print(schedule.jobs)

while True:
    schedule.run_pending()
    time.sleep(0.1)