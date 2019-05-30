# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Compiler.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lexical_btn = QtWidgets.QPushButton(self.centralwidget)
        self.lexical_btn.setGeometry(QtCore.QRect(350, 40, 131, 31))
        self.lexical_btn.setObjectName("lexical_btn")
        self.textEdit_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_1.setGeometry(QtCore.QRect(40, 40, 251, 381))
        self.textEdit_1.setObjectName("textEdit_1")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(530, 40, 251, 381))
        self.textEdit_2.setObjectName("textEdit_2")
        self.syntactic_btn = QtWidgets.QPushButton(self.centralwidget)
        self.syntactic_btn.setGeometry(QtCore.QRect(350, 120, 131, 31))
        self.syntactic_btn.setObjectName("syntactic_btn")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 200, 131, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.lexical_btn.clicked.connect(MainWindow.lexical_analysis)
        self.syntactic_btn.clicked.connect(MainWindow.syntactic_analysis)
        self.pushButton.clicked.connect(MainWindow.LL1_analysis)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Compiler"))
        self.lexical_btn.setText(_translate("MainWindow", "LexicalAnalyzer"))
        self.syntactic_btn.setText(_translate("MainWindow", "SyntacticAnalyzer"))
        self.pushButton.setText(_translate("MainWindow", "LL（1）"))

