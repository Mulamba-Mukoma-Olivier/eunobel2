# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulaire_stocks.ui'
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

        self.save_stock_btn = QPushButton(self.widget)
        self.save_stock_btn.setObjectName(u"save_stock_btn")
        self.save_stock_btn.setMinimumSize(QSize(300, 35))
        self.save_stock_btn.setMaximumSize(QSize(300, 35))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.save_stock_btn.setFont(font)
        self.save_stock_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_stock_btn.setStyleSheet(u"background: #4b7bb2;\n"
"color: #fff;")

        self.horizontalLayout.addWidget(self.save_stock_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.id_produit_stock_input = QLineEdit(self.widget_3)
        self.id_produit_stock_input.setObjectName(u"id_produit_stock_input")
        self.id_produit_stock_input.setMinimumSize(QSize(0, 35))
        self.id_produit_stock_input.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.id_produit_stock_input, 1, 0, 1, 1)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.quantite_stock_input = QLineEdit(self.widget_3)
        self.quantite_stock_input.setObjectName(u"quantite_stock_input")
        self.quantite_stock_input.setMinimumSize(QSize(0, 35))
        self.quantite_stock_input.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.quantite_stock_input, 5, 0, 1, 1)

        self.id_entrepot_stock_input = QLineEdit(self.widget_3)
        self.id_entrepot_stock_input.setObjectName(u"id_entrepot_stock_input")
        self.id_entrepot_stock_input.setMinimumSize(QSize(0, 35))
        self.id_entrepot_stock_input.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.id_entrepot_stock_input, 3, 0, 1, 1)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)


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
        self.save_stock_btn.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ID Produit", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Quantite", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ID Entrepot", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Stocks", None))
    # retranslateUi

# if __name__=='__main__':
#     app = QApplication([])
#     ecran = QMainWindow()
#     ui_ecran = Ui_MainWindow()
#     ui_ecran.setupUi(ecran)
#     ecran.show()
#     app.exec()