from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QGraphicsColorizeEffect, QPushButton
from PySide6.QtGui import QColor
from PySide6.QtCore import (
    QPropertyAnimation,
    Property,
)


class CustomButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.colorVal = QColor(181, 189, 104)

        self.colorAnim = QPropertyAnimation(self, b'color')
        self.colorAnim.setDuration(400)
        self.colorAnim.setStartValue(QColor(204,102,102))
        self.colorAnim.setEndValue(QColor(181,189,104))
    
    @Property(QColor)
    def color(self):
        return self.colorVal
    
    @color.setter
    def color(self, val):
        self.colorVal = val
        
        self.setStyleSheet(f"""
                           background-color: rgb({val.red()},{val.green()},{val.blue()});
                           border-radius: 20px;
                           """)
        
    def enterEvent(self, event):
        self.colorAnim.setDirection(self.colorAnim.Forward)
        if self.colorAnim.state() == self.colorAnim.State.Stopped:
            
            self.colorAnim.start()
        QPushButton.enterEvent(self, event)
    
    def leaveEvent(self, event):
        self.colorAnim.setDirection(self.colorAnim.Backward)
        if self.colorAnim.state() == self.colorAnim.State.Stopped:
            self.colorAnim.start()
        QPushButton.leaveEvent(self, event)
        
class CustomButton2(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.colorVal = QColor(181, 189, 104)

        self.colorAnim = QPropertyAnimation(self, b'color')
        self.colorAnim.setDuration(400)
        self.colorAnim.setStartValue(QColor(35,35,35))
        self.colorAnim.setEndValue(QColor(50,50,50))
    
    @Property(QColor)
    def color(self):
        return self.colorVal
    
    @color.setter
    def color(self, val):
        self.colorVal = val
        
        self.setStyleSheet(f"""
                           background-color: rgb({val.red()},{val.green()},{val.blue()});
                           border-radius: 20px;
                           color: #999999;
                           """)
        
    def enterEvent(self, event):
        self.colorAnim.setDirection(self.colorAnim.Forward)
        if self.colorAnim.state() == self.colorAnim.State.Stopped:
            
            self.colorAnim.start()
        QPushButton.enterEvent(self, event)
    
    def leaveEvent(self, event):
        self.colorAnim.setDirection(self.colorAnim.Backward)
        if self.colorAnim.state() == self.colorAnim.State.Stopped:
            self.colorAnim.start()
        QPushButton.leaveEvent(self, event)  