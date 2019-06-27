import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np

from pyqtgraph.Qt import QtGui

# OPENGL 3D PLOT WIDGET
class OL_3D_Plot(QtGui.QWidget):
    def __init__(self, parent=None):
        super(OL_3D_Plot, self).__init__()
        print("OL_3D_PLOT HERE")
        layout = QtGui.QHBoxLayout()

        self.plot = gl.GLViewWidget()
        self.plot.opts['distance'] = 1500
        self.plot.setWindowTitle('3-Dimensional Plot')
        # create the background grids
        gx = gl.GLGridItem(color = 'k')
        gx.rotate(90, 0, 1, 0)
        gy = gl.GLGridItem()
        gy.rotate(90, 1, 0, 0)
        gz = gl.GLGridItem()
        gx.scale(5, 5, 5)
        gy.scale(5, 5, 5)
        gz.scale(5, 5, 5)
        self.plot.addItem(gx)
        self.plot.addItem(gy)
        self.plot.addItem(gz)

        v0_xArray = []
        v0_yArray = []
        v0_zArray = []

        plot_xyz = np.vstack([v0_xArray, v0_yArray, v0_zArray]).transpose()

        self.trace_red = gl.GLLinePlotItem(pos=plot_xyz, color = pg.glColor(244, 66, 66), antialias = True)
        self.trace_blue = gl.GLLinePlotItem(pos=plot_xyz, color=pg.glColor(66, 100, 244), antialias= True)
        self.trace_green = gl.GLLinePlotItem(pos=plot_xyz, color=pg.glColor(66, 244, 104), antialias= True)
        self.trace_yellow = gl.GLLinePlotItem(pos=plot_xyz, color=pg.glColor(244, 244, 66), antialias= True)
        self.plot.addItem(self.trace_red)
        self.plot.addItem(self.trace_blue)
        self.plot.addItem(self.trace_green)
        self.plot.addItem(self.trace_yellow)

        #self.plot.setBackgroundColor('w')
        layout.addWidget(self.plot)
        self.setLayout(layout)