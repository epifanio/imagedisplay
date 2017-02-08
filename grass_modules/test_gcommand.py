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
from g2g import Grass2img

outputname='mkt_cl5'

grass_img = Grass2img([outputname], tmpdir='lik4').makeimg()

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