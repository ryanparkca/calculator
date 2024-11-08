# ch 4.2.1. main.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.btn1=QPushButton('Message', self)
        self.setWindowTitle('Calculator')
        self.resize(256,256)
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())
