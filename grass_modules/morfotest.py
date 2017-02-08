#1/usr/local/bin/python3.6

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


os.environ['PATH'] = '/usr/bin:%s/bin:%s/scripts:/home/epi/.grass7/addons/bin:/home/epi/.grass7/addons/scripts:/usr/local/opt/gdal2/bin/:/Users/epi/.grass7/addons/bin:$PATH' % (GISBASE, GISBASE)

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


img = []
img = r.makemorfo(input='bathy', nnwin=15, pmwin=9, resolution=1.0,
                  st=0.1, ct=0.0001, exp=0.0, zs=1.0,
                  overwrite=True, remove=False)
imagegroup = r.rastack(img[3:])

#k = 7
#cluster = "cluster7dtm_bis"
#classifier = r.getKmeans(imagegroup=imagegroup, k=k)
#spectralPlot(classifier[1])


#img.append("mosaic")
print(img)



i.group(maplist=img[3:], group='geoform4', subgroup='geoform4')

i.cluster(group='geoform4',
          subgroup='geoform4',
          signaturefile='geoform3_5_9_sign22',
          classes=5,
          min_size=9,
          iterations=200,
          reportfile='geoform3_5_9_rep22',
          overwrite=True)

i.maxlik(group='geoform4',
         subgroup='geoform4',
         signaturefile='geoform3_5_9_sign22',
         output='geoform3_5_92',
         reject='geoform3_5_9_rej2',
         overwrite=True)

rasterlist = g.glist()

#print(rasterlist)

grass_img = Grass2img(['geoform3_5_92'], tmpdir='lik4').makeimg()


# r.geomorphon elevation=bathyMSL_filled forms=bathyMSL_filled_forms dist=0.1 skip=0.8 --o
grass.run_command('r.geomorphon', elevation='bathy', forms='bathy_forms_flat2', dist=0.1, skip=0.8, flat=2, overwrite=True)

grass_img = Grass2img(['bathy_forms'], tmpdir='lik4').makeimg(html=True)

print(grass_img)

zoom = 12
image = grass_img['bathy_forms']['raster']
clat, clon = grass_img['bathy_forms']['C']
ll_lat, ll_lon = grass_img['bathy_forms']['LL']
ur_lat, ur_lon = grass_img['bathy_forms']['UR']

maptemplate="""<!DOCTYPE html>
<html>
<head>
	<meta charset='utf-8'>
	<title>Leaflet.Control.FullScreen Demo</title>
	<link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css" />
	<style type="text/css">
		#map { width: 700px; height: 433px; }
		.fullscreen-icon { background-image: url(icon-fullscreen.png); }
		/* one selector per rule as explained here : http://www.sitepoint.com/html5-full-screen-api/ */
		#map:-webkit-full-screen { width: 100%% !important; height: 100%% !important; z-index: 99999; }
		#map:-ms-fullscreen { width: 100%% !important; height: 100%% !important; z-index: 99999; }
		#map:full-screen { width: 100%% !important; height: 100%% !important; z-index: 99999; }
		#map:fullscreen { width: 100%% !important; height: 100%% !important; z-index: 99999; }
		.leaflet-pseudo-fullscreen { position: fixed !important; width: 100%% !important; height: 100%% !important; top: 0px !important; left: 0px !important; z-index: 99999; }
	</style>
	<script src="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js"></script>
	<script src="static/Control.FullScreen.js"></script>
</head>
<body>

<div id="map"></div>

<script>
    var base = new L.TileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpandmbXliNDBjZWd2M2x6bDk3c2ZtOTkifQ._QA7i5Mpkd_m30IGElHziw', {
        maxZoom: 19,
        id: 'mapbox.streets'
    });

    var map = new L.Map('map', {
        layers: [base],
        center: new L.LatLng(%s, %s),
        zoom: %s,
        fullscreenControl: true,
        fullscreenControlOptions: { // optional
            title:"Show me the fullscreen !",
            titleCancel:"Exit fullscreen mode"
            }
    });

    var imageUrl = '%s',
    imageBounds = [[%s, %s], [%s, %s]];
    L.imageOverlay(imageUrl, imageBounds).addTo(map);
    // detect fullscreen toggling
    map.on('enterFullscreen', function(){
        if(window.console) window.console.log('enterFullscreen');
    });
    map.on('exitFullscreen', function(){
        if(window.console) window.console.log('exitFullscreen');
    });
</script>
</body>
</html>""" % (clat, clon, zoom, image, ll_lat, ll_lon, ur_lat, ur_lon)
map = open('map.html','w')
map.write(maptemplate)
map.close()

print(maptemplate)

