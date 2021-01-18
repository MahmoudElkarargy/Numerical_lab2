# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from Methods.GaussianElimination import mainFunc
from Methods.GaussianJordan import JordonMainFun
from Methods.LUDecomposition import LUMainFun
from Methods.GaussSeidel import SeidalMainFun

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(990, 620)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 40)")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(230, 20, 501, 60))
        self.label.setStyleSheet("background: transparent;\n"
"color: rgb(166, 203, 255);\n"
"margin: 5px;\n"
"font-size: 38px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 131, 31))
        self.label_2.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 24px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox.setGeometry(QtCore.QRect(250, 100, 211, 31))
        self.checkBox.setStyleSheet("outline: none;\n"
"background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.checkBox.setObjectName("checkBox")
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(40, 120, 119, 2))
        self.line.setStyleSheet("background-color:  rgb(234, 255, 253);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 140, 451, 461))
        self.groupBox.setStyleSheet("background-color: rgba(152, 189, 255, 10);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 221, 31))
        self.label_4.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"font-size: 18px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.label_4.setObjectName("label_4")
        self.nbOfVariables = QtWidgets.QSpinBox(self.groupBox)
        self.nbOfVariables.setGeometry(QtCore.QRect(250, 10, 31, 41))
        self.nbOfVariables.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;;\n"
"background: transparent;\n"
"font-size: 18px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"text-align: center;\n"
"")
        self.nbOfVariables.setMinimum(2)
        self.nbOfVariables.setMaximum(9)
        self.nbOfVariables.setProperty("value", 9)
        self.nbOfVariables.setObjectName("nbOfVariables")
        self.errorMsg = QtWidgets.QLabel(self.groupBox)
        self.errorMsg.setGeometry(QtCore.QRect(20, 60, 411, 31))
        self.errorMsg.setStyleSheet("background: transparent;\n"
"color:rgb(252, 1, 7);\n"
"font-size: 18px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.errorMsg.setObjectName("errorMsg")
        self.labelEqu1 = QtWidgets.QLabel(self.groupBox)
        self.labelEqu1.setGeometry(QtCore.QRect(20, 90, 151, 31))
        self.labelEqu1.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.labelEqu1.setObjectName("labelEqu1")
        self.lineEditEQ1 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEQ1.setGeometry(QtCore.QRect(190, 90, 241, 21))
        self.lineEditEQ1.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 12px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.lineEditEQ1.setText("")
        self.lineEditEQ1.setObjectName("lineEditEQ1")
        self.labelEqu2 = QtWidgets.QLabel(self.groupBox)
        self.labelEqu2.setGeometry(QtCore.QRect(20, 130, 161, 31))
        self.labelEqu2.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.labelEqu2.setObjectName("labelEqu2")
        self.labelEqu3 = QtWidgets.QLabel(self.groupBox)
        self.labelEqu3.setGeometry(QtCore.QRect(20, 170, 151, 31))
        self.labelEqu3.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.labelEqu3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.labelEqu3.setObjectName("labelEqu3")
        self.labelEqu4 = QtWidgets.QLabel(self.groupBox)
        self.labelEqu4.setGeometry(QtCore.QRect(20, 210, 151, 31))
        self.labelEqu4.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.labelEqu4.setObjectName("labelEqu4")
        self.labelEqu5 = QtWidgets.QLabel(self.groupBox)
        self.labelEqu5.setGeometry(QtCore.QRect(20, 250, 151, 31))
        self.labelEqu5.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.labelEqu5.setObjectName("labelEqu5")
        self.labelEqu6 = QtWidgets.QLabel(self.groupBox)
        self.labelEqu6.setGeometry(QtCore.QRect(20, 290, 151, 31))
        self.labelEqu6.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.labelEqu6.setObjectName("labelEqu6")
        self.labelEqu7 = QtWidgets.QLabel(self.groupBox)
        self.labelEqu7.setGeometry(QtCore.QRect(20, 330, 161, 31))
        self.labelEqu7.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.labelEqu7.setObjectName("labelEqu7")
        self.labelEqu8 = QtWidgets.QLabel(self.groupBox)
        self.labelEqu8.setGeometry(QtCore.QRect(20, 370, 151, 31))
        self.labelEqu8.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.labelEqu8.setObjectName("labelEqu8")
        self.lineEditEQ3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEQ3.setGeometry(QtCore.QRect(190, 170, 241, 21))
        self.lineEditEQ3.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 12px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.lineEditEQ3.setObjectName("lineEditEQ3")
        self.lineEditEQ4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEQ4.setGeometry(QtCore.QRect(190, 210, 241, 21))
        self.lineEditEQ4.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 12px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.lineEditEQ4.setObjectName("lineEditEQ4")
        self.lineEditEQ5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEQ5.setGeometry(QtCore.QRect(190, 250, 241, 21))
        self.lineEditEQ5.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 12px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.lineEditEQ5.setObjectName("lineEditEQ5")
        self.lineEditEQ6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEQ6.setGeometry(QtCore.QRect(190, 290, 241, 21))
        self.lineEditEQ6.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 12px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.lineEditEQ6.setObjectName("lineEditEQ6")
        self.lineEditEQ7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEQ7.setGeometry(QtCore.QRect(190, 330, 241, 21))
        self.lineEditEQ7.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 12px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.lineEditEQ7.setObjectName("lineEditEQ7")
        self.lineEditEQ8 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEQ8.setGeometry(QtCore.QRect(190, 370, 241, 21))
        self.lineEditEQ8.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 12px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.lineEditEQ8.setObjectName("lineEditEQ8")
        self.lineEditEQ2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEQ2.setGeometry(QtCore.QRect(190, 130, 241, 21))
        self.lineEditEQ2.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 12px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.lineEditEQ2.setText("")
        self.lineEditEQ2.setObjectName("lineEditEQ2")
        self.labelEqu9 = QtWidgets.QLabel(self.groupBox)
        self.labelEqu9.setGeometry(QtCore.QRect(20, 410, 151, 31))
        self.labelEqu9.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.labelEqu9.setObjectName("labelEqu9")
        self.lineEditEQ9 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEQ9.setGeometry(QtCore.QRect(190, 410, 241, 21))
        self.lineEditEQ9.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 12px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.lineEditEQ9.setObjectName("lineEditEQ9")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(520, 90, 161, 31))
        self.label_7.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 24px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.label_7.setObjectName("label_7")
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setGeometry(QtCore.QRect(530, 120, 149, 2))
        self.line_2.setStyleSheet("background-color:  rgb(234, 255, 253);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.parametersGroup = QtWidgets.QGroupBox(self.centralWidget)
        self.parametersGroup.setGeometry(QtCore.QRect(530, 140, 421, 51))
        self.parametersGroup.setStyleSheet("background-color: rgba(152, 189, 255, 10);")
        self.parametersGroup.setTitle("")
        self.parametersGroup.setObjectName("parametersGroup")
        self.label_5 = QtWidgets.QLabel(self.parametersGroup)
        self.label_5.setGeometry(QtCore.QRect(0, 10, 151, 31))
        self.label_5.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.label_5.setObjectName("label_5")
        self.maxIterations = QtWidgets.QSpinBox(self.parametersGroup)
        self.maxIterations.setGeometry(QtCore.QRect(160, 0, 41, 41))
        self.maxIterations.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.maxIterations.setMinimum(5)
        self.maxIterations.setMaximum(100000000)
        self.maxIterations.setProperty("value", 50)
        self.maxIterations.setObjectName("maxIterations")
        self.label_6 = QtWidgets.QLabel(self.parametersGroup)
        self.label_6.setGeometry(QtCore.QRect(210, 10, 91, 31))
        self.label_6.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.label_6.setObjectName("label_6")
        self.Epsilon = QtWidgets.QDoubleSpinBox(self.parametersGroup)
        self.Epsilon.setGeometry(QtCore.QRect(310, 0, 101, 41))
        self.Epsilon.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"outline: none;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.Epsilon.setDecimals(6)
        self.Epsilon.setMinimum(1e-06)
        self.Epsilon.setMaximum(1.0)
        self.Epsilon.setSingleStep(0.001)
        self.Epsilon.setProperty("value", 1e-05)
        self.Epsilon.setObjectName("Epsilon")
        self.line_3 = QtWidgets.QFrame(self.centralWidget)
        self.line_3.setGeometry(QtCore.QRect(510, 140, 3, 420))
        self.line_3.setStyleSheet("background-color:  rgb(234, 255, 253);")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(520, 200, 111, 31))
        self.label_8.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 22px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.label_8.setObjectName("label_8")
        self.line_4 = QtWidgets.QFrame(self.centralWidget)
        self.line_4.setGeometry(QtCore.QRect(530, 230, 98, 2))
        self.line_4.setStyleSheet("background-color:  rgb(234, 255, 253);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.MethodsGroup = QtWidgets.QGroupBox(self.centralWidget)
        self.MethodsGroup.setGeometry(QtCore.QRect(530, 250, 421, 81))
        self.MethodsGroup.setStyleSheet("background-color: rgba(152, 189, 255, 10);")
        self.MethodsGroup.setTitle("")
        self.MethodsGroup.setObjectName("MethodsGroup")
        self.label_9 = QtWidgets.QLabel(self.MethodsGroup)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.label_9.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.label_9.setObjectName("label_9")
        self.method = QtWidgets.QComboBox(self.MethodsGroup)
        self.method.setGeometry(QtCore.QRect(120, 0, 231, 32))
        self.method.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background-color: rgb(10, 10, 50);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.method.setObjectName("method")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.initialLabel = QtWidgets.QLabel(self.MethodsGroup)
        self.initialLabel.setGeometry(QtCore.QRect(10, 40, 161, 31))
        self.initialLabel.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.initialLabel.setObjectName("initialLabel")
        self.initialPointsInput = QtWidgets.QLineEdit(self.MethodsGroup)
        self.initialPointsInput.setGeometry(QtCore.QRect(180, 40, 221, 21))
        self.initialPointsInput.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 12px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.initialPointsInput.setText("")
        self.initialPointsInput.setObjectName("initialPointsInput")
        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_10.setGeometry(QtCore.QRect(520, 340, 111, 31))
        self.label_10.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 22px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.label_10.setObjectName("label_10")
        self.line_5 = QtWidgets.QFrame(self.centralWidget)
        self.line_5.setGeometry(QtCore.QRect(530, 370, 97, 2))
        self.line_5.setStyleSheet("background-color:  rgb(234, 255, 253);")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(530, 380, 421, 221))
        self.groupBox_2.setStyleSheet("background-color: rgba(152, 189, 255, 10);")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 181, 31))
        self.label_11.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.label_11.setObjectName("label_11")
        self.valuesResult1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.valuesResult1.setGeometry(QtCore.QRect(40, 40, 351, 21))
        self.valuesResult1.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.valuesResult1.setText("")
        self.valuesResult1.setObjectName("valuesResult1")
        self.valuesResult2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.valuesResult2.setGeometry(QtCore.QRect(40, 70, 351, 21))
        self.valuesResult2.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.valuesResult2.setText("")
        self.valuesResult2.setObjectName("valuesResult2")
        self.execTimeLabel = QtWidgets.QLabel(self.groupBox_2)
        self.execTimeLabel.setGeometry(QtCore.QRect(10, 110, 161, 31))
        self.execTimeLabel.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.execTimeLabel.setObjectName("execTimeLabel")
        self.excutionTime = QtWidgets.QLineEdit(self.groupBox_2)
        self.excutionTime.setGeometry(QtCore.QRect(180, 110, 91, 21))
        self.excutionTime.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.excutionTime.setText("")
        self.excutionTime.setObjectName("excutionTime")
        self.SecondsLabel = QtWidgets.QLabel(self.groupBox_2)
        self.SecondsLabel.setGeometry(QtCore.QRect(280, 110, 91, 31))
        self.SecondsLabel.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.SecondsLabel.setObjectName("SecondsLabel")
        self.showIterations = QtWidgets.QPushButton(self.groupBox_2)
        self.showIterations.setGeometry(QtCore.QRect(10, 170, 141, 32))
        self.showIterations.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);\n"
"")
        self.showIterations.setObjectName("showIterations")
        self.calculate = QtWidgets.QPushButton(self.groupBox_2)
        self.calculate.setGeometry(QtCore.QRect(160, 170, 101, 32))
        self.calculate.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);\n"
"")
        self.calculate.setObjectName("calculate")
        self.showGraph = QtWidgets.QPushButton(self.groupBox_2)
        self.showGraph.setGeometry(QtCore.QRect(270, 170, 141, 32))
        self.showGraph.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(0, 0, 40);\n"
"")
        self.showGraph.setObjectName("showGraph")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connection of functions
        self.nbOfVariables.valueChanged.connect(self.setNumberOfEquations)
        self.checkBox.stateChanged.connect(self.readFromFile)
        self.method.currentTextChanged.connect(self.setMethod)
        self.calculate.clicked.connect(self.calculateButtonClicked)

        # Hide unneeded fields.
        self.errorMsg.hide()
        self.excutionTime.hide()
        self.execTimeLabel.hide()
        self.SecondsLabel.hide()
        self.valuesResult2.hide()

    def setMethod(self):
        if (self.method.currentText() == "Gauss-Seidel" or self.method.currentText() == "All"):
            self.initialPointsInput.show()
            self.initialLabel.show()
            self.showGraph.show()
            self.showIterations.show()
        else:
            self.initialLabel.hide()
            self.initialPointsInput.hide()
            self.showIterations.hide()
            self.showGraph.hide()
        self.execTimeLabel.hide()
        self.excutionTime.hide()
        self.SecondsLabel.hide()
        self.valuesResult1.setText("")
        self.valuesResult2.setText("")
        self.errorMsg.setText("")

    def readFromFile(self):
        if (self.checkBox.isChecked()):
            self.groupBox.hide()
            self.parametersGroup.hide()
            self.MethodsGroup.hide()
        else:
            self.groupBox.show()
            self.parametersGroup.show()
            self.MethodsGroup.show()

    def setNumberOfEquations(self):
        numberOfEqu = int(self.nbOfVariables.text())
        self.labelEqu3.hide()
        self.labelEqu4.hide()
        self.labelEqu5.hide()
        self.labelEqu6.hide()
        self.labelEqu7.hide()
        self.labelEqu8.hide()
        self.labelEqu9.hide()
        self.lineEditEQ9.hide()
        self.lineEditEQ3.hide()
        self.lineEditEQ4.hide()
        self.lineEditEQ5.hide()
        self.lineEditEQ6.hide()
        self.lineEditEQ7.hide()
        self.lineEditEQ8.hide()
        self.lineEditEQ9.hide()
        self.valuesResult1.setText("")
        self.valuesResult2.setText("")
        self.execTimeLabel.hide()
        self.excutionTime.hide()
        self.SecondsLabel.hide()
        self.errorMsg.setText("")
        if (numberOfEqu > 2):
            self.labelEqu3.show()
            self.lineEditEQ3.show()
        if (numberOfEqu > 3):
            self.labelEqu4.show()
            self.lineEditEQ4.show()
        if (numberOfEqu > 4):
            self.labelEqu5.show()
            self.lineEditEQ5.show()
        if (numberOfEqu > 5):
            self.labelEqu6.show()
            self.lineEditEQ6.show()
        if (numberOfEqu > 6):
            self.labelEqu7.show()
            self.lineEditEQ7.show()
        if (numberOfEqu > 7):
            self.labelEqu8.show()
            self.lineEditEQ8.show()
        if (numberOfEqu > 8):
            self.labelEqu9.show()
            self.lineEditEQ9.show()

    def search(self, listt, platform):
        for i in range(len(listt)):
            if listt[i] == platform:
                return True
        return False

    def calculateButtonClicked(self):
        redStyle = 'background: transparent; color:rgb(252, 1, 7);font-size: 14px;font-family: "Lucida Console", "Courier New", monospace;'
        greenStyle = 'background: transparent; color:lightgreen;font-size: 14px;font-family: "Lucida Console", "Courier New", monospace;'
        self.errorMsg.show()
        if not self.checkBox.isChecked():
                numberOfVariables = int(self.nbOfVariables.text())
                if (self.lineEditEQ1.text() == "" or self.lineEditEQ2.text() == "" or
                        (self.lineEditEQ3.text() == "" and numberOfVariables > 2) or
                        (self.lineEditEQ4.text() == "" and numberOfVariables > 3) or
                        (self.lineEditEQ5.text() == "" and numberOfVariables > 4) or
                        (self.lineEditEQ6.text() == "" and numberOfVariables > 5) or
                        (self.lineEditEQ7.text() == "" and numberOfVariables > 6) or
                        (self.lineEditEQ8.text() == "" and numberOfVariables > 7) or
                        (self.lineEditEQ9.text() == "" and numberOfVariables > 8)
                ):
                    self.errorMsg.setStyleSheet(redStyle)
                    self.errorMsg.setText("PLEASE FILL ALL THE EQUATIONS!")
                else:
                    self.errorMsg.setStyleSheet(greenStyle)
                    self.errorMsg.setText("CALCULATING ....")
                    method = self.method.currentText()

                    # Get Equations..
                    # Handle spaces in equation
                    firstEq = self.lineEditEQ1.text()
                    firstEq = firstEq.replace(" ", "")
                    firstEq = firstEq.lower()
                    # Getting the variables in the first eq..
                    varr = []
                    for char in firstEq:
                        if (char.isalpha()):
                            print(char)
                            varr.append(char)
                    # Getting the second eq and handle spaces.
                    secondEq = self.lineEditEQ2.text()
                    secondEq = secondEq.replace(" ", "")
                    secondEq = secondEq.lower()
                    i = 0
                    # Check if still the variables entered is less than the nb of varaibles
                    while (len(varr) != numberOfVariables and i < len(secondEq)):
                        # Make sure this var is not added before.
                        if (secondEq[i].isalpha() and not (self.search(varr, secondEq[i]))):
                            varr.append(secondEq[i])
                        i += 1
                    fullEquation = firstEq + "," + secondEq
                    if (numberOfVariables > 2):
                        # Getting the third eq and handle spaces.
                        thirdEq = self.lineEditEQ3.text()
                        thirdEq = thirdEq.replace(" ", "")
                        thirdEq = thirdEq.lower()
                        i = 0
                        # Check if still the variables entered is less than the nb of varaibles
                        while (len(varr) != numberOfVariables and i < len(thirdEq)):
                            # Make sure this var is not added before.
                            if (thirdEq[i].isalpha() and not (self.search(varr, thirdEq[i]))):
                                varr.append(thirdEq[i])
                            i += 1
                        fullEquation += "," + thirdEq

                    if (numberOfVariables > 3):
                        # Getting the third eq and handle spaces.
                        forthEq = self.lineEditEQ4.text()
                        forthEq = forthEq.replace(" ", "")
                        forthEq = forthEq.lower()
                        i = 0
                        # Check if still the variables entered is less than the nb of varaibles
                        while (len(varr) != numberOfVariables and i < len(forthEq)):
                            # Make sure this var is not added before.
                            if (forthEq[i].isalpha() and not (self.search(varr, forthEq[i]))):
                                varr.append(forthEq[i])
                            i += 1
                        fullEquation += "," + forthEq

                    if (numberOfVariables > 4):
                        # Getting the third eq and handle spaces.
                        fifthEq = self.lineEditEQ5.text()
                        fifthEq = fifthEq.replace(" ", "")
                        fifthEq = fifthEq.lower()
                        i = 0
                        # Check if still the variables entered is less than the nb of varaibles
                        while (len(varr) != numberOfVariables and i < len(fifthEq)):
                            # Make sure this var is not added before.
                            if (fifthEq[i].isalpha() and not (self.search(varr, fifthEq[i]))):
                                varr.append(fifthEq[i])
                            i += 1
                        fullEquation += "," + fifthEq

                    if (numberOfVariables > 5):
                        # Getting the third eq and handle spaces.
                        sixthEq = self.lineEditEQ6.text()
                        sixthEq = sixthEq.replace(" ", "")
                        sixthEq = sixthEq.lower()
                        i = 0
                        # Check if still the variables entered is less than the nb of varaibles
                        while (len(varr) != numberOfVariables and i < len(sixthEq)):
                            # Make sure this var is not added before.
                            if (sixthEq[i].isalpha() and not (self.search(varr, sixthEq[i]))):
                                varr.append(sixthEq[i])
                            i += 1
                        fullEquation += "," + sixthEq

                    if (numberOfVariables > 6):
                        # Getting the third eq and handle spaces.
                        seventhEq = self.lineEditEQ7.text()
                        seventhEq = seventhEq.replace(" ", "")
                        seventhEq = seventhEq.lower()
                        i = 0
                        # Check if still the variables entered is less than the nb of varaibles
                        while (len(varr) != numberOfVariables and i < len(seventhEq)):
                            # Make sure this var is not added before.
                            if (seventhEq[i].isalpha() and not (self.search(varr, seventhEq[i]))):
                                varr.append(seventhEq[i])
                            i += 1
                        fullEquation += "," + seventhEq

                    if (numberOfVariables > 7):
                        # Getting the third eq and handle spaces.
                        eigthEq = self.lineEditEQ8.text()
                        eigthEq = eigthEq.replace(" ", "")
                        eigthEq = eigthEq.lower()
                        i = 0
                        # Check if still the variables entered is less than the nb of varaibles
                        while (len(varr) != numberOfVariables and i < len(eigthEq)):
                            # Make sure this var is not added before.
                            if (eigthEq[i].isalpha() and not (self.search(varr, eigthEq[i]))):
                                varr.append(eigthEq[i])
                            i += 1
                        fullEquation += "," + eigthEq

                    if (numberOfVariables > 8):
                        # Getting the third eq and handle spaces.
                        ninthEq = self.lineEditEQ9.text()
                        ninthEq = ninthEq.replace(" ", "")
                        ninthEq = ninthEq.lower()
                        i = 0
                        # Check if still the variables entered is less than the nb of varaibles
                        while (len(varr) != numberOfVariables and i < len(ninthEq)):
                            # Make sure this var is not added before.
                            if (ninthEq[i].isalpha() and not (self.search(varr, ninthEq[i]))):
                                varr.append(ninthEq[i])
                            i += 1
                        fullEquation += "," + ninthEq

                    if (len(varr) != numberOfVariables):
                        self.errorMsg.setStyleSheet(redStyle)
                        self.errorMsg.setText("NUMBERS OF VARIABLES ARE NOT CORRECT!")
                    else:
                        if (numberOfVariables > 4):
                            self.valuesResult2.show()
                        else:
                            self.valuesResult2.hide()
                        print(fullEquation)
                        if (method == "Gaussian-Elimination"):
                            print("Gaussian-Elimination")
                            result = mainFunc(numberOfVariables, fullEquation)
                            if (result == "Error"):
                                self.errorMsg.setStyleSheet(redStyle)
                                self.errorMsg.setText("ERROR!: Functions are incorrect")
                            else:
                                print(result)
                                if (numberOfVariables > 4):
                                    results = result.split(',')
                                    string = ""
                                    for i in range(4):
                                        string += "  " + varr[i].upper() + ": "
                                        string += results[i]
                                    self.valuesResult1.setText(string)
                                    string = ""
                                    for j in range(4, (len(results)-1)):
                                        string += "  " + varr[j].upper() + ": "
                                        string += results[j]
                                    self.valuesResult2.setText(string)
                                else:
                                    results = result.split(',')
                                    string = ""
                                    for i in range(len(results) - 1):
                                        string += "  " + varr[i].upper() + ": "
                                        string += results[i]
                                    self.valuesResult1.setText(string)
                                self.errorMsg.setText("SOLVED USED GAUSSIAN-ELIMINATION")
                                self.execTimeLabel.show()
                                self.excutionTime.show()
                                self.SecondsLabel.show()
                        elif (method == "LU decomposition"):
                            print("LU decomposition")
                            result = LUMainFun(numberOfVariables, fullEquation)
                            print(result)
                            if (numberOfVariables > 4):
                                result = result.tolist()
                                string = ""
                                print(result)
                                for i in range(4):
                                    string += "  " + varr[i].upper() + ": "
                                    string += str(round(result[i], 3))
                                self.valuesResult1.setText(string)
                                string = ""
                                for j in range(4, (len(result))):
                                    string += "  " + varr[j].upper() + ": "
                                    string += str(round(result[j], 3))
                                self.valuesResult2.setText(string)
                            else:
                                result = result.tolist()
                                string = ""
                                for i in range(len(result)):
                                    string += "  " + varr[i].upper() + ": "
                                    string += str(round(result[i], 3))
                                self.valuesResult1.setText(string)
                            self.errorMsg.setText("SOLVED USED LU Decomposition")
                            self.execTimeLabel.show()
                            self.excutionTime.show()
                            self.SecondsLabel.show()
                        elif (method == "Gaussian- Jordan"):
                            print("Gaussian- Jordan")
                            result = JordonMainFun(numberOfVariables, fullEquation)
                            if (result == "Error"):
                                self.errorMsg.setStyleSheet(redStyle)
                                self.errorMsg.setText("ERROR!: Functions are incorrect")
                            else:
                                print(result)
                                if (numberOfVariables > 4):
                                    results = result.split(',')
                                    string = ""
                                    for i in range(4):
                                        string += "  " + varr[i].upper() + ": "
                                        string += results[i]
                                    self.valuesResult1.setText(string)
                                    string = ""
                                    for j in range(4, (len(results) - 1)):
                                        string += "  " + varr[j].upper() + ": "
                                        string += results[j]
                                    self.valuesResult2.setText(string)
                                else:
                                    results = result.split(',')
                                    string = ""
                                    for i in range(len(results) - 1):
                                        string += "  " + varr[i].upper() + ": "
                                        string += results[i]
                                    self.valuesResult1.setText(string)
                                self.errorMsg.setText("SOLVED USED GAUSSIAN-JORDON")
                                self.execTimeLabel.show()
                                self.excutionTime.show()
                                self.SecondsLabel.show()
                        elif (method == "Gauss-Seidel"):
                            print("Gauss-Seidel")
                            init = self.initialPointsInput.text()
                            if(init == ""):
                                self.errorMsg.setStyleSheet(redStyle)
                                self.errorMsg.setText("PLEASE WRITE DOWN THE INITAL POINTS!")
                            else:
                                initList = init.split(' ')
                                if(len(initList) != numberOfVariables):
                                    self.errorMsg.setStyleSheet(redStyle)
                                    self.errorMsg.setText("SOME INITAL POINTS ARE MISSED!")
                                else:
                                    newlist = [float(i) for i in initList]
                                    result = SeidalMainFun(numberOfVariables, fullEquation, int(self.maxIterations.text()),
                                                           float(self.Epsilon.text()), newlist)
                                    result = result.tolist()
                                    string = ""
                                    print(result)
                                    self.valuesResult2.show()
                                    for i in range(2):
                                        string += "  " + varr[i].upper() + ": "
                                        string += str(result[i])
                                    self.valuesResult1.setText(string)
                                    string = ""
                                    for j in range(2, (len(result))):
                                        string += "  " + varr[j].upper() + ": "
                                        string += str(result[j])
                                    self.valuesResult2.setText(string)
                                    self.errorMsg.setText("SOLVED USED LU Decomposition")
                                    self.execTimeLabel.show()
                                    self.excutionTime.show()
                                    self.SecondsLabel.show()
                        else:
                            print("All methods")
        else:
                input_file = open("../Views/input.txt","r")
                if os.path.isfile('../Views/input.txt'):
                        print("File exist")
                else:
                        print("File not exist")
                numberOfVariables = int(input_file.readline().strip("\n"))
                method = input_file.readline().strip("\n")
                fullEquation = input_file.readline().strip("\n")
                varr =[]
                for char in fullEquation:
                        if (char.isalpha()):

                                varr.append(char)
                for i in range(numberOfVariables-1):
                        fullEquation = fullEquation + "," + input_file.readline().strip("\n")
                initial_values = []
                initial_values = input_file.readline().split()
                print(initial_values)

                if method == "Gaussian-elimination":
                        result = mainFunc(numberOfVariables, fullEquation)
                        if (result == "Error"):
                                self.errorMsg.setStyleSheet(redStyle)
                                self.errorMsg.setText("ERROR!: Functions are incorrect")
                        else:
                                print(result)
                                if (numberOfVariables > 4):
                                        results = result.split(',')
                                        string = ""
                                        for i in range(4):
                                                string += "  " + varr[i].upper() + ": "
                                                string += results[i]
                                        self.valuesResult1.setText(string)
                                        string = ""
                                        for j in range(4, (len(results) - 1)):
                                                string += "  " + varr[j].upper() + ": "
                                                string += results[j]
                                        self.valuesResult2.setText(string)
                                else:
                                        results = result.split(',')
                                        string = ""
                                        for i in range(len(results) - 1):
                                                string += "  " + varr[i].upper() + ": "
                                                string += results[i]
                                        self.valuesResult1.setText(string)
                                self.errorMsg.setText("SOLVED USED GAUSSIAN-ELIMINATION")
                                self.execTimeLabel.show()
                                self.excutionTime.show()
                                self.SecondsLabel.show()
                elif method == "Gaussian-jordan":

                        result = JordonMainFun(numberOfVariables, fullEquation)
                        if (numberOfVariables > 4):
                                results = result.split(',')
                                string = ""
                                for i in range(4):
                                        string += "  " + varr[i].upper() + ": "
                                        string += results[i]
                                self.valuesResult1.setText(string)
                                string = ""
                                for j in range(4, (len(results) - 1)):
                                        string += "  " + varr[j].upper() + ": "
                                        string += results[j]
                                        self.valuesResult2.setText(string)
                        else:
                                results = result.split(',')
                                string = ""
                                for i in range(len(results) - 1):
                                        string += "  " + varr[i].upper() + ": "
                                        string += results[i]
                                self.valuesResult1.setText(string)
                        self.errorMsg.setText("SOLVED USED GAUSSIAN-JORDON")
                        self.execTimeLabel.show()
                        self.excutionTime.show()
                        self.SecondsLabel.show()

                elif method == "Gaussian-Seidel":
                        result = SeidalMainFun(numberOfVariables, fullEquation,50,
                                               0.00001, [float(i) for i in initial_values])
                        result = result.tolist()
                        string = ""
                        print(result)
                        self.valuesResult2.show()
                        for i in range(2):
                                string += "  " + varr[i].upper() + ": "
                                string += str(result[i])
                        self.valuesResult1.setText(string)
                        string = ""
                        for j in range(2, (len(result))):
                                string += "  " + varr[j].upper() + ": "
                                string += str(result[j])
                        self.valuesResult2.setText(string)
                        self.errorMsg.setText("SOLVED USED LU Decomposition")
                        self.execTimeLabel.show()
                        self.excutionTime.show()
                        self.SecondsLabel.show()
                elif method == "LU decomposition":
                        print(numberOfVariables)
                        print(fullEquation)
                        result = LUMainFun(numberOfVariables, fullEquation)

                        if (numberOfVariables > 4):
                                result = result.tolist()
                                string = ""
                                print(result)
                                for i in range(4):
                                        string += "  " + varr[i].upper() + ": "
                                        string += str(round(result[i], 3))
                                self.valuesResult1.setText(string)
                                string = ""
                                for j in range(4, (len(result))):
                                        string += "  " + varr[j].upper() + ": "
                                        string += str(round(result[j], 3))
                                self.valuesResult2.setText(string)
                        else:
                                result = result.tolist()
                                string = ""
                                for i in range(len(result)):
                                        string += "  " + varr[i].upper() + ": "
                                        string += str(round(result[i], 3))
                                self.valuesResult1.setText(string)
                        self.errorMsg.setText("SOLVED USED LU Decomposition")
                        self.execTimeLabel.show()
                        self.excutionTime.show()
                        self.SecondsLabel.show()
                else:
                        pass
                #







    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LAB TWO"))
        self.label.setText(_translate("MainWindow", "* Numerical Project *"))
        self.label_2.setText(_translate("MainWindow", "Function"))
        self.checkBox.setText(_translate("MainWindow", "Select from File"))
        self.label_4.setText(_translate("MainWindow", "Number of Variables:"))
        self.errorMsg.setText(_translate("MainWindow", "Error msg."))
        self.labelEqu1.setText(_translate("MainWindow", "First Equation:"))
        self.labelEqu2.setText(_translate("MainWindow", "Second Equation:"))
        self.labelEqu3.setText(_translate("MainWindow", "Third Equation:"))
        self.labelEqu4.setText(_translate("MainWindow", "Forth Equation:"))
        self.labelEqu5.setText(_translate("MainWindow", "Fifth Equation:"))
        self.labelEqu6.setText(_translate("MainWindow", "Sixth Equation:"))
        self.labelEqu7.setText(_translate("MainWindow", "Seventh Equation:"))
        self.labelEqu8.setText(_translate("MainWindow", "Eighth Equation:"))
        self.labelEqu9.setText(_translate("MainWindow", "Ninth Equation:"))
        self.label_7.setText(_translate("MainWindow", "Parameters"))
        self.label_5.setText(_translate("MainWindow", "Max Iteration:"))
        self.label_6.setText(_translate("MainWindow", "Epsilon:"))
        self.label_8.setText(_translate("MainWindow", "Methods"))
        self.label_9.setText(_translate("MainWindow", "Method:"))
        self.method.setCurrentText(_translate("MainWindow", "All Methods"))
        self.method.setItemText(0, _translate("MainWindow", "All Methods"))
        self.method.setItemText(1, _translate("MainWindow", "Gaussian-Elimination"))
        self.method.setItemText(2, _translate("MainWindow", "LU decomposition"))
        self.method.setItemText(3, _translate("MainWindow", "Gaussian- Jordan"))
        self.method.setItemText(4, _translate("MainWindow", "Gauss-Seidel"))
        self.initialLabel.setText(_translate("MainWindow", "Initial Points:"))
        self.label_10.setText(_translate("MainWindow", "Results"))
        self.label_11.setText(_translate("MainWindow", "Variables Values:"))
        self.execTimeLabel.setText(_translate("MainWindow", "Execution time:"))
        self.SecondsLabel.setText(_translate("MainWindow", "Seconds"))
        self.showIterations.setText(_translate("MainWindow", "Show iterations"))
        self.calculate.setText(_translate("MainWindow", "Calculate"))
        self.showGraph.setText(_translate("MainWindow", "Show Graph"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
