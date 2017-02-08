import sys
import os
import tempfile
import shutil
import uuid

import subprocess
import grass.script as grass
from osgeo import gdal, osr
from collections import OrderedDict
from pyproj import Proj


from IPython.display import display
from ipywidgets import interact, interactive, fixed
from ipywidgets import widgets
import json


def which(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


class Grass2img(object):
    def __init__(self, layers, tmpdir=None):
        self.layers = layers
        self.checkgdaldem()
        self.tmpdir = tmpdir

    def checkgdaldem(self):
        gdaldem = which('gdaldem')
        if not gdaldem:
            print('you need gdaldem')
            return None
        else:
            return gdaldem

    def grasslayercheck(self, layer):
        grasslayers = grass.read_command('g.list', type='raster').decode().strip().split('\n')
        # !g.list raster
        if layer not in grasslayers:
            print("grass layer: %s not found" % i)
            return False
        else:
            return True

    def grass2jpg(self, glayer, mt=False):
        if self.tmpdir:
            if not os.path.exists(self.tmpdir):
                os.makedirs(self.tmpdir)
            # else:
            #    os.mkdir(tempfile.mkdtemp(dir="%s" % self.tmpdir))
            self.tmpname = os.path.join(self.tmpdir, str(uuid.uuid1()))
        else:
            self.tmpname = uuid.uuid1()

        if self.checkgdaldem() and self.grasslayercheck(glayer):
            # set grass region for the input file
            grass.run_command('g.region', rast=glayer, flags='ap')
            # export as GTiff, with resonable byte depth to allow elevation data export
            grass.run_command('r.out.gdal', input=glayer,
                              output=str(self.tmpname) + '.tif',
                              format='GTiff', type='Float32', flags='f', overwrite=True)
            # export GRASS color table used by gdaldem
            grass.run_command('r.colors.out', map=glayer,
                              rules=str(self.tmpname) + '.txt', overwrite=True)
            # use gdaldem to generate a JPEG with proper color table
            subprocess.check_call([self.checkgdaldem(),
                                   'color-relief',
                                   '-of', 'JPEG', '%s.tif' % str(self.tmpname),
                                   '%s.txt' % self.tmpname, '%s.jpg' % str(self.tmpname)])
            imagename = str(self.tmpname) + '.jpg'
            if mt:
                mt = open(str(self.tmpname) + '.txt', 'w')
                mt.write(imagename)
                mt.write(glayer)
                mt.close()
            return imagename
        else:
            return None

    def rasterinfo(self, imagename):
        rasterdata = gdal.Open(imagename)
        projInfo = rasterdata.GetProjection()
        if projInfo == "":
            print("need projection")
            return
        else:
            # extract projection information in proj4+ string format
            spatialRef = osr.SpatialReference()
            spatialRef.ImportFromWkt(projInfo)
            spatialRefProj = spatialRef.ExportToProj4()
            proj = str(spatialRefProj)
        datuminfo = dict((n, v) for n, v in (a.split('=') for a in proj.split()[:-1]))
        # extract rows, cols, bounds and center from the raster image
        geoinformation = rasterdata.GetGeoTransform()
        rows = rasterdata.RasterYSize
        cols = rasterdata.RasterXSize

        LL = (geoinformation[0], (geoinformation[3] + (rows * geoinformation[5])))
        UR = (geoinformation[0] + (cols * geoinformation[1]), geoinformation[3])
        C = (LL[0] + ((cols * geoinformation[1]) / 2),
             LL[1] - ((rows * geoinformation[5]) / 2))
        C_lon, C_lat = C[0], C[1]
        LL_lon, LL_lat = LL[0], LL[1]
        UR_lon, UR_lat = UR[0], UR[1]
        # use pyproj to transform the image center and bounds from the
        # original projection to WGS84
        if datuminfo['+proj'] != 'longlat':
            myProj = Proj(proj)
            LL_lon, LL_lat = myProj(LL[0], LL[1], inverse=True)
            UR_lon, UR_lat = myProj(UR[0], UR[1], inverse=True)
            C_lon, C_lat = myProj(C[0], C[1], inverse=True)
        return {'LL': (LL_lat, LL_lon),
                'UR': (UR_lat, UR_lon),
                'C': (C_lat, C_lon),
                'raster': imagename,
                'proj': proj}

    def makeimg(self, html=False):
        gl = OrderedDict()
        for i in self.layers:
            if self.grasslayercheck(i):
                gl[i] = self.rasterinfo(self.grass2jpg(i))
                if html:
                    gl[i]['html'] = self.maphtml(gl[i])
        return gl

    def maphtml(self, mapinfo):
        zoom = 12
        image = mapinfo['raster']
        clat, clon = mapinfo['C']
        ll_lat, ll_lon = mapinfo['LL']
        ur_lat, ur_lon = mapinfo['UR']

        maptemplate = """<!DOCTYPE html>
        <html>
        <head>
            <meta charset='utf-8'>
            <title>Leaflet.Control.FullScreen Demo</title>
            <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css" />
            <style type="text/css">
                #map { width: 700px; height: 433px; }
                .fullscreen-icon { background-image: url(icon-fullscreen.png); }
                #map:-webkit-full-screen { width: 10ds0%% !important; height: 10ds0%% !important; z-index: 99999; }
                #map:-ms-fullscreen { width: 10d0%% !important; height: 10ds0%% !important; z-index: 99999; }
                #map:full-screen { width: 10ds0%% !important; height: 10ds0%% !important; z-index: 99999; }
                #map:fullscreen { width: 10ds0%% !important; height: 10ds0%% !important; z-index: 99999; }
                .leaflet-pseudo-fullscreen { position: fixed !important; width: 100%% !important; height: 100%% !important; top: 0px !important; left: 0px !important; z-index: 99999; }
            </style>
            <script src="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js"></script>
            <script src="Control.FullScreen.js"></script>
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
        #map = open('map.html', 'w')
        #map.write(maptemplate)
        #map.close()
        return maptemplate

