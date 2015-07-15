#!/usr/bin/ python
from flask import Flask
from datetime import timedelta
from datetime import datetime
from datetime import date
from optparse import OptionParser

app = Flask(__name__)

def daysFromChristmas():
    currentdate = date.today()
    christmas = date(datetime.today().year,12,25)
    if christmas < currentdate:
        christmas = date(datetime.today().year + 1,12,25)
    delta = christmas - currentdate
    days = delta.days
    return "%d from the nearest Christmas" % days

def daysFromDate(strdate):
    currentdate = date.today()
    futuredate = datetime.strptime(strdate, '%Y-%m-%d').date()
    delta = futuredate - currentdate
    return delta.days
    
def event(strdate,event):
    days = daysFromDate(strdate)
    return "%d days until %s" % (days,event)

def deadline(strdate):
    days = daysFromDate(strdate)
    futuredate = datetime.strptime(strdate, '%Y-%m-%d').date()
    return "%d days until %s" % (days, futuredate.strftime("%d %B, %Y"))

@app.route("/")
def main():
    parser = OptionParser()
    parser.add_option("-d", "--deadline", dest="date",
                      help="Specify the deadline in ISO format: yyyy-mm-dd", metavar="DEADLINE")
    parser.add_option("-e", "--event", dest="event", 
                      help="Name of the deadline event",metavar="EVENT")
    (options, args) = parser.parse_args()
    result = ""
    if options.date is not None:
        if options.event is not None:
            result = event(options.date,options.event)
        else:
            result = deadline(options.date)
    else:
        result = daysFromChristmas()
    return result

if __name__ == "__main__":
    app.run()
    
        



