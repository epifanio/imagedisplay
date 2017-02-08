#!/usr/local/bin/python36

from bs4 import BeautifulSoup


with open("/Users/epi/leaflet.html") as file:
    htmlFile = file.read()
    soup = BeautifulSoup(htmlFile, "html5lib")
    #print(soup)
    headTag = soup.findAll('script')
    print(headTag)
    divTag = soup.new_tag('div')
    divTag['class'] = "link"
    headTag[-1].insert_after(divTag)
    print(soup) #This should print the new, modified html
    #print(dir(soup))


def makemap(raster):
    zoom = 12
    image = grass_img['bathy_forms']['raster']
    clat, clon = grass_img['bathy_forms']['C']
    ll_lat, ll_lon = grass_img['bathy_forms']['LL']
    ur_lat, ur_lon = grass_img['bathy_forms']['UR']

    maptemplate = """<!DOCTYPE html>
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
    map = open('map.html', 'w')
    map.write(maptemplate)
    map.close()