# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 40)")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(285, 20, 390, 60))
        self.label.setStyleSheet("background: transparent;\n"
"color: rgb(166, 203, 255);\n"
"margin: 5px;\n"
"font-size: 36px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 111, 31))
        self.label_2.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox.setGeometry(QtCore.QRect(270, 100, 191, 21))
        self.checkBox.setStyleSheet("outline: none;\n"
"background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.checkBox.setObjectName("checkBox")
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(40, 120, 100, 2))
        self.line.setStyleSheet("background-color:  rgb(234, 255, 253);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 140, 451, 421))
        self.groupBox.setStyleSheet("background-color: rgba(152, 189, 255, 10);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 191, 31))
        self.label_4.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.label_4.setObjectName("label_4")
        self.nbOfVariables = QtWidgets.QSpinBox(self.groupBox)
        self.nbOfVariables.setGeometry(QtCore.QRect(230, 10, 31, 41))
        self.nbOfVariables.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;;\n"
"background: transparent;\n"
"font-size: 18px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);\n"
"text-align: center;\n"
"")
        self.nbOfVariables.setMinimum(2)
        self.nbOfVariables.setMaximum(8)
        self.nbOfVariables.setProperty("value", 2)
        self.nbOfVariables.setObjectName("nbOfVariables")
        self.errorMsg = QtWidgets.QLabel(self.groupBox)
        self.errorMsg.setGeometry(QtCore.QRect(30, 50, 351, 31))
        self.errorMsg.setStyleSheet("background: transparent;\n"
"color:rgb(252, 1, 7);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.errorMsg.setObjectName("errorMsg")
        self.labelEqu1 = QtWidgets.QLabel(self.groupBox)
        self.labelEqu1.setGeometry(QtCore.QRect(10, 90, 141, 31))
        self.labelEqu1.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.labelEqu1.setObjectName("labelEqu1")
        self.lineEditEQ1 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEQ1.setGeometry(QtCore.QRect(170, 90, 241, 21))
        self.lineEditEQ1.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 12px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.lineEditEQ1.setText("")
        self.lineEditEQ1.setObjectName("lineEditEQ1")
        self.labelEqu2 = QtWidgets.QLabel(self.groupBox)
        self.labelEqu2.setGeometry(QtCore.QRect(10, 130, 141, 31))
        self.labelEqu2.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.labelEqu2.setObjectName("labelEqu2")
        self.labelEqu3 = QtWidgets.QLabel(self.groupBox)
        self.labelEqu3.setGeometry(QtCore.QRect(10, 170, 141, 31))
        self.labelEqu3.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.labelEqu3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.labelEqu3.setObjectName("labelEqu3")
        self.labelEqu4 = QtWidgets.QLabel(self.groupBox)
        self.labelEqu4.setGeometry(QtCore.QRect(10, 210, 141, 31))
        self.labelEqu4.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.labelEqu4.setObjectName("labelEqu4")
        self.labelEqu5 = QtWidgets.QLabel(self.groupBox)
        self.labelEqu5.setGeometry(QtCore.QRect(10, 250, 141, 31))
        self.labelEqu5.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.labelEqu5.setObjectName("labelEqu5")
        self.labelEqu6 = QtWidgets.QLabel(self.groupBox)
        self.labelEqu6.setGeometry(QtCore.QRect(10, 290, 141, 31))
        self.labelEqu6.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.labelEqu6.setObjectName("labelEqu6")
        self.labelEqu7 = QtWidgets.QLabel(self.groupBox)
        self.labelEqu7.setGeometry(QtCore.QRect(10, 330, 141, 31))
        self.labelEqu7.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.labelEqu7.setObjectName("labelEqu7")
        self.labelEqu8 = QtWidgets.QLabel(self.groupBox)
        self.labelEqu8.setGeometry(QtCore.QRect(10, 370, 131, 31))
        self.labelEqu8.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;")
        self.labelEqu8.setObjectName("labelEqu8")
        self.lineEditEQ3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEQ3.setGeometry(QtCore.QRect(170, 170, 241, 21))
        self.lineEditEQ3.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 12px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.lineEditEQ3.setObjectName("lineEditEQ3")
        self.lineEditEQ4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEQ4.setGeometry(QtCore.QRect(170, 210, 241, 21))
        self.lineEditEQ4.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 12px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.lineEditEQ4.setObjectName("lineEditEQ4")
        self.lineEditEQ5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEQ5.setGeometry(QtCore.QRect(170, 250, 241, 21))
        self.lineEditEQ5.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 12px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.lineEditEQ5.setObjectName("lineEditEQ5")
        self.lineEditEQ6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEQ6.setGeometry(QtCore.QRect(170, 290, 241, 21))
        self.lineEditEQ6.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 12px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.lineEditEQ6.setObjectName("lineEditEQ6")
        self.lineEditEQ7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEQ7.setGeometry(QtCore.QRect(170, 330, 241, 21))
        self.lineEditEQ7.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 12px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.lineEditEQ7.setObjectName("lineEditEQ7")
        self.lineEditEQ8 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEQ8.setGeometry(QtCore.QRect(170, 370, 241, 21))
        self.lineEditEQ8.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 12px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.lineEditEQ8.setObjectName("lineEditEQ8")
        self.lineEditEQ2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEQ2.setGeometry(QtCore.QRect(170, 130, 241, 21))
        self.lineEditEQ2.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 12px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.lineEditEQ2.setText("")
        self.lineEditEQ2.setObjectName("lineEditEQ2")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(520, 90, 131, 31))
        self.label_7.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.label_7.setObjectName("label_7")
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setGeometry(QtCore.QRect(530, 120, 113, 2))
        self.line_2.setStyleSheet("background-color:  rgb(234, 255, 253);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.parametersGroup = QtWidgets.QGroupBox(self.centralWidget)
        self.parametersGroup.setGeometry(QtCore.QRect(520, 140, 421, 51))
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
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.maxIterations.setMaximum(100000000)
        self.maxIterations.setProperty("value", 50)
        self.maxIterations.setObjectName("maxIterations")
        self.label_6 = QtWidgets.QLabel(self.parametersGroup)
        self.label_6.setGeometry(QtCore.QRect(220, 10, 91, 31))
        self.label_6.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.label_6.setObjectName("label_6")
        self.Epsilon = QtWidgets.QDoubleSpinBox(self.parametersGroup)
        self.Epsilon.setGeometry(QtCore.QRect(320, 0, 91, 41))
        self.Epsilon.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"outline: none;\n"
"font-size: 14px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.Epsilon.setDecimals(6)
        self.Epsilon.setMinimum(1e-06)
        self.Epsilon.setMaximum(1.0)
        self.Epsilon.setSingleStep(0.001)
        self.Epsilon.setProperty("value", 1e-05)
        self.Epsilon.setObjectName("Epsilon")
        self.line_3 = QtWidgets.QFrame(self.centralWidget)
        self.line_3.setGeometry(QtCore.QRect(500, 140, 3, 420))
        self.line_3.setStyleSheet("background-color:  rgb(234, 255, 253);")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(520, 200, 91, 31))
        self.label_8.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.label_8.setObjectName("label_8")
        self.line_4 = QtWidgets.QFrame(self.centralWidget)
        self.line_4.setGeometry(QtCore.QRect(530, 230, 78, 2))
        self.line_4.setStyleSheet("background-color:  rgb(234, 255, 253);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.MethodsGroup = QtWidgets.QGroupBox(self.centralWidget)
        self.MethodsGroup.setGeometry(QtCore.QRect(520, 250, 411, 91))
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
        self.initialLabel.setGeometry(QtCore.QRect(10, 50, 161, 31))
        self.initialLabel.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 16px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.initialLabel.setObjectName("initialLabel")
        self.initialPointsInput = QtWidgets.QLineEdit(self.MethodsGroup)
        self.initialPointsInput.setGeometry(QtCore.QRect(180, 50, 221, 21))
        self.initialPointsInput.setStyleSheet("border: 0;\n"
"border-bottom: 1px solid #999;\n"
"background: transparent;\n"
"font-size: 12px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.initialPointsInput.setText("")
        self.initialPointsInput.setObjectName("initialPointsInput")
        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_10.setGeometry(QtCore.QRect(520, 340, 91, 31))
        self.label_10.setStyleSheet("background: transparent;\n"
"color: rgb(234, 255, 253);\n"
"margin: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color: rgb(234, 255, 253);")
        self.label_10.setObjectName("label_10")
        self.line_5 = QtWidgets.QFrame(self.centralWidget)
        self.line_5.setGeometry(QtCore.QRect(530, 370, 69, 2))
        self.line_5.setStyleSheet("background-color:  rgb(234, 255, 253);")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connection of functions
        self.nbOfVariables.valueChanged.connect(self.setNumberOfEquations)
        self.checkBox.stateChanged.connect(self.readFromFile)
        self.method.currentTextChanged.connect(self.setMethod)
        # Hide unneeded fields.
        self.errorMsg.hide()
        self.labelEqu3.hide()
        self.labelEqu4.hide()
        self.labelEqu5.hide()
        self.labelEqu6.hide()
        self.labelEqu7.hide()
        self.labelEqu8.hide()
        self.lineEditEQ3.hide()
        self.lineEditEQ4.hide()
        self.lineEditEQ5.hide()
        self.lineEditEQ6.hide()
        self.lineEditEQ7.hide()
        self.lineEditEQ8.hide()
        self.initialLabel.hide()
        self.initialPointsInput.hide()

    def setMethod(self):
        if (self.method.currentText() == "Gaussian- Jordan" or self.method.currentText() == "All"):
            self.initialPointsInput.show()
            self.initialLabel.show()
        else:
            self.initialLabel.hide()
            self.initialPointsInput.hide()

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
        self.lineEditEQ3.hide()
        self.lineEditEQ4.hide()
        self.lineEditEQ5.hide()
        self.lineEditEQ6.hide()
        self.lineEditEQ7.hide()
        self.lineEditEQ8.hide()
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Numerical Project"))
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
        self.label_7.setText(_translate("MainWindow", "Parameters"))
        self.label_5.setText(_translate("MainWindow", "Max Iteration:"))
        self.label_6.setText(_translate("MainWindow", "Epsilon:"))
        self.label_8.setText(_translate("MainWindow", "Methods"))
        self.label_9.setText(_translate("MainWindow", "Method:"))
        self.method.setItemText(0, _translate("MainWindow", "Gaussian-Elimination"))
        self.method.setItemText(1, _translate("MainWindow", "LU decomposition"))
        self.method.setItemText(2, _translate("MainWindow", "Gaussian- Jordan"))
        self.method.setItemText(3, _translate("MainWindow", "Gauss-Seidel"))
        self.method.setItemText(4, _translate("MainWindow", "All"))
        self.initialLabel.setText(_translate("MainWindow", "Initial Points:"))
        self.label_10.setText(_translate("MainWindow", "Result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
