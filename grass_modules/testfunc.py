import os
import collections
from collections import OrderedDict

os.environ['GISDBASE']="/home/epi"


class DictTable(collections.OrderedDict):
    def _repr_html_(self):
        html = ["<table width=100%>"]
        for key, value in self.items():
            html.append("<tr>")
            html.append("<td>{0}</td>".format(key))
            html.append("<td>{0}</td>".format(value))
            html.append("</tr>")
        html.append("</table>")
        return ''.join(html)


def listloc():
    return DictTable(
        OrderedDict((i,
                     sorted(
                         [k for k in str(os.listdir(os.path.join(os.environ['GISDBASE'],
                                                                 i))).replace('[',
                                                                              '').replace(']',
                                                                                          '').replace("'",
                                                                                                      "").split(", ") ])
                     ) for i in sorted(os.listdir(os.environ['GISDBASE']))))

#print(listloc())

#os.listdir(os.environ['GISDBASE'])

#for i in sorted(os.listdir(os.environ['GISDBASE'])):
#    print(i)


def listloc():
    return DictTable(
        OrderedDict((i,
                     sorted(
                         [k for k in str(os.listdir(os.path.join(os.environ['GISDBASE'],
                                                                 i)))])
                     ) for i in sorted(os.listdir(os.environ['GISDBASE']))))

#print(listloc())

def listloc2(self):
    locdict = OrderedDict()
    for i in sorted(os.listdir(os.environ['GISDBASE'])):
        if os.path.isdir(os.path.join(os.environ['GISDBASE'], i)):
            if 'PERMANENT' in os.listdir(os.path.join(os.environ['GISDBASE'], i)):
                locdict[i] = sorted([k for k in str(os.listdir(os.path.join(os.environ['GISDBASE'],
                                                             i))).replace('[',
                                                                          '').replace(']',
                                                                                      '').replace("'",
                                                                                                  "").split(", ")])
    return DictTable(locdict)

#os.path.join(os.environ['GISDBASE'], sorted(os.listdir(os.environ['GISDBASE'])))

