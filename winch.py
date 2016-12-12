#!/usr/bin/env python
###!/sw/bin/python2.7
"""


Listen for UDP datagrams containing SIO/MET rebroadcast winch wire
data from LCI-90 on USCGC Healy during HLY1202. Details from Scott Hiller via
email of 2012-09-06 w/ HLY12E.ACQ config file for SIO/MET Windows app

The data are broadcast on Port 40192 (but not for HLY1603)

The data fields are:
Date, Time, (ctd winch) Lineout, Speed, Tension, (3/8" winch) Lineout, Speed, Tension, (680 winch) Lineout, Speed, Tension, (9/16 winch) Lineout, Speed, Tension

Sample data line:
 090912,144737,-9.8,-0.0,8.0,0.3,0.0,10.0,0.0,0.0,107.0,-0.1,0.0,86.0

The time stamps seem to be truncated seconds. We often see more than one sample per second
so we'll make our own time stamps

Date from the LCI looks like:
 04RD,2016-09-23T06:30:03.201,00000122,00000000,-00002.9,2823

Programmer: Dale Chayes <dale@ldeo.columbia.edu>
Created:  2012-09-09
Updated:  2012-09-13   switch to own timestamps
Updated:  2016-09-22   use data on port 90
"""

import sys  # for command line args
import socket  # for networking stuff
import traceback  # for errors

from time import strptime, asctime, strftime, mktime  #
from pylab import *
import pytz
from datetime import datetime

UDP_PORT = 40192  # if the science network is woring right
UDP_PORT = 94  # for LCI directly

UDP_IP = "255.255.255.255"  # broadcast address

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#s.bind(('', UDP_PORT))

index = []
time = []
tension = []
avg_tension = []
sample_rate = 2  # sample rate in Hertz
display_window = 5 * 60 * sample_rate * 2  # I want a five minute window
average_window = 4 * 6 * sample_rate  # about four roll/pitch periods

ion()
hold(False)
# fig=figure(1)                   # This works, but fixed (small) size
fig = figure(figsize=(24, 8))
# print dir(fig)

ax = fig.add_subplot(1, 1, 1)
ax.set_ylabel('Tension [pounds]')
ax.set_xlabel('Time ')
ax.set_title('Trawl wire tension')
ax.grid(True)

count = 0
# while count<1000:
while True:
    data, addr = s.recvfrom(1024)  # buffer size is 1024 bytes
    #    print "received message:", data,
    #    print  data,
    t = datetime.utcnow()  # use our own timestamp
    time.append(t)
    time_str = t.isoformat()
    p = data.strip().split(',')
    p = [10, 20, 30, 40, 50]
    #    raw_date = p[0]
    #    raw_time= p[1]

    # for 9/16" wire on science
    #    core_lineout=p[11]
    #    core_speed=p[12]
    #    core_tension=p[13]

    # for 9/16 wire on LCI
    core_lineout = p[4]
    core_speed = p[3]
    core_tension = p[2]

    print(time_str, core_lineout, core_speed, core_tension)
    #    print core_lineout, core_speed, core_tension

    # For CTD
    #    core_lineout=p[2]
    #    core_speed=p[3]
    #    core_tension=p[4]

    # use strptime() to parse time and date
    #    time1= strptime(raw_date+raw_time, '%d%m%y%H%M%S')
    #    time.append(epoch2num(mktime(time1)))  # Unix epoch time as num
    index.append(count)
    #        print asctime(time1)
    #    time1_str=strftime("%Y-%m-%d-%H:%M:%S", time1)
    #        print "Raw:", raw_date, raw_time, time1_str

    # instead of all this tedium:
    #        day=raw_date[0:2]
    #        month=raw_date[2:4]
    #        year='20'+raw_date[4:6]          # fix 2-year future problem
    #        print year, month, day
    #        hour=raw_time[0:2]
    #        minute = raw_time[2:4]
    #        second = raw_time[4:6]

    tension.append(core_tension)
    #    print count, raw_date,raw_time,time[count], time1_str, \
    #    print count, raw_date,raw_time, time1_str, \

    #    print ' %d\t%s\t%s\t%s\t%s', count, time_str, core_lineout, core_speed, core_tension,
    #   print  count, time_str, core_lineout, core_speed, core_tension,

    if count < display_window:
        avg_tension.append(float(core_tension))
    else:
        #        avg_tension.append(array(tension[-(average_window):],dtype='float').mean())
        avg_tension.append(array(tension[-30:], dtype='float').mean())

    # print 'Lengths: ', len(time), len(index), len(tension)

    #    ax.plot_date(time,tension, fmt='r')
    #    ax.plot_date(time,tension, fmt='r', tz=pytz.utc)

    hold(False)
    ax.plot_date(time, tension, fmt='r-', xdate='True', tz=pytz.utc)
    hold(True)
    ax.plot_date(time, avg_tension, fmt='b.', xdate='True', tz=pytz.utc)

    #    ax.plot_date(time,tension, fmt='r')
    ax.set_ylabel('Tension [pounds]')
    ax.set_xlabel('Time [UTC]')
    ax.set_title('Healy Real-Time 9/16 wire tension')
    ax.grid(True)
    gcf().autofmt_xdate()
    draw()  # update the screen plot

    count += 1
    if count > display_window:  # Plot only a fixed number of points
        time.pop(0)
        index.pop(0)
        tension.pop(0)
        avg_tension.pop(0)
        print
        '  {0:.1f}'.format(array(tension[-30:], dtype='float').mean())
        #       print '   > %.1f', avg_tension[-1:][0]
    else:
        print('    > no average yet')


# ---- end of while loop
# ion()
# show()                          #  to keep the plot on the screen

print('Count: ', len(index), 'Tension: ', len(tension))