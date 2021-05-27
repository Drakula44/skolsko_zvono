from flask import Flask
from flask import render_template,request,url_for,redirect
from flask_assets import Environment
import sys
import schedule
import threading
import time

from werkzeug.utils import redirect
import data
import datetime

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)




def run_continuously(interval=1):
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run



stop_run_continuously = run_continuously()

app = Flask(__name__)
assets = Environment(app)
assets.register(data.bundles)


def ring_bell():
    print("Ring!!!"+str(datetime.datetime.now().time()),sys.stderr)
    GPIO.output(17, GPIO.HIGH)
    time.sleep(3.5)
    GPIO.output(17, GPIO.LOW)

def refresh_schedule():
    schedule.clear()
    niz = data.weekly_schedule
    for i in range(7):
        for j in range(len(niz[i])):
            if i == 0:
                schedule.every().monday.at(niz[i][j][0]).do(ring_bell)
                schedule.every().monday.at(niz[i][j][1]).do(ring_bell)
            elif i == 1:
                schedule.every().tuesday.at(niz[i][j][0]).do(ring_bell)
                schedule.every().tuesday.at(niz[i][j][1]).do(ring_bell)
            elif i == 2:
                schedule.every().wednesday.at(niz[i][j][0]).do(ring_bell)
                schedule.every().wednesday.at(niz[i][j][1]).do(ring_bell)
            elif i == 3:
                schedule.every().thursday.at(niz[i][j][0]).do(ring_bell)
                schedule.every().thursday.at(niz[i][j][1]).do(ring_bell)
            elif i == 4:
                schedule.every().friday.at(niz[i][j][0]).do(ring_bell)
                schedule.every().friday.at(niz[i][j][1]).do(ring_bell)
            elif i == 5:
                schedule.every().saturday.at(niz[i][j][0]).do(ring_bell)
                schedule.every().saturday.at(niz[i][j][1]).do(ring_bell)
            elif i == 6:
                schedule.every().sunday.at(niz[i][j][0]).do(ring_bell)
                schedule.every().sunday.at(niz[i][j][1]).do(ring_bell)

def dict_to_array(dict):
    niz = data.weekly_schedule
    for i in range(7):
        niz[i] = []
        j = 0
        key_first = "timeEntryfirst-" + str(i) + "_" + str(j)
        key_second = "timeEntrysecond-" + str(i) + "_" + str(j)
        while key_first in dict and key_second in dict:
            if dict[key_first] != '' and dict[key_second] != '':
                niz[i].append([dict[key_first],dict[key_second]])
            j+=1
            key_first = "timeEntryfirst-" + str(i) + "_" + str(j)
            key_second = "timeEntrysecond-" + str(i) + "_" + str(j)
        data.weekly_schedule = niz
        refresh_schedule

@app.route('/raspored')
def weekly_schedule():
    return render_template('raspored.html',raspored=data.weekly_schedule,diw=data.days_in_week)

@app.route('/toggle')
def toggle():
    if data.working:
        data.working = False
        schedule.clear()
    else:
        data.working = True
        refresh_schedule()
    return redirect(url_for("index"))


@app.route('/')
def index():
    return render_template('index.html',working=data.working)


@app.route('/submit', methods=['GET', 'POST'])
def change_schedule():
    if request.method == 'POST':
        dict_to_array(request.form.to_dict())
        return redirect(url_for("index"))
    else:
        return "greska"
        
@app.route('/')
def main():
    return render_template('index.html',working=data.working)
