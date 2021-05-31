import logging
import subprocess
from flask import render_template
import datetime
from project import app
from .models import Stat
date = datetime.datetime.now()
yesterday=date-datetime.timedelta(days=1)
print(date)
print(yesterday)
def decorate(func):
    def call(*args,**kwargs):
        start = datetime.datetime.now()
        result = func(*args,**kwargs)
        funname= func.__name__
        end = datetime.datetime.now()
        message = """Function: {}
        Execution Time : {}
        Address : {}
        Date: {}
        """.format(funname,end-start,func.__name__,start)
        logging.basicConfig(filename='logging.log', level=logging.DEBUG, filemode="w+",
                            format="%(asctime)-15s %(levelname)-8s %(message)s")
        logging.debug(message)
        return result
    call.__name__ = func.__name__
    return call
@app.route("/")
@decorate
def home():
    return render_template("home.html")
@decorate
def get_value(command):
    return subprocess.Popen(command,shell=True,stdout=subprocess.PIPE).stdout.read()

@app.route("/CPU",methods=['GET'])
@decorate
def cpu():

    return render_template("cpu.html",value=(get_value("top -b -n 1 -d1 | grep \"Cpu(s)\" | awk '{printf \"%.2f\",$2}'" )).decode(),values=Stat.query.filter(Stat.time>=yesterday).all())

@app.route("/Disk",methods=['GET'])
@decorate
def disk():

    return render_template("disk.html",value=(get_value("df -h | awk \'$NF==\"/\"{printf \"%s (%s)\",$3,$5}\'")).decode(),values=Stat.query.filter(Stat.time>=yesterday).all())

@app.route("/Memory",methods=['GET'])
@decorate
def memory():
    value = (get_value("free -m | awk 'NR==2{printf \"%s MB (%.2f%%)\",$3,$3*100/$2}'").decode())
    return render_template("memory.html",value=value,values=Stat.query.filter(Stat.time>=yesterday).all())

