import os
import cherrypy

cherrypy.config.update({'server.socket_port': 8099})
cherrypy.engine.restart()

PATH = os.path.abspath(os.path.dirname(__file__))
class Root(object): pass

cherrypy.tree.mount(Root(), '2d/', config={
        '2d/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': PATH,
                'tools.staticdir.index': 'index.html',
                'server.socket_port': 8099,
            },
    })

cherrypy.quickstart()