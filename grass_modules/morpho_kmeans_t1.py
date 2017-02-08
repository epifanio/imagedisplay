#!/usr/local/bin/python36

import sys
import os


GISDBASE = "/Users/epi/grassdata/"
MAPSET = "copy"
LOCATION_NAME = "project"


if sys.platform=='darwin':
    GISBASE ="/usr/local/grass-7.3.svn"
else:
    GISBASE ="/usr/local/grass-7.3.svn"


os.environ["GISBASE"] = GISBASE
sys.path.append(os.path.join(GISBASE, 'etc/python'))

os.environ["GISDBASE"] = GISDBASE
os.environ["MAPSET"] = MAPSET
os.environ["LOCATION_NAME"] = LOCATION_NAME

gisrc = 'MAPSET: %s\n' % os.environ["MAPSET"]
gisrc += 'GISDBASE: %s\n' % os.environ["GISDBASE"]
gisrc += 'LOCATION_NAME: %s\n' % os.environ["LOCATION_NAME"]
gisrc += 'GUI: text'

grass_gisrc = open('/tmp/gisrc', 'w')
grass_gisrc.write(gisrc)
grass_gisrc.close()
os.environ['GISRC'] = '/tmp/gisrc'


os.environ['PATH'] = '/usr/sbin:/bin/:/usr/bin:%s/bin:%s/scripts:/home/epi/.grass7/addons/bin:/home/epi/.grass7/addons/scripts:/usr/local/opt/gdal2/bin/:/Users/epi/.grass7/addons/bin:$PATH' % (GISBASE, GISBASE)

import grass.script as grass
from grass.script import array as garray
from spectral import *
import spectral.io.envi as envi
spectral.settings.show_progress = False
from grassutil import General, Raster, spectralPlot, Imagery
from makemorfo import Morphometry
from g2g import Grass2img

g = General()
m = Morphometry()
r = Raster()
im = Imagery()

outputname='mkt_cl5'


nnwin_opt = [5, 9, 15, 23, 33]
pmwin_opt = [5, 9, 15, 23, 33]

for i in nnwin_opt:
    for j in pmwin_opt:
                nnwin = i
                pmwin = j
                st = 0.1
                ct = 0.0001
                exp = 0.0
                zs = 1.0
                resolution = 1.0
                img = []
                img = r.makemorfo(input='bathy',
                                  nnwin=nnwin,
                                  pmwin=pmwin,
                                  resolution=resolution,
                                  st=st,
                                  ct=ct,
                                  exp=exp,
                                  zs=zs,
                                  overwrite=True,
                                  remove=False)
                for nc in [3, 5, 7, 9]:
                    for sc in [9, 15, 21]:
                        outputname="clustery_nc%s_sc%s_nn%s_pm%s" % (nc, sc, i, j)
                        im.group(maplist=img[3:], group=outputname, subgroup=outputname)

                        im.cluster(group=outputname,
                                  subgroup=outputname,
                                  signaturefile=outputname+'_sign',
                                  classes=nc,
                                  min_size=sc,
                                  iterations=200,
                                  reportfile=outputname+'_rep',
                                  overwrite=True)


                        im.maxlik(group=outputname,
                                 subgroup=outputname,
                                 signaturefile=outputname+'_sign',
                                 output=outputname,
                                 reject=outputname+'_rej2',
                                 overwrite=True)



outputmaps = grass.read_command('g.list', type='raster', pattern='clustery_*', exclude='*rej2').decode().strip().split('\n')
all = Grass2img(outputmaps, tmpdir='clustery').makeimg(html=True)

import json
with open('data.json', 'w') as fp:
    json.dump(all, fp, sort_keys=True, indent=4)