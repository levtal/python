#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
http://zetcode.com/gui/pyqt5/menustoolbars/
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        #New menu is created with QMenu.
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        #An action is added to the submenu with addAction().
        impMenu.addAction(impAct)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())