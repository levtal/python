 #!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This program creates a quit
button. When we press the button,
the application terminates. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        qbtn = QPushButton('Quit', self)
		'''
		  The second parameter is the parent widget. The parent widget is the Example widget, which is a QWidget by inheritance. 
		'''
        qbtn.clicked.connect(QCoreApplication.instance().quit)
       '''The event processing system in PyQt5 is built with the signal & slot mechanism. If we click on the button, the signal clicked is emitted. The slot can be a Qt slot or any Python callable. The QCoreApplication contains the main event loop—it processes and dispatches all events. The instance() method gives us its current instance. Note that QCoreApplication is created with the QApplication. The clicked signal is connected to the quit() method which terminates the application. The communication is done between two objects: the sender and the receiver. The sender is the push button, the receiver is the application object. 
	   '''


	   qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)       
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())