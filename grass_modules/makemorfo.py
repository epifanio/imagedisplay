import sys
sys.path.append('/usr/local/grass-7.3.svn/etc/python')
import grass.script as grass
from grass.script import array as garray
from spectral import *
import spectral.io.envi as envi
spectral.settings.show_progress = False
from grassutil import General, Raster, Imagery

g = General()
r = Raster()
i = Imagery()

class Morphometry:

    def makemorpho(self, inputs, nnwin=9, pmwin=15, resolution=None, overwrite=True, remove=False):
        r_elevation = inputs
        if resolution is not None:
            grass.run_command('g.region', rast=r_elevation, flags='ap')
        else:
            grass.run_command('g.region', rast=r_elevation, res=resolution, flags='ap')
        suffix = str(r_elevation) + '_'
        xavg = suffix + 'avg'
        xmin = suffix + 'min'
        xmax = suffix + 'max'
        xslope = suffix + 'slope'
        xprofc = suffix + 'profc'
        xcrosc = suffix + 'crosc'
        xminic = suffix + 'minic'
        xmaxic = suffix + 'maxic'
        xlongc = suffix + 'longc'
        xer = suffix + 'er'
        img = [suffix + 'avg',
               suffix + 'min',
               suffix + 'max',
               suffix + 'er',
               suffix + 'slope',
               suffix + 'profc',
               suffix + 'crosc',
               suffix + 'minic',
               suffix + 'maxic',
               suffix + 'longc']
        if remove is True:
            rast = '%s,%s,%s,%s,%s,%s,%s,%s,%s' % (xavg, xmin, xmax, xslope, xprofc, xcrosc, xminic, xmaxic, xlongc)
            grass.run_command('g.remove', type='rast', name=rast, flags='f')
        else:
            grass.run_command('r.neighbors',
                              input=r_elevation,
                              output=xavg,
                              size=nnwin,
                              method='average',
                              overwrite=overwrite)
            print("average done")
            grass.run_command('r.neighbors',
                              input=r_elevation,
                              output=xmin,
                              size=nnwin,
                              method='minimum',
                              overwrite=overwrite)
            print("minimum done")
            grass.run_command('r.neighbors',
                              input=r_elevation,
                              output=xmax,
                              size=nnwin,
                              method='maximum',
                              overwrite=overwrite)
            print("maximum done")
            grass.run_command('r.mapcalc',
                              expression='%s = 1.0 * (%s - %s)/(%s - %s)' % (xer, xavg, xmin, xmax, xmin),
                              overwrite=True)
            # !r.fillnulls input={xer} output={xer} --o --q
            print("er done")

            grass.run_command('r.param.scale',
                              input=r_elevation,
                              output=xslope,
                              size=pmwin,
                              slope_tolerance=0.1,
                              curvature_tolerance=0.0001,
                              method='slope',
                              exponent=0.0,
                              zscale=1.0,
                              overwrite=True)
            print("slope done")
            grass.run_command('r.param.scale',
                              input=r_elevation,
                              output=xprofc,
                              size=pmwin,
                              slope_tolerance=0.1,
                              curvature_tolerance=0.0001,
                              method='profc',
                              exponent=0.0,
                              zscale=1.0,
                              overwrite=True)
            print("profc done")
            grass.run_command('r.param.scale',
                              input=r_elevation,
                              output=xcrosc,
                              size=pmwin,
                              slope_tolerance=0.1,
                              curvature_tolerance=0.0001,
                              method='crosc',
                              exponent=0.0,
                              zscale=1.0,
                              overwrite=True)
            print("crosc done")
            grass.run_command('r.param.scale',
                              input=r_elevation,
                              output=xminic,
                              size=pmwin,
                              slope_tolerance=0.1,
                              curvature_tolerance=0.0001,
                              method='minic',
                              exponent=0.0,
                              zscale=1.0,
                              overwrite=True)
            print("minic done")
            grass.run_command('r.param.scale',
                              input=r_elevation,
                              output=xmaxic,
                              size=pmwin,
                              slope_tolerance=0.1,
                              curvature_tolerance=0.0001,
                              method='maxic',
                              exponent=0.0,
                              zscale=1.0,
                              overwrite=True)
            print("maxic done")
            grass.run_command('r.param.scale',
                              input=r_elevation,
                              output=xlongc,
                              size=pmwin,
                              slope_tolerance=0.1,
                              curvature_tolerance=0.0001,
                              method='longc',
                              exponent=0.0,
                              zscale=1.0,
                              overwrite=True)
            print("longc done")
            vrange = grass.read_command('r.info',
                                        map=xslope,
                                        flags='r')
            if sys.version_info.major >= 3:
                vrange = vrange.decode()
            vmin = vrange.strip().split('\n')[0].split('=')[1]
            vmax = vrange.strip().split('\n')[1].split('=')[1]
            grass.run_command('r.mapcalc',
                              expression='%s = (%s/%s)' % (xslope, xslope, vmax),
                              overwrite=True)
            print("xslope done")
        return img


    def writegarray(self, m, mapname):
        clust = garray.array()
        clust[...] = m
        grass.run_command('g.remove',
                          type='raster',
                          name=mapname)
        clust.write(mapname)
        print("newmap: %s, written to GRASS MAPSET" % mapname)


    def getkmeans(self, imagegroup='', k=5, samps=150, bands="all", outputmap=''):
        if bands == "all":
            (m1, c1) = kmeans(imagegroup[:, :, :], k, samps)
        if bands != "all":
            (m1, c1) = kmeans(imagegroup[:, :, range(0, bands)], k, samps)
        self.writegarray(m=m1, mapname=outputmap)
        return (m1, c1)

    def group(self, maplist, group, subgroup):
        if group in General().glist(type='group'):
            print("group %s already present" % group)
            return
        if General().grasslayerscheck(maplist):
            imagegroup = ','.join(i for i in maplist)
            grass.run_command('i.group',
                                group=group,
                                subgroup=subgroup,
                                input=maplist)
        else:
            print('not all the maps were found')
            return

    def cluster(self, group, subgroup, signaturefile, classes, min_size, iterations, reportfile, overwrite):
        if not subgroup:
            subgroup = group
        if not overwrite:
            overwrite = False
        try:
            grass.run_command('i.cluster',
                                group=group,
                                subgroup=subgroup,
                                signaturefile=signaturefile,
                                classes=classes,
                                min_size=min_size,
                                iterations=iterations,
                                reportfile=reportfile,
                                overwrite=overwrite)
        except:
            print('check if the signature and/or the reportfile file already exist')

    def maxlik(self, group, subgroup, signaturefile, output, reject, overwrite):
        if not overwrite:
            overwrite = False
        grass.run_command('i.maxlik',
                            group=group,
                            subgroup=subgroup,
                            signaturefile=signaturefile,
                            output=output,
                            reject=reject,
                            overwrite=overwrite)


        # !r.geomorphon elevation=bathyMSL_filled forms=bathyMSL_filled_forms dist=0.1 skip=0.8 --o

