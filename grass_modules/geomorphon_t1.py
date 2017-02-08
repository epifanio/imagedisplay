#!/usr/local/bin/python3.6


import sys
import os
import tempfile

GISDBASE = "/Users/epi/grassdata/"
MAPSET = "copy"
LOCATION_NAME = "project"


if sys.platform=='darwin':
    GISBASE ="/usr/local/grass-7.3.svn"
else:
    GISBASE ="/usr/local/grass-7.3.svn"


os.environ["GISBASE"] = GISBASE
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

sys.path.append(os.path.join(GISBASE, 'etc/python'))
os.environ['PATH'] = '%s/bin:%s/scripts:/home/epi/.grass7/addons/bin:/home/epi/.grass7/addons/scripts:/usr/local/opt/gdal2/bin/:/Users/epi/.grass7/addons/bin:$PATH' % (GISBASE, GISBASE)

import grass.script as grass


search = 25
flat = 1.5
skip = 3
dist = 45

outputname = 'bathy_forms_%s_%s_%s_%s' % (search, flat, skip, dist)

grass.run_command('r.geomorphon',
                  elevation='bathy',
                  forms=outputname,
                  search=search,
                  flat=flat,
                  skip=skip,
                  dist=dist,
                  overwrite=True)
