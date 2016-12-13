import sys
import os
# linux
"""
"""
sys.path.append('/usr/local/grass-7.3.svn/etc/python')
os.environ["GISBASE"] = "/usr/local/grass-7.3.svn"
os.environ["GISDBASE"] = "/home/epi/GRASS7DATA"
os.environ["GISDBASE"] = "/home/epi/grassdata"
os.environ["MAPSET"] = "PERMANENT"
#os.environ["LOCATION_NAME"] = "lonlat"
os.environ["LOCATION_NAME"] = "project"
os.environ['GISRC'] = '/tmp/grass7-epi-8352/gisrc'
os.environ['PATH'] = '/usr/local/grass-7.3.svn/bin:/usr/local/grass-7.3.svn/scripts:/home/epi/.grass7/addons/bin:/home/epi/.grass7/addons/scripts:/usr/local/cuda-7.0/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/lib/gmt/bin'


# mac
#sys.path.append('/usr/local/Cellar/grass7/7.0.5/grass-7.0.5/etc/python')
#os.environ["GISBASE"] = "/usr/local/Cellar/grass7/7.0.5/grass-7.0.5"
#os.environ["GISDBASE"] = "/Users/epi/grassdata"
#os.environ["MAPSET"] = "copy"
#os.environ["LOCATION_NAME"] = "project"
#os.environ['GISRC'] = '/var/folders/8b/tqs3j9h114v4j3lq23t833yw0000gn/T/grass7-epi-10954/gisrc'
#os.environ['PATH'] = '/usr/local/Cellar/grass7/7.0.5/grass-7.0.5/bin:/usr/local/Cellar/grass7/7.0.5/grass-7.0.5/scripts:/Users/epi/.grass7/addons/bin:/Users/epi/.grass7/addons/scripts:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Library/TeX/texbin'

# mac GRASS 7.3
"""

sys.path.append('/Applications/GRASS-7.3.app/Contents/MacOS/etc/python')
os.environ['GISRC'] = '/var/folders/8b/tqs3j9h114v4j3lq23t833yw0000gn/T/grass7-epi-12524/gisrc'
os.environ['PATH'] = '/usr/local/Cellar/gdal2/2.1.2/bin:/Applications/GRASS-7.3.app/Contents/MacOS/bin:/Applications/GRASS-7.3.app/Contents/MacOS/scripts:/Users/epi/.grass7/addons/bin:/Users/epi/.grass7/addons/scripts:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Library/TeX/texbin'
os.environ['GIS_LOCK'] = '12524'
os.environ['_'] = '/usr/local/bin/ipython'
os.environ['GRASS_PROJSHARE'] = '/Library/Frameworks/PROJ.framework/Resources/proj'
os.environ['GISBASE'] = '/Applications/GRASS-7.3.app/Contents/MacOS'
os.environ['HISTSIZE'] = '3000'
os.environ['HISTFILE'] = '/Users/epi/grassdata/project/copy/.bash_history'
os.environ['TMPDIR'] = '/var/folders/8b/tqs3j9h114v4j3lq23t833yw0000gn/T/grass7-epi-12524'
os.environ['GRASS_PYTHON'] = 'python'
os.environ['GRASS_VERSION'] = '7.3.svn'
os.environ['GDAL_DRIVER_PATH'] = '/usr/local/lib/gdalplugins'
os.environ['PYTHONPATH'] = '/Applications/GRASS-7.3.app/Contents/MacOS/etc/python'
os.environ['GRASS_ADDON_BASE'] = '/Users/epi/.grass7/addons'
os.environ['GRASS_HTML_BROWSER_MACOSX'] = '-b com.apple.helpviewer'
os.environ['GRASS_HTML_BROWSER'] = 'lynx'
os.environ['GRASS_PAGER'] = 'more'
os.environ['MANPATH'] = '/Applications/GRASS-7.3.app/Contents/MacOS/docs/man:/Users/epi/.grass7/addons/docs/man:/usr/local/share/man:/usr/share/man:/opt/X11/share/man:/Library/TeX/texbin/man:/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk/usr/share/man:/Applications/Xcode.app/Contents/Developer/usr/share/man:/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/share/man'
os.environ['__PYVENV_LAUNCHER__'] = '/usr/local/Cellar/python3/3.5.2_3/bin/python3.5'
os.environ['HOME'] = '/Users/epi'
os.environ['GRASS_GNUPLOT'] = 'gnuplot -persist'
os.environ["GISDBASE"] = "/Users/epi/grassdata"
# !rm -rf /Users/epi/grassdata/.DS_Store
os.environ['DYLD_FRAMEWORK_PATH'] = '/Applications/GRASS-7.3.app/Contents/MacOS/lib'
"""

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

#os.environ['GRASS_HTML_BROWSER'] = 'xdg-open'
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

img = r.makemorfo(input='bathy', nnwin=27, pmwin=39, resolution=1.0, overwrite=True, remove=False)
imagegroup = r.rastack(img[3:])

#k = 7
#cluster = "cluster7dtm_bis"
#classifier = r.getKmeans(imagegroup=imagegroup, k=k)
#spectralPlot(classifier[1])


i.group(maplist=img[:3], group='geoform2', subgroup='geoform2')

i.cluster(group='geoform2',
          subgroup='geoform2',
          signaturefile='geoform5_5_15_sign2',
          classes=5,
          min_size=15,
          iterations=200,
          reportfile='geoform5_5_15_rep2',
          overwrite=True)

i.maxlik(group='geoform2',
         subgroup='geoform2',
         signaturefile='geoform5_5_15_sign2',
         output='geoform5_5_152',
         reject='geoform5_5_15_rej2',
         overwrite=True)

rasterlist = g.glist()

print(rasterlist)

grass_img = Grass2img(['geoform64_bis'], tmpdir='lik4').makeimg()
