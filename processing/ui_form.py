# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(790, 480)
        MainWindow.setMinimumSize(QSize(790, 480))
        MainWindow.setMaximumSize(QSize(790, 480))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.previewGroupBox = QGroupBox(self.centralwidget)
        self.previewGroupBox.setObjectName(u"previewGroupBox")
        self.previewGroupBox.setGeometry(QRect(20, 10, 750, 424))
        self.previewGroupBox.setMinimumSize(QSize(663, 424))
        self.horizontalLayout = QHBoxLayout(self.previewGroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.previewContainer = QWidget(self.previewGroupBox)
        self.previewContainer.setObjectName(u"previewContainer")
        self.previewContainer.setMinimumSize(QSize(640, 360))
        self.previewContainer.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.previewContainer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 790, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.previewGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.previewContainer.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #000", None))
    # retranslateUi

