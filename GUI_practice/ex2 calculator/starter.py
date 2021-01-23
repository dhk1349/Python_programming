# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 23:33:56 2021

@author: dhk1349
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 22:31:26 2021

@author: dhk1349
"""

import sys
from calculator import Ui_MainWindow #수정부분
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class calculator_obj(QMainWindow, Ui_MainWindow): 
    
    def __init__(self):

        super().__init__()

        self.setupUi(self)
        # self.timer = QTimer(self)
        # self.timer.setSingleShot(False)
        # self.timer.setInterval(5000) # in milliseconds, so 5000 = 5 seconds
        # # self.timer.timeout.connect(self.start_Macro)
        # self.timer.start()i0nscn2kdlr2k


        #print(self.hasMouseTracking())


        self.show()



app = QApplication([])
sn = calculator_obj()
QApplication.processEvents()
sys.exit(app.exec_())