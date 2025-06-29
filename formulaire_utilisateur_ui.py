# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulaire_utilisateur.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background: #4b7bb2;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(600, 0))
        self.widget.setStyleSheet(u"background: #fff;")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save_utilisateur_btn = QPushButton(self.widget)
        self.save_utilisateur_btn.setObjectName(u"save_utilisateur_btn")
        self.save_utilisateur_btn.setMinimumSize(QSize(300, 35))
        self.save_utilisateur_btn.setMaximumSize(QSize(300, 35))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.save_utilisateur_btn.setFont(font)
        self.save_utilisateur_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_utilisateur_btn.setStyleSheet(u"background: #4b7bb2;\n"
"color: #fff;")

        self.horizontalLayout.addWidget(self.save_utilisateur_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        
        self.mot_de_passe_input = QLineEdit(self.widget_3)
        self.mot_de_passe_input.setObjectName(u"mot_de_passe_input")
        self.mot_de_passe_input.setMinimumSize(QSize(0, 35))
        self.mot_de_passe_input.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.mot_de_passe_input, 3, 0, 1, 1)

        self.nom_utilisateur = QLabel(self.widget_3)
        self.nom_utilisateur.setObjectName(u"nom_utilisateur")
        self.nom_utilisateur.setFont(font)

        self.gridLayout.addWidget(self.nom_utilisateur, 0, 0, 1, 1)

        self.mot_de_passe = QLabel(self.widget_3)
        self.mot_de_passe.setObjectName(u"mot_de_passe")
        self.mot_de_passe.setFont(font)

        self.gridLayout.addWidget(self.mot_de_passe, 2, 0, 1, 1)

        self.nom_utilisateur_input = QLineEdit(self.widget_3)
        self.nom_utilisateur_input.setObjectName(u"nom_utilisateur_input")
        self.nom_utilisateur_input.setMinimumSize(QSize(0, 35))
        self.nom_utilisateur_input.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.nom_utilisateur_input, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label)


        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.widget)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.save_utilisateur_btn.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.nom_utilisateur.setText(QCoreApplication.translate("MainWindow", u"Nom Utilisateur", None))
        self.mot_de_passe.setText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Creer un Utilisateur", None))
    # retranslateUi

