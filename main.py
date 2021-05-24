from flask import Flask
from flask import render_template,request
from flask_assets import Environment, Bundle
import sys
import schedule
import threading
import time
import data

from flask_script import Manager


import logging


logging.basicConfig(filename='logs.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger(__name__)



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




app = Flask(__name__)
manager = Manager(app)
assets = Environment(app)
assets.register(data.bundles)

def ring_bell():
    print("RING!!!!!!!!!",sys.stderr)
    logger.info("RING!!!!!!!!!RING!!!!!!!!!")

def refresh_schedule():
    schedule.clear()
    niz = weekly_schedule
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

def refersh_weekly(new_weekly):
    for item in weekly_schedule["monday"]:
        pass




@app.route('/raspored')
def weekly_schedule():
    name = 'Nikola'
    return render_template('raspored.html',name=name,raspored=data.weekly_schedule,diw=data.days_in_week)


@app.route('/')
def main():
    return 'Hello, World!'

def dict_to_array(dict):
    for i in range(7):
        niz[i] = []
        j = 0
        key_first = "timeEntryfirst-" + str(i) + "_" + str(j)
        key_second = "timeEntrysecond-" + str(i) + "_" + str(j)
        while key_first in dict and key_second in dict:
            niz[i].append([dict[key_first],dict[key_second]])
            j+=1
            key_first = "timeEntryfirst-" + str(i) + "_" + str(j)
            key_second = "timeEntrysecond-" + str(i) + "_" + str(j)


@app.route('/submit', methods=['GET', 'POST'])
def change_schedule():
    if request.method == 'POST':
        dict_to_array(request.form.to_dict())
        return "lol"
    else:
        return "what"
        
#refresh_schedule()
stop_run_continuously = run_continuously()
# stop_run_continuously.set()
