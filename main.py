from email.mime import application
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QMessageBox
from ui import Ui_MainWindow
from controller import *

class Parser(QtWidgets.QMainWindow):
    def __init__(self):
        super(Parser, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.directory = ""
        
    def init_UI(self):
        self.setWindowTitle("Osu collector parser")
        
        self.ui.lineEdit.setPlaceholderText('collection url')
        self.ui.pushButton.clicked.connect(self.download_beatmaps)
        self.ui.pushButton_2.clicked.connect(self.get_save_path)
    
    def get_save_path(self):
        self.directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        _translate = QtCore.QCoreApplication.translate
        self.ui.label.setText(_translate("MainWindow", self.directory))
    
    def download_beatmaps(self):
        url = self.ui.lineEdit.text()
        if url != "" and self.directory != "":
            parse_url_song(url, self.directory+"/")
            msg = QMessageBox()
            msg.setText("Download is ended!")
            msg.setWindowTitle("Info")
            msg.setWindowIcon(QtGui.QIcon("white tic.png"))
            msg.setIcon(QMessageBox.Information)
            msg.setStyleSheet("background-color: rgb(255, 255, 255);")
            msg.setStyleSheet("color: rgb(0, 0, 0);")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setText("Please set correct url or directory path")
            msg.setWindowTitle("Warning")
            msg.setWindowIcon(QtGui.QIcon("white tic.png"))
            msg.setIcon(QMessageBox.Information)
            msg.setStyleSheet("background-color: rgb(255, 255, 255);")
            msg.setStyleSheet("color: rgb(0, 0, 0);")
            msg.exec_()
            #QMessageBox.about(self, "Warning", "Please set correct url or directory path!")
        

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Parser()
    application.show()
    sys.exit(app.exec())