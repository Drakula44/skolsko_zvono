from flask import Flask
from flask import render_template,request,redirect, url_for
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

def falls_ring():
    print("NEst!!!!!!!!!",sys.stderr)


# schedule.every(15).seconds.do(falls_ring)
stop_run_continuously = run_continuously()








app = Flask(__name__)
manager = Manager(app)
assets = Environment(app)
assets.register(data.bundles)


def ring_bell():
    print("RING!!!!!!!!!",sys.stderr)
    logger.info("RING!!!!!!!!!RING!!!!!!!!!")

def stop_schedule():
    schedule.clear()
    stop_run_continuously.set()

def refresh_schedule():
    schedule.clear()
    stop_run_continuously.set()
    niz = data.weekly_schedule
    stop_run_continuously = run_continuously()
    for i in range(7):
        lena = 0
        if i == 0:
            lena = len(niz['monday'])
        elif i == 1:
            lena = len(niz['tuesday'])
        elif i == 2:
            lena = len(niz['wednesday'])
        elif i == 3:
            lena = len(niz['thursday'])
        elif i == 4:
            lena = len(niz['friday'])
        elif i == 5:
            lena = len(niz['saturday'])
        elif i == 6:
            lena = len(niz['sunday'])

        for j in range(lena):
            if i == 0:
                schedule.every().monday.at(niz['monday'][j][0]).do(ring_bell)
                schedule.every().monday.at(niz['monday'][j][1]).do(ring_bell)
            elif i == 1:
                schedule.every().tuesday.at(niz['tuesday'][j][0]).do(ring_bell)
                schedule.every().tuesday.at(niz['tuesday'][j][1]).do(ring_bell)
            elif i == 2:
                schedule.every().wednesday.at(niz['wednesday'][j][0]).do(ring_bell)
                schedule.every().wednesday.at(niz['wednesday'][j][1]).do(ring_bell)
            elif i == 3:
                schedule.every().thursday.at(niz['thursday'][j][0]).do(ring_bell)
                schedule.every().thursday.at(niz['thursday'][j][1]).do(ring_bell)
            elif i == 4:
                schedule.every().friday.at(niz['friday'][j][0]).do(ring_bell)
                schedule.every().friday.at(niz['friday'][j][1]).do(ring_bell)
            elif i == 5:
                schedule.every().saturday.at(niz['saturday'][j][0]).do(ring_bell)
                schedule.every().saturday.at(niz['saturday'][j][1]).do(ring_bell)
            elif i == 6:
                schedule.every().sunday.at(niz['sunday'][j][0]).do(ring_bell)
                schedule.every().sunday.at(niz['sunday'][j][1]).do(ring_bell)

def refersh_weekly(new_weekly):
    for item in weekly_schedule["monday"]:
        pass




@app.route('/raspored')
def weekly_schedule():
    name = 'Nikola'
    return render_template('raspored.html',name=name,raspored=data.weekly_schedule,diw=data.days_in_week)


@app.route('/')
def main():
    return render_template('index.html',working=data.working)


@app.route('/toggle')
def toggle():
    if data.working == True:
        stop_schedule()
        data.working = False
    else:
        refresh_schedule()
        data.working = True
    return redirect(url_for('main'))

def dict_to_array(dict):
    niz = data.weekly_schedule
    print(niz)
    for i in range(7):
        if i == 0:
            niz['monday'] = []
            j = 0
            key_first = "timeEntryfirst-" + str(i) + "_" + str(j)
            key_second = "timeEntrysecond-" + str(i) + "_" + str(j)
            while key_first in dict and key_second in dict:
                niz['monday'].append([dict[key_first],dict[key_second]])
                j+=1
                key_first = "timeEntryfirst-" + str(i) + "_" + str(j)
                key_second = "timeEntrysecond-" + str(i) + "_" + str(j)
        elif i == 1:
            niz['tuesday'] = []
            j = 0
            key_first = "timeEntryfirst-" + str(i) + "_" + str(j)
            key_second = "timeEntrysecond-" + str(i) + "_" + str(j)
            while key_first in dict and key_second in dict:
                niz['tuesday'].append([dict[key_first],dict[key_second]])
                j+=1
                key_first = "timeEntryfirst-" + str(i) + "_" + str(j)
                key_second = "timeEntrysecond-" + str(i) + "_" + str(j)
        elif i == 2:
            niz['wednesday'] = []
            j = 0
            key_first = "timeEntryfirst-" + str(i) + "_" + str(j)
            key_second = "timeEntrysecond-" + str(i) + "_" + str(j)
            while key_first in dict and key_second in dict:
                niz['wednesday'].append([dict[key_first],dict[key_second]])
                j+=1
                key_first = "timeEntryfirst-" + str(i) + "_" + str(j)
                key_second = "timeEntrysecond-" + str(i) + "_" + str(j)
        elif i == 3:
            niz['thursday'] = []
            j = 0
            key_first = "timeEntryfirst-" + str(i) + "_" + str(j)
            key_second = "timeEntrysecond-" + str(i) + "_" + str(j)
            while key_first in dict and key_second in dict:
                niz['thursday'].append([dict[key_first],dict[key_second]])
                j+=1
                key_first = "timeEntryfirst-" + str(i) + "_" + str(j)
                key_second = "timeEntrysecond-" + str(i) + "_" + str(j)
        elif i == 4:
            niz['friday'] = []
            j = 0
            key_first = "timeEntryfirst-" + str(i) + "_" + str(j)
            key_second = "timeEntrysecond-" + str(i) + "_" + str(j)
            while key_first in dict and key_second in dict:
                niz['friday'] .append([dict[key_first],dict[key_second]])
                j+=1
                key_first = "timeEntryfirst-" + str(i) + "_" + str(j)
                key_second = "timeEntrysecond-" + str(i) + "_" + str(j)
        elif i == 5:
            niz['saturday'] = []
            j = 0
            key_first = "timeEntryfirst-" + str(i) + "_" + str(j)
            key_second = "timeEntrysecond-" + str(i) + "_" + str(j)
            while key_first in dict and key_second in dict:
                niz['saturday'].append([dict[key_first],dict[key_second]])
                j+=1
                key_first = "timeEntryfirst-" + str(i) + "_" + str(j)
                key_second = "timeEntrysecond-" + str(i) + "_" + str(j)
        elif i == 6:
            niz['sunday'] = []
            j = 0
            key_first = "timeEntryfirst-" + str(i) + "_" + str(j)
            key_second = "timeEntrysecond-" + str(i) + "_" + str(j)
            while key_first in dict and key_second in dict:
                niz['sunday'].append([dict[key_first],dict[key_second]])
                j+=1
                key_first = "timeEntryfirst-" + str(i) + "_" + str(j)
                key_second = "timeEntrysecond-" + str(i) + "_" + str(j)
    data.weekly_schedule = niz
    refresh_schedule()
        


@app.route('/submit', methods=['GET', 'POST'])
def change_schedule():
    if request.method == 'POST':
        dict_to_array(request.form.to_dict())
        return redirect(url_for('main'),code=302)
    else:
        return "what"
        
#refresh_schedule()
# stop_run_continuously.set()
