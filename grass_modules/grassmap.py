#!/usr/local/bin/python3.6


import sys
import os


GISDBASE = "/Users/epi/grassdata/"
MAPSET = "PERMANENT"
LOCATION_NAME = "nantucket"


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


os.environ['PATH'] = '%s/bin:%s/scripts:/home/epi/.grass7/addons/bin:/home/epi/.grass7/addons/scripts:/usr/local/opt/gdal2/bin/:/Users/epi/.grass7/addons/bin:$PATH' % (GISBASE, GISBASE)

import grass.script as grass
from grass.script import array as garray
from spectral import *
import spectral.io.envi as envi
spectral.settings.show_progress = False
from grassutil import General, Raster, spectralPlot, Imagery
from makemorfo import Morphometry
from g2l import Grass2img, Grass2Leaflet

g = General()
m = Morphometry()
r = Raster()
i = Imagery()

rasterlist = g.glist()

print(rasterlist)

grass_img = Grass2img(['bathy_nantucket'], tmpdir='geomorphon').makeimg(html=True)


print(grass_img['bathy_nantucket'])


