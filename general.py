import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from page_general import PageGeneral
from page_additional import PageAdditional
from page_start import PageStart


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.clicks = 0
        self.setStyleSheet("background-color: rgb(230, 230, 250);")
        self.setMinimumSize(800, 500)
        self.resize(1200, 700)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.offset = None
        self.offset_title_bar = False

        self.top_bar = QFrame()
        self.top_bar.setObjectName('top_bar')
        self.top_bar.setStyleSheet("""
            #top_bar {
                background-color: rgb(230, 230, 250);
                border-top-left-radius:  1em 1em;
                border-top-right-radius:  1em 1em;
            }
        """)
        self.top_bar.setMaximumHeight(40)
        self.top_bar.setFrameShadow(QFrame.Raised)

        self.content = QFrame()
        self.content.setStyleSheet("""
            background-color: rgb(35,43,50);
            border-bottom-right-radius: 1em 1em;
            border-bottom-left-radius:  1em 1em;
        """)
        self.content.setFrameShadow(QFrame.Raised)

# StackedWidget
        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
# Adds Pages
        self.pageStart = PageStart()
        self.stackedWidget.addWidget(self.pageStart)
        self.pageGeneral = PageGeneral()
        self.stackedWidget.addWidget(self.pageGeneral)
        self.pageAdditional = PageAdditional()
        self.stackedWidget.addWidget(self.pageAdditional)

# left_bar
        self.left_bar = QFrame()
        self.left_bar.setStyleSheet('''
            background-color: rgb(230, 230, 250);
            border-top-left-radius:  1em 1em;
            border-bottom-left-radius:  1em 1em;
            ''')
        self.left_bar.setMinimumWidth(50)
        self.left_bar.setMaximumWidth(50)
        self.left_bar.setFrameShadow(QFrame.StyledPanel | QFrame.Raised)

# title_bar
        self.title_bar = QFrame()
        self.title_bar.setStyleSheet("background-color: transparent")
        self.title_bar.setMinimumWidth(120)
        self.gridLayout2 = QtWidgets.QGridLayout(self.title_bar)
        self.gridLayout2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout2.setSpacing(0)
        self.label_title = QLabel('Title_bar', alignment=Qt.AlignCenter)
        self.label_title.setObjectName('label_title')
        self.label_title.setStyleSheet("background-color: #E6E6FA")
        font = self.label_title.font()
        font.setPointSize(15)
        self.label_title.setFont(font)
        self.label_title.installEventFilter(self)
        self.gridLayout2.addWidget(self.label_title, 0, 0)

# min_button
        self.min_button = QPushButton()
        self.min_button.setStyleSheet("""
            QPushButton:hover { 
                background-color: rgb(177, 247, 173);
                border: 0px solid;
                border-top-left-radius:  1em 1em;
                border-bottom-left-radius: 1em 1em;
                border-top-right-radius:  1em 1em;
                border-bottom-right-radius: 1em 1em;
            }
            QPushButton:!hover { 
                background-color: transparent; 
                border: 0px solid; 
                font: 11pt; 
                color: rgb(180,180,180) 
            }
        """)
        self.min_button.setIcon(
            QIcon(QPixmap('icons/Apagar/cil-minus.png')))
        self.min_button.setMinimumHeight(40)
        self.min_button.setMaximumWidth(40)
        self.min_button.clicked.connect(self.turn_window)

# max_button
        self.max_button = QPushButton()
        self.max_button.setStyleSheet("""
            QPushButton:hover { 
                background-color: rgb(177, 247, 173);
                border: 0px solid;
                border-top-left-radius:  1em 1em;
                border-bottom-left-radius: 1em 1em;
                border-top-right-radius:  1em 1em;
                border-bottom-right-radius: 1em 1em;
            }
            QPushButton:!hover { 
                background-color: transparent; 
                border: 0px solid; 
                font: 11pt; 
                color: rgb(180,180,180) 
            }
        """)
        self.max_button.setIcon(
            QIcon(QPixmap('icons/Apagar/cil-fullscreen.png')))
        self.max_button.setMinimumHeight(40)
        self.max_button.setMaximumWidth(40)
        self.max_button.clicked.connect(self.expand_window)

# close_button
        self.close_button = QPushButton()
        self.close_button.setStyleSheet("""
            QPushButton:hover { 
                background-color: rgb(255, 120, 120);
                border: 0px solid;
                border-top-left-radius:  1em 1em;
                border-bottom-left-radius: 1em 1em;
                border-top-right-radius:  1em 1em;
                border-bottom-right-radius: 1em 1em;
            }
            QPushButton:!hover { 
                background-color: transparent; 
                border: 0px solid; 
                font: 11pt; 
                color: rgb(180,180,180) 
            }
        """)
        self.close_button.setIcon(
            QIcon(QPixmap('icons/Apagar/cil-power-standby.png')))
        self.close_button.setMinimumHeight(40)
        self.close_button.setMaximumWidth(40)
        self.close_button.clicked.connect(self.close_window)

# menu_button
        self.menu_button = QPushButton()
        self.menu_button.setStyleSheet("""
            QPushButton:hover { 
                background-color: rgb(177, 247, 173);
                border-radius: 9px;
                border: 0px solid 
            }
            QPushButton:!hover { 
                background-color: transparent;
                border-radius: 9px;
                border: 0px solid; 
                font: 11pt; 
                color: rgb(180,180,180) 
            }
        """)
        self.menu_button.setText("")
        self.menu_button.setIcon(QIcon(QPixmap('icons/Apagar/cil-menu.png')))
        self.menu_button.setMinimumHeight(40)
        self.menu_button.clicked.connect(self.toggle)

# page_1_button
        self.page_1_button = QPushButton()
        self.page_1_button.setStyleSheet("""
            QPushButton:hover { 
                background-color: rgb(177, 247, 173);
                border-radius: 9px;
                border: 0px solid  
            }
            QPushButton:!hover { 
                background-color: transparent; 
                border: 0px solid; 
                font: 11pt;
                border-radius: 9px;
                color: rgb(180,180,180) 
            }
        """)
        self.page_1_button.setText("")
        self.page_1_button.setIcon(
            QIcon(QPixmap('icons/Apagar/cil-mood-very-good.png')))
        self.page_1_button.setMinimumHeight(40)
        self.page_1_button.clicked.connect(self.page_1)

        self.chek_activ_1 = QFrame()
        self.chek_activ_1.setMaximumWidth(0)
        self.chek_activ_1.setFrameShadow(QFrame.Raised)

# page_2_button
        self.page_2_button = QPushButton()
        self.page_2_button.setStyleSheet("""
            QPushButton:hover { 
                background-color: rgb(177, 247, 173);
                border-radius: 9px;
                border: 0px solid 
            }
            QPushButton:!hover { 
                background-color: transparent;
                border-radius: 9px;
                border: 0px solid; 
                font: 11pt;
                color: rgb(180,180,180)
            }
        """)
        self.page_2_button.setText("")
        self.page_2_button.setIcon(
            QIcon(QPixmap('icons/Apagar/cil-mood-very-bad.png')))
        self.page_2_button.setMinimumHeight(40)
        self.page_2_button.clicked.connect(self.page_2)

        self.chek_activ_2 = QFrame()
        self.chek_activ_2.setMaximumWidth(0)
        self.chek_activ_2.setFrameShadow(QFrame.Raised)

        self.layout_navigation = QGridLayout(self.top_bar)
        self.layout_navigation.addWidget(self.title_bar, 0, 0)
        self.layout_navigation.addWidget(self.min_button, 0, 1)
        self.layout_navigation.addWidget(self.max_button, 0, 2)
        self.layout_navigation.addWidget(self.close_button, 0, 3)
        self.layout_navigation.setContentsMargins(0, 0, 0, 0)

        self.layout_menu_0 = QHBoxLayout()
        self.layout_menu_0.addWidget(self.menu_button)
        self.layout_menu_0.setContentsMargins(0, 0, 0, 0)
        self.layout_menu_0.setSpacing(0)

        self.layout_menu_1 = QHBoxLayout()
        self.layout_menu_1.addWidget(self.chek_activ_1)
        self.layout_menu_1.addWidget(self.page_1_button)
        self.layout_menu_1.setContentsMargins(0, 0, 0, 0)
        self.layout_menu_1.setSpacing(0)

        self.layout_menu_2 = QHBoxLayout()
        self.layout_menu_2.addWidget(self.chek_activ_2)
        self.layout_menu_2.addWidget(self.page_2_button)
        self.layout_menu_2.setContentsMargins(0, 0, 0, 0)
        self.layout_menu_2.setSpacing(0)

        self.vbox_1 = QVBoxLayout(self.left_bar)
        self.vbox_1.addLayout(self.layout_menu_0)
        self.vbox_1.addLayout(self.layout_menu_1)
        self.vbox_1.addLayout(self.layout_menu_2)
        self.vbox_1.addStretch()
        self.vbox_1.setContentsMargins(0, 0, 0, 0)

        self.right_bar = QFrame()
        self.right_bar.setStyleSheet('''
            border-top-right-radius:  14px; border-bottom-right-radius: 14px;
            ''')
        self.right_bar.setFrameShadow(QFrame.Raised)

        self.vbox_2 = QVBoxLayout(self.right_bar)
        self.vbox_2.addWidget(self.top_bar)
        self.vbox_2.addWidget(self.stackedWidget)
        self.vbox_2.setContentsMargins(0, 0, 0, 0)
        self.vbox_2.setSpacing(0)

        self.hbox = QHBoxLayout(self)
        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.hbox.setSpacing(0)
        self.hbox.addWidget(self.left_bar)
        self.hbox.addWidget(self.right_bar)

    def eventFilter(self, obj, event):
        if self.label_title is obj:
            if event.type() == QtCore.QEvent.Enter:
                self.offset_title_bar = True
            elif event.type() == QtCore.QEvent.Leave:
                self.offset_title_bar = False
        return super().eventFilter(obj, event)

    def page_1(self):
        self.stackedWidget.setCurrentIndex(1)
        self.chek_activ_1.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 227, 32, 1), stop:1 transparent);")
        self.chek_activ_1.setMaximumWidth(10)
        self.chek_activ_2.setStyleSheet("")
        self.chek_activ_2.setMaximumWidth(0)

    def page_2(self):
        self.stackedWidget.setCurrentIndex(2)
        self.chek_activ_1.setStyleSheet("")
        self.chek_activ_1.setMaximumWidth(0)
        self.chek_activ_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 227, 32, 1), stop:1 transparent);")
        self.chek_activ_2.setMaximumWidth(10)

    def turn_window(self):
        self.showMinimized()

    def expand_window(self):
        if self.isMaximized():
            self.max_button.setIcon(
                QIcon("icons/Apagar/cil-fullscreen.png"))
            self.showNormal()
            self.left_bar.setStyleSheet('''
            background-color: rgb(230, 230, 250);
            border-top-left-radius:  1em 1em;
            border-bottom-left-radius:  1em 1em;
            ''')
            self.right_bar.setStyleSheet('''
            border-top-right-radius:  14px; border-bottom-right-radius: 14px;
            ''')
            self.pageStart.sizewin(maxwindow=False)
            self.pageGeneral.sizewin(maxwindow=False)
            self.pageAdditional.sizewin(maxwindow=False)
        else:
            self.max_button.setIcon(
                QIcon("icons/Apagar/cil-fullscreen-exit.png"))
            self.showMaximized()
            self.left_bar.setStyleSheet('''
            background-color: rgb(230, 230, 250);
            ''')
            self.right_bar.setStyleSheet('''''')
            self.pageStart.sizewin(maxwindow=True)
            self.pageGeneral.sizewin(maxwindow=True)
            self.pageAdditional.sizewin(maxwindow=True)

    def close_window(self):
        self.close()

    def mousePressEvent(self, event):
        """ Координаты записи нажатия мышью
        :param event:
        """
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """ Мышь двигает окно
        :param event:
        """
        if self.isMaximized():
            return
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton and self.offset_title_bar:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        """ Мышь отпущена, удалить координаты
        :param event:
        """
        self.offset = None
        super().mouseReleaseEvent(event)

    def toggle(self):
        self.animation = QPropertyAnimation(self.left_bar, b"minimumWidth")
        self.animation.setDuration(900)
        if self.left_bar.width() == 50:
            self.animation.setStartValue(50)
            self.animation.setEndValue(280)
            self.page_1_button.setText("Page 1")
            self.page_1_button.setIcon(
                QIcon(QPixmap('icons/Noimg.png')))
            self.page_2_button.setText("Page 2")
            self.page_2_button.setIcon(
                QIcon(QPixmap('icons/Noimg.png')))
        else:
            self.animation.setStartValue(280)
            self.animation.setEndValue(50)
            self.page_1_button.setText("")
            self.page_1_button.setIcon(
                QIcon(QPixmap('icons/Apagar/cil-mood-very-good.png')))
            self.page_2_button.setText("")
            self.page_2_button.setIcon(
                QIcon(QPixmap('icons/Apagar/cil-mood-very-bad.png')))

        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
