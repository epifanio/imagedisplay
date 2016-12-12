#!/usr/local/bin/python

from multiprocessing import Process, Queue

import multiprocessing
from glob import glob
import pandas as pd
import numpy as np
import feather


def worker1(filename, geom=False, data_time=False):
    key=filename.split('/')[-1].split('.')[0][:-22]
    names=['Ping Time',
           'Ping Number',
           'Beam Number',
           'Easting',
           'Northing',
           'Depth',
           'Longitude',
           'Latitude',
           'Backscatter Value',
           'Corrected Backscatter Value',
            'True Angle']
    df = pd.read_csv(filename,
                skiprows=16,
                names=names,
                delim_whitespace=True)
    if geom:
        df['Geom']=makegeom(df=df, x='Easting',y='Northing')
    if data_time:
        df = df.assign(datetime=pd.to_datetime(df['Ping Time'],
                                               unit='s') - pd.Timedelta(16,
                                                                        unit='s'),
                       line=key)
    return df

def makegeom(df, x, y):
    geom = np.core.defchararray.add(
        np.core.defchararray.add(
            np.core.defchararray.add(
                'Point(',
                df[x].values.astype(str)),
            ' '),
        np.core.defchararray.add(
            df[y].values.astype(str),
            ')')
    )
    return geom

def worker2(filename):
    df = feather.read_dataframe(filename)
    return df


def slave1(queue, filename):
    print(filename)
    #val = worker1(filename)
    queue.put(worker1(filename))


lista = []
queue = Queue()



procs = [Process(target=slave1, args=(queue, i)) for i in  glob('%s/*' % '/Users/epi/SHARED/SHARED/ASCII')]
for proc in procs:
    proc.start()
finished = 0

while finished < len(glob('%s/*' % '/Users/epi/SHARED/SHARED/ASCII')):
    #item = queue.get()
    lista.append(queue.get())
    finished = finished+1
    left = len(glob('%s/*' % '/Users/epi/SHARED/SHARED/ASCII')) - finished
    print('running ... %s file left' %  left)

acoustic = pd.concat(lista)
print(acoustic.shape)