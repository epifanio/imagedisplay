import grass.script as grass
import rpy2.robjects as robjects
import rpy2.rinterface as rinterface

def makemorfo(input,pswin,nclass,ssamp,nsamp,outimg, resolution):
    s_tol_p = 0.1
    c_tol_p = 0.0001
    exp_p = 0.0
    zscale_p = 1.0
    r_elevation = input
    grass.run_command('g.region', rast = r_elevation, flags = 'ap', res = resolution)
    grass.run_command('r.neighbors', input = r_elevation, output = 'xavg', size = pswin, method = 'average', flags='-o')
    grass.run_command('r.neighbors', input = r_elevation, output = 'xmin', size = pswin, method = 'minimum', flags='-o')
    grass.run_command('r.neighbors', input = r_elevation, output = 'xmax', size = pswin, method = 'maximum', flags='-o')
    grass.run_command('r.mapcalculator' , formula = '1.0 * (%s - %s)/(%s - %s)' % ('xavg', 'xmin', 'xmax', 'xmin') , outfile = 'xer', flags = '-o')
    grass.run_command('r.param.scale', input = r_elevation, output = 'xslope', size = pswin, s_tol = 0.1, c_tol = c_tol_p, param = 'slope', exp = exp_p, zscale = zscale_p, flags = '-o') 
    grass.run_command('r.param.scale', input = r_elevation, output = 'xprofc', size = pswin, s_tol = 0.1, c_tol = c_tol_p, param = 'profc', exp = exp_p, zscale = zscale_p, flags = '-o') 
    grass.run_command('r.param.scale', input = r_elevation, output = 'xcrosc', size = pswin, s_tol = 0.1, c_tol = c_tol_p, param = 'crosc', exp = exp_p, zscale = zscale_p, flags = '-o') 
    grass.run_command('r.param.scale', input = r_elevation, output = 'xminic', size = pswin, s_tol = 0.1, c_tol = c_tol_p, param = 'minic', exp = exp_p, zscale = zscale_p, flags = '-o') 
    grass.run_command('r.param.scale', input = r_elevation, output = 'xmaxic', size = pswin, s_tol = 0.1, c_tol = c_tol_p, param = 'maxic', exp = exp_p, zscale = zscale_p, flags = '-o') 
    grass.run_command('r.param.scale', input = r_elevation, output = 'xlongc', size = pswin, s_tol = 0.1, c_tol = c_tol_p, param = 'longc', exp = exp_p, zscale = zscale_p, flags = '-o') 
    vrange = grass.read_command('r.info', map='xslope', flags='r').strip().split('\n')
    vmin = vrange[0].split('=')[1]
    vmax = vrange[1].split('=')[1]
    grass.run_command('r.mapcalculator' , formula = '(%s/%s)' % ('xslope', vmax) , outfile = 'xslope', flags = '-o')
    robjects.r.require('morfoclara')
    files = robjects.r.c("xer","xcrosc","xlongc","xslope","xprofc","xminic","xmaxic")
    clustering = robjects.r.morfoclara(files,nclass,ssamp,nsamp,outimg)


