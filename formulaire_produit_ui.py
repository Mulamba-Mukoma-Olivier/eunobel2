# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulaire_produit.ui'
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
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)


        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1, Qt.AlignHCenter)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)

        self.id_produit_input = QLineEdit(self.widget_3)
        self.id_produit_input.setObjectName(u"id_produit_input")
        self.id_produit_input.setMinimumSize(QSize(0, 35))
        self.id_produit_input.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.id_produit_input, 1, 0, 1, 1)

        self.id_categorie_produit_input = QLineEdit(self.widget_3)
        self.id_categorie_produit_input.setObjectName(u"id_categorie_produit_input")
        self.id_categorie_produit_input.setMinimumSize(QSize(0, 35))
        self.id_categorie_produit_input.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.id_categorie_produit_input, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)

        self.nom_produit_input = QLineEdit(self.widget_3)
        self.nom_produit_input.setObjectName(u"nom_produit_input")
        self.nom_produit_input.setMinimumSize(QSize(0, 35))
        self.nom_produit_input.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.nom_produit_input, 3, 0, 1, 1)

        self.prix_achat_produit_input = QLineEdit(self.widget_3)
        self.prix_achat_produit_input.setObjectName(u"prix_achat_produit_input")
        self.prix_achat_produit_input.setMinimumSize(QSize(0, 35))
        self.prix_achat_produit_input.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.prix_achat_produit_input, 3, 1, 1, 1)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout.addWidget(self.label_8, 4, 1, 1, 1)

        self.description_produit_input = QLineEdit(self.widget_3)
        self.description_produit_input.setObjectName(u"description_produit_input")
        self.description_produit_input.setMinimumSize(QSize(0, 35))
        self.description_produit_input.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.description_produit_input, 5, 0, 1, 1)

        self.prix_vente_produit_input = QLineEdit(self.widget_3)
        self.prix_vente_produit_input.setObjectName(u"prix_vente_produit_input")
        self.prix_vente_produit_input.setMinimumSize(QSize(0, 35))
        self.prix_vente_produit_input.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.prix_vente_produit_input, 5, 1, 1, 1)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout.addWidget(self.label_9, 6, 1, 1, 1)

        self.code_barre_produit_input = QLineEdit(self.widget_3)
        self.code_barre_produit_input.setObjectName(u"code_barre_produit_input")
        self.code_barre_produit_input.setMinimumSize(QSize(0, 35))
        self.code_barre_produit_input.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.code_barre_produit_input, 7, 0, 1, 1)

        self.seuil_alerte_produit_input = QLineEdit(self.widget_3)
        self.seuil_alerte_produit_input.setObjectName(u"seuil_alerte_produit_input")
        self.seuil_alerte_produit_input.setMinimumSize(QSize(0, 35))
        self.seuil_alerte_produit_input.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.seuil_alerte_produit_input, 7, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save_produit_btn = QPushButton(self.widget)
        self.save_produit_btn.setObjectName(u"save_produit_btn")
        self.save_produit_btn.setMinimumSize(QSize(300, 35))
        self.save_produit_btn.setMaximumSize(QSize(300, 35))
        self.save_produit_btn.setFont(font1)
        self.save_produit_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_produit_btn.setStyleSheet(u"background: #4b7bb2;\n"
"color: #fff;")

        self.horizontalLayout.addWidget(self.save_produit_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)


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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enregistrer Vos Produits", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ID Produit", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ID Categorie", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nom Produit", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Prix d'achat", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"description", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Prix de vente", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Code barres", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Seuil d'alerte", None))
        self.save_produit_btn.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
    # retranslateUi

# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     ecran = QMainWindow()
#     ui_ecran = Ui_MainWindow()
#     ui_ecran.setupUi(ecran)
#     ecran.show()
#     sys.exit(app.exec())