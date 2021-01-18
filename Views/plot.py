import numpy
from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.iteration = 50
        iterations = [i+1 for i in range(self.iteration)]
        content = numpy.loadtxt('values.txt')
        content = numpy.transpose(content)
        print(content)
        # self.iteration = j
        iterations = [i + 1 for i in range(self.iteration)]
        #Add Background colour to white
        self.graphWidget.setBackground('w')
        # Add Title
        self.graphWidget.setTitle("variables with iterations", color="b", size="20pt")
        # Add Axis Labels
        styles = {"color": "#00f", "font-size": "30px"}
        self.graphWidget.setLabel("left", "values", **styles)
        self.graphWidget.setLabel("bottom", "iterations", **styles)
        #Add legend
        self.graphWidget.addLegend()
        #Add grid
        self.graphWidget.showGrid(x=True, y=True)
        #Set Range
        self.graphWidget.setXRange(0, self.iteration, padding=0)
        self.graphWidget.setYRange(-10, 10, padding=0)

        for i in range(content.shape[0]):
            self.plot(iterations, list(content[i]),"iterations of variable "+str(i), 'r')

    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='o', symbolSize=10, symbolBrush=(color))

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()