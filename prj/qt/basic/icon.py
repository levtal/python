#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial
 http://zetcode.com/gui/pyqt5/firstprograms/

This example shows an icon
in the titlebar of the window.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget): #Example class inherits from the QWidget class.
    def __init__(self):
        super().__init__()  # __init__() method is a constructor

        self.initUI()# The creation of the GUI is
                     # delegated to the initUI() method.

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')

        self.setWindowIcon(QIcon('web.png'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())