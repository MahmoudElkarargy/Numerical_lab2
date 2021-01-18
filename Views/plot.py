import numpy
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication

class Ui_SecondWindow(object):

    maxIterations = 0
    def __init__(self, maxIterations):
        self.maxIterations = maxIterations

    def setupUi(self, MainWindow):
        MainWindow.graphWidget = pg.PlotWidget()
        MainWindow.setCentralWidget(MainWindow.graphWidget)
        content = numpy.loadtxt('values.txt')
        content = numpy.transpose(content)
        print(content)
        # self.iteration = j
        iterations = [i + 1 for i in range(self.maxIterations)]
        #Add Background colour to white
        MainWindow.graphWidget.setBackground('w')
        # Add Title
        MainWindow.graphWidget.setTitle("variables with iterations", color="b", size="20pt")
        # Add Axis Labels
        styles = {"color": "#00f", "font-size": "30px"}
        MainWindow.graphWidget.setLabel("left", "values", **styles)
        MainWindow.graphWidget.setLabel("bottom", "iterations", **styles)
        #Add legend
        MainWindow.graphWidget.addLegend()
        #Add grid
        MainWindow.graphWidget.showGrid(x=True, y=True)
        #Set Range
        MainWindow.graphWidget.setXRange(0, self.maxIterations, padding=0)
        MainWindow.graphWidget.setYRange(-10, 10, padding=0)

        for i in range(content.shape[0]):
            self.plot(MainWindow, iterations, list(content[i]),"iterations of variable "+str(i), 'r')

    def plot(self, MainWindow ,x, y, plotname, color):
        pen = pg.mkPen(color=color)
        MainWindow.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='o', symbolSize=10, symbolBrush=(color))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    graph = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(graph)
    graph.show()
    sys.exit(app.exec_())