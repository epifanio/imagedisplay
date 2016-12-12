#!/usr/bin/env python

############################################################################
#
# MODULE:      r.clustery.py
# AUTHOR(S):   Margherita Di Leo, Massimo Di Stefano
# PURPOSE:     Morphometric characterization of river basins
# COPYRIGHT:   (C) 2010 by the GRASS Development Team
#
#              This program is free software under the GNU General Public
#              License (>=v2). Read the file COPYING that comes with GRASS
#              for details.
#
#############################################################################

#%module
#% description: 
#% keywords: raster
#%end
#%option
#% key: map
#% type: string
#% gisprompt: old,raster,raster
#% key_desc: name
#% description: Name of elevation raster map 
#% required: yes
#%end
#%option
#% key: output
#% type: string
#% gisprompt: new,file,file
#% key_desc: output 
#% description: output name (must start with a letter)
#% required: yes
#%end
#%option
#% key: cluster
#% type: integer
#% key_desc: cluster
#% description: number of desired cluster 
#% required : yes
#%end
#%option
#% key: psize
#% type: integer
#% key_desc: psize
#% description: size of param scale mobile window
#% required : yes
#%end
#%option
#% key: ssize
#% type: integer
#% key_desc: ssize
#% description: size of kmeans samples
#% required : yes
#%end
#%option
#% key: snumber
#% type: integer
#% key_desc: snumber
#% description: number of kmeans samples
#% required : yes
#%end
#%option
#% key: resolution
#% type: integer
#% key_desc: resolution
#% description: resolution for the working region 
#% required : yes
#%end

import sys
import os
import grass.script as grass
from dtm_clust import makemorfo

def main():
    dtm = options['map'].split('@')[0] 
    output = options['output']
    cluster = int(options['cluster'])
    psize = int(options['psize'])
    ssize = int(options['ssize'])
    snumber = int(options['snumber'])
    resolution = float(options['resolution'])
    makemorfo(dtm,psize,cluster,ssize,snumber,output,resolution)
    #grass.run_command('r.in.gdal' , input = output, flags = 'oe', output = output)
    
if __name__ == "__main__":
    options, flags = grass.parser()
    sys.exit(main())