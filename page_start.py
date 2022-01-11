import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class PageStart(QMainWindow):
    def __init__(self):
        super().__init__()

        self.page_start = QtWidgets.QWidget(self)
        self.page_start.setObjectName("page start")
        self.setCentralWidget(self.page_start)
        self.page_start.setStyleSheet("border-bottom-right-radius: 1em 1em;")

        self.gridLayout = QtWidgets.QGridLayout(self.page_start)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.label_content = QLabel(
            'Page Start', self, alignment=Qt.AlignCenter)
        self.label_content.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(122, 255, 178, 1), stop:1 rgba(230, 230, 250, 250));")
        self.gridLayout.addWidget(self.label_content, 0, 0)
        self.gridLayout.setRowStretch(0, 1)
        font = self.label_content.font()
        font.setPointSize(20)
        self.label_content.setFont(font)
        self.sizeGrip = QtWidgets.QSizeGrip(self)
        self.sizeGrip.setStyleSheet("background-color: #E6E6FA")
        self.gridLayout.addWidget(
            self.sizeGrip, 1, 0, 1, 1, QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)

    def sizewin(self, maxwindow=False):
        if maxwindow == False:
            self.sizeGrip.show()
            self.page_start.setStyleSheet(
                "border-bottom-right-radius: 1em 1em;")
        elif maxwindow == True:
            self.sizeGrip.hide()
            self.page_start.setStyleSheet("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PageStart()
    window.show()
    sys.exit(app.exec_())
