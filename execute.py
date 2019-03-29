# encoding: utf-8
"""
@author: lin
@file: execute.py
@time: 2019/3/22 12:25
@desc:
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Compiler import *
from LexicalAnalyzer import Lexical_Analyzer
from LexicalAnalyzer import Syntactic_Analyzer

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
    def lexical_analysis(self):
        strings = self.textEdit_1.toPlainText()
        answer = Lexical_Analyzer(strings)
        s=''
        for a in answer:
            s=s+str(a)+'\n'
        self.textEdit_2.setPlainText(s)
    def syntactic_analysis(self):
        strings = self.textEdit_1.toPlainText()
        sa = Syntactic_Analyzer(strings)
        result = sa.analysis()
        if result:
            self.textEdit_2.setPlainText(strings+'  right')
        else:
            self.textEdit_2.setPlainText(strings + '  false')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())