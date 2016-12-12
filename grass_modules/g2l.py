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

from ipyleaflet import (
    Map,
    Marker,
    TileLayer, ImageOverlay,
    Polyline, Polygon, Rectangle, Circle, CircleMarker,
    GeoJSON,
    DrawControl
)

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

    def grass2jpg(self, glayer):
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

    def makeimg(self):
        gl = OrderedDict()
        for i in self.layers:
            if self.grasslayercheck(i):
                gl[i] = self.rasterinfo(self.grass2jpg(i))
        return gl


def handle_draw(self, action, geo_json):
    print(action)
    print(geo_json)


class Grass2Leaflet(object):
    def __init__(self, grassimg):
        self.grassimg = grassimg
        self.draw_control = None
        self.zoom = 15
        self.center = self.centermap()
        self.m = Map(default_tiles=TileLayer(opacity=1.0), center=self.center, zoom=self.zoom)

    def centermap(self):
        centerlat = []
        centerlon = []
        for i in self.grassimg:
            centerlat.append(self.grassimg[i]['C'][0])
            centerlon.append(self.grassimg[i]['C'][1])
        center = (sum(centerlat) / float(len(centerlat)), sum(centerlon) / float(len(centerlon)))
        return center

    def imgoverlays(self):
        self.leafletimg = OrderedDict()
        for i in self.grassimg:
            layer = ImageOverlay(url=self.grassimg[i]['raster'],
                                 bounds=(self.grassimg[i]['LL'], self.grassimg[i]['UR']))
            self.leafletimg[i] = layer

    def render(self, draw_control=None):
        self.imgoverlays()
        self.dc = None
        options = ['None']
        self.m.add_layer(self.leafletimg[list(self.grassimg.keys())[-1]])
        if len(self.grassimg) >= 2:
            self.maplist = widgets.Dropdown(
                options=options + list(self.grassimg.keys()),
                value=list(self.grassimg.keys())[-1],
                description='Select Layer:',
            )
            self.maplist.observe(self.on_value_change, names='value')
            display(self.maplist)
        if draw_control:
            self.dc = DrawControl()
            self.dc.on_draw(handle_draw)
            self.m.add_control(self.dc)
        display(self.m)
        return {'map': self.m, 'drawer': self.dc}

    def on_value_change(self, layername):
        self.m.clear_layers()
        self.m.add_layer(TileLayer(opacity=1.0))
        if self.maplist.value != 'None':
            self.m.add_layer(self.leafletimg[layername['new']])

    def main(self):
        self.imgoverlays()
        self.render()
