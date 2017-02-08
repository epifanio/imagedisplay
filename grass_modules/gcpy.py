#!/usr/local/bin/python36

import sys
import os

class enableGrass():
    def __init__:
        self.GISDBASE = "/Users/epi/grassdata/"
        self.MAPSET = "copy"
        self.LOCATION_NAME = "project"


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
from g2g import Grass2img