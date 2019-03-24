import matplotlib.pyplot as pl
import numpy as np
from matplotlib.collections import LineCollection

def draw_graph(xy,edges,edgecolor='b'):
    lcol = xy[edges]
    lc = LineCollection(xy[edges])
    lc.set_linewidth(0.1)
    lc.set_color(edgecolor)
    pl.gca().add_collection(lc)
    pl.xlim(xy[:,0].min(), xy[:,0].max())
    pl.ylim(xy[:,1].min(), xy[:,1].max())

def draw_points(xy,parts=None, markersize=10):
    if parts is None:
        pl.plot(xy[:,0], xy[:,1], 'ro', markersize=markersize, clip_on=False)
    else:
        parttypes = np.unique(parts)
        colors = pl.cm.jet(parttypes/float(parttypes.max()))
        for p in parttypes:
            I = np.where(parts == p)[0]
            pl.plot(xy[I,0], xy[I,1], 'o', markersize=markersize, markerfacecolor=colors[p,:3],clip_on=False)
