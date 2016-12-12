import sys
sys.path.append('/usr/local/grass-7.3.svn/etc/python')

import os
os.environ["GISBASE"] = "/usr/local/grass-7.3.svn"
#os.environ["GISDBASE"] = "/home/epi/GRASS7DATA"
os.environ["GISDBASE"] = "/home/epi/grassdata"
os.environ["MAPSET"] = "PERMANENT"
#os.environ["LOCATION_NAME"] = "lonlat"
os.environ["LOCATION_NAME"] = "project"

#os.environ['GRASS_PYTHON'] = 'python'
#os.environ['TMPDIR'] = '/tmp/grass7-epi-5932'
#os.environ['GRASS_PROJSHARE'] = '/usr/share/proj'
#os.environ['GIS_LOCK'] = '5932'
#os.environ['PYTHONPATH'] = '/usr/local/grass-7.3.svn/etc/python'
#os.environ['GRASS_VERSION'] = '7.3.svn'
#os.environ['GRASS_ADDON_BASE'] = '/home/epi/.grass7/addons/'
#os.environ['GRASS_GNUPLOT'] = 'gnuplot -persist'
#os.environ['GISBASE'] = '/usr/local/grass-7.3.svn'
#os.environ['GISRC'] = '/tmp/grass7-epi-5932/gisrc'
os.environ['GISRC'] = '/tmp/grass7-epi-8352/gisrc'
#os.environ['GRASS_HTML_BROWSER'] = 'xdg-open'
os.environ['PATH'] = '/usr/local/grass-7.3.svn/bin:/usr/local/grass-7.3.svn/scripts:/home/epi/.grass7/addons/bin:/home/epi/.grass7/addons/scripts:/usr/local/cuda-7.0/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/lib/gmt/bin'
#os.environ['HISTFILE'] = '/home/epi/GRASS7DATA/lonlat/PERMANENT/.bash_history'
#os.environ['MANPATH'] = '/usr/local/grass-7.3.svn/docs/man:/home/epi/.grass7/addons/docs/man:/usr/local/man:/usr/local/share/man:/usr/share/man'
#os.environ['LD_LIBRARY_PATH'] = '/usr/local/grass-7.3.svn/lib:/usr/local/cuda-7.0/lib64:'

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

listloc = g.listloc()
rasterlist = g.glist()

print(listloc, rasterlist)

img = r.makemorfo(input='bathyMSL', nnwin=9, pmwin=15, resolution=1.0, overwrite=True, remove=False)
#rint(img)
#r.histo('bathyMSL', stats=True, color='RdYlBu_r')
#r.hypso('bathyMSL', plot=True, report=True)
#r.width('bathyMSL', plot=True, report=True)
imagegroup = r.rastack(img[3:])

#k = 7
#cluster = "cluster7dtm_bis"
#classifier = r.getKmeans(imagegroup=imagegroup, k=k)
#spectralPlot(classifier[1])


i.group(maplist=img[:3], group='geoform', subgroup='geoform')

i.cluster(group='geoform',
          subgroup='geoform',
          signaturefile='geoform6sign4',
          classes=7,
          min_size=9,
          iterations=200,
          reportfile='geoform6rep4',
          overwrite=True)

i.maxlik(group='geoform',
         subgroup='geoform',
         signaturefile='geoform6sign4',
         output='geoform64_bis',
         reject='geoform64_rej',
         overwrite=True)

rasterlist = g.glist()

print(rasterlist)

grass_img = Grass2img(['geoform64_bis'], tmpdir='lik4').makeimg()
