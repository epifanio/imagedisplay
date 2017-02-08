#!/usr/local/bin/python3.6


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

# r.geomorphon elevation=bathyMSL_filled forms=bathyMSL_filled_forms dist=0.1 skip=0.8 --o

outputname='bathy_forms_search25_skip3_flat15_dist16'

param = {}

import numpy as np

search = np.arange(1, 9, 1)
flat = np.arange(0, 3, 0.1)

skip = np.arange(1, 9, 1)
dist = np.arange(0, 10, 0.5)

grass.run_command('r.geomorphon', elevation='bathy', forms=outputname, search=25, flat=1.5, skip=3, dist=16, overwrite=True)


grass_img = Grass2img([outputname], tmpdir='geomorphon').makeimg(html=True)

print(grass_img)

zoom = 15
image = grass_img[outputname]['raster']
clat, clon = grass_img[outputname]['C']
ll_lat, ll_lon = grass_img[outputname]['LL']
ur_lat, ur_lon = grass_img[outputname]['UR']




maptemplate="""<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <title>Leaflet.Control.FullScreen Demo</title>
    <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css" />
    <style type="text/css">
        body { padding: 0; margin: 0; }
        html, body, #map { height: 100%%; }
        .fullscreen-icon { background-image: url(icon-fullscreen.png); }
        /* one selector per rule as explained here : http://www.sitepoint.com/html5-full-screen-api/ */
        #map:-webkit-full-screen { width: 100%% !important; height: 100%% !important; z-index: 99999; }
        #map:-ms-fullscreen { width: 100%% !important; height: 100%% !important; z-index: 99999; }
        #map:full-screen { width: 100%% !important; height: 100%% !important; z-index: 99999; }
        #map:fullscreen { width: 100%% !important; height: 100%% !important; z-index: 99999; }
        .leaflet-pseudo-fullscreen { position: fixed !important; width: 100%% !important; height: 100%% !important; top: 0px !important; left: 0px !important; z-index: 99999; }
    </style>

<script src="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js"></script>
<script src="../static/Control.FullScreen.js"></script>
</head>
<body>

<div id="map"></div>

<script>
    var mbAttr = 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
                  '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
                  'Imagery © <a href="http://mapbox.com">Mapbox</a>',
                  mbUrl = 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpandmbXliNDBjZWd2M2x6bDk3c2ZtOTkifQ._QA7i5Mpkd_m30IGElHziw';

    var grayscale   = L.tileLayer(mbUrl, {id: 'mapbox.light', attribution: mbAttr}),
        streets  = L.tileLayer(mbUrl, {id: 'mapbox.streets',   attribution: mbAttr}),
        test = L.tileLayer("../lik4/tiles/{z}/{x}/{y}.png", {bounds: [[%s, %s], [%s, %s]]});



    var map = new L.Map('map', {
        layers: [grayscale],
        center: new L.LatLng(%s, %s),
        zoom: %s,
        fullscreenControl: true,
        fullscreenControlOptions: { // optional
            title:"Show me the fullscreen !",
            titleCancel:"Exit fullscreen mode"
            }
    });

    var baseLayers = {
        "Grayscale": grayscale,
        "Streets": streets,
        "test": test
        };

    var imageUrl = '../%s',
    imageBounds = [[%s, %s], [%s, %s]];
    var classification = L.imageOverlay(imageUrl, imageBounds).addTo(map);
    // detect fullscreen toggling
    map.on('enterFullscreen', function(){
        if(window.console) window.console.log('enterFullscreen');
    });
    map.on('exitFullscreen', function(){
        if(window.console) window.console.log('exitFullscreen');
    });

    var sc1 = new L.LayerGroup();
    var sc2 = new L.LayerGroup();

    var overlays = {
        "SC 1": sc1,
        "SC 2": sc2,
        "%s": classification,
        };

    L.control.layers(baseLayers, overlays).addTo(map);

</script>
</body>
</html>""" % (ll_lat, ll_lon, ur_lat, ur_lon, clat, clon, zoom, image, ll_lat, ll_lon, ur_lat, ur_lon, outputname)
map = open('geomorphon/%s.html' % outputname, 'w')
map.write(maptemplate)
map.close()
print(outputname)


outputmaps = grass.read_command('g.list', type='raster', pattern='bathy_forms_search*').decode().strip().split('\n')
all = Grass2img(outputmaps, tmpdir='geomorphon').makeimg(html=True)




template=''
for i in list(all.keys()):
    image = all[i]['raster']
    clat, clon = all[i]['C']
    ll_lat, ll_lon = all[i]['LL']
    ur_lat, ur_lon = all[i]['UR']
    tpl = """
    %s_imageBounds = [[%s, %s], [%s, %s]];
    var %s = L.imageOverlay('../%s', %s_imageBounds).addTo(map);
    """ % (i, ll_lat, ll_lon, ur_lat, ur_lon, i, image, i)
    template += tpl

#print(template)


overlays = ''
for i in list(all.keys()):
    overlays += '"%s": %s,' % (i, i)

#print(overlays)




maptemplate2 = """<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <title>Leaflet.Control.FullScreen Demo</title>
    <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css" />
    <style type="text/css">
        body { padding: 0; margin: 0; }
        html, body, #map { height: 100%%; }
        .fullscreen-icon { background-image: url(icon-fullscreen.png); }
        /* one selector per rule as explained here : http://www.sitepoint.com/html5-full-screen-api/ */
        #map:-webkit-full-screen { width: 100%% !important; height: 100%% !important; z-index: 99999; }
        #map:-ms-fullscreen { width: 100%% !important; height: 100%% !important; z-index: 99999; }
        #map:full-screen { width: 100%% !important; height: 100%% !important; z-index: 99999; }
        #map:fullscreen { width: 100%% !important; height: 100%% !important; z-index: 99999; }
        .leaflet-pseudo-fullscreen { position: fixed !important; width: 100%% !important; height: 100%% !important; top: 0px !important; left: 0px !important; z-index: 99999; }
    </style>

<script src="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js"></script>
<script src="../static/Control.FullScreen.js"></script>
</head>
<body>

<div id="map"></div>

<script>
    var mbAttr = 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
                  '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
                  'Imagery © <a href="http://mapbox.com">Mapbox</a>',
                  mbUrl = 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpandmbXliNDBjZWd2M2x6bDk3c2ZtOTkifQ._QA7i5Mpkd_m30IGElHziw';

    var grayscale   = L.tileLayer(mbUrl, {id: 'mapbox.light', attribution: mbAttr}),
        streets  = L.tileLayer(mbUrl, {id: 'mapbox.streets',   attribution: mbAttr});



    var map = new L.Map('map', {
        layers: [grayscale],
        center: new L.LatLng(%s, %s),
        zoom: %s,
        fullscreenControl: true,
        fullscreenControlOptions: { // optional
            title:"Show me the fullscreen !",
            titleCancel:"Exit fullscreen mode"
            }
    });

    var baseLayers = {
        "Grayscale": grayscale,
        "Streets": streets
        };

    %s

    // detect fullscreen toggling
    map.on('enterFullscreen', function(){
        if(window.console) window.console.log('enterFullscreen');
    });
    map.on('exitFullscreen', function(){
        if(window.console) window.console.log('exitFullscreen');
    });

    var sc1 = new L.LayerGroup();
    var sc2 = new L.LayerGroup();

    var overlays = {
        %s
        };

    L.control.layers(baseLayers, overlays).addTo(map);

</script>
</body>
</html>""" % (clat, clon, 18, template, overlays)

map = open('geomorphon/%s.html' % 'allmapps', 'w')
map.write(maptemplate2)
map.close()
#print(outputname)