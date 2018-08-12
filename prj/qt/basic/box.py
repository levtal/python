#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial
 http://zetcode.com/gui/pyqt5/firstprograms/
In this example, we create a simple
window in PyQt5.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)# PyQt5 application must create an application
     #  object.
     # The sys.argv parameter is a list of arguments from a command line. Python scripts can be run from the shell. It is a way how we can control the startup of our scripts.

    w = QWidget() # The QWidget widget is the base class of all user
                  # interface objects in PyQt5.
    w.resize(250, 650)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())