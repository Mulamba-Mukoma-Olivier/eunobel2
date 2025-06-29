from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import sys

class Ui_PageCentralisatrice(object):
    def setupUi(self, PageCentralisatrice):
        if not PageCentralisatrice.objectName():
            PageCentralisatrice.setObjectName(u"PageCentralisatrice")
        PageCentralisatrice.resize(800, 600)
        PageCentralisatrice.setStyleSheet(u"background: #333;")
        self.centralwidget = QWidget(PageCentralisatrice)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Stencil"])
        font.setPointSize(130)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #fff;")

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QPushButton{\n"
"	background: #fff;\n"
"	border: none;\n"
"	padding: 10px;\n"
"	border-top-left-radius: 35px;\n"
"	border-bottom-left-radius: 35px;\n"
"	border-top-right-radius: 35px;\n"
"	border-bottom-right-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: yellow;\n"
"}")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Accueil = QPushButton(self.widget)
        self.Accueil.setObjectName(u"Accueil")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.Accueil.setFont(font1)
        self.Accueil.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"./images/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Accueil.setIcon(icon)
        self.Accueil.setIconSize(QSize(50, 50))
        self.Accueil.setCheckable(True)
        self.Accueil.setAutoExclusive(True)

        self.gridLayout.addWidget(self.Accueil, 0, 0, 1, 1, Qt.AlignTop)

        self.Produits = QPushButton(self.widget)
        self.Produits.setObjectName(u"Produits")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.Produits.setFont(font2)
        self.Produits.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"./images/produits.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Produits.setIcon(icon1)
        self.Produits.setIconSize(QSize(50, 50))
        self.Produits.setCheckable(True)
        self.Produits.setAutoExclusive(True)

        self.gridLayout.addWidget(self.Produits, 0, 1, 1, 1)

        self.Clients = QPushButton(self.widget)
        self.Clients.setObjectName(u"Clients")
        self.Clients.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"./images/clients.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Clients.setIcon(icon2)
        self.Clients.setIconSize(QSize(50, 50))
        self.Clients.setCheckable(True)
        self.Clients.setAutoExclusive(True)

        self.gridLayout.addWidget(self.Clients, 0, 2, 1, 1)

        self.Entrepots = QPushButton(self.widget)
        self.Entrepots.setObjectName(u"Entrepots")
        self.Entrepots.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"./images/so.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Entrepots.setIcon(icon3)
        self.Entrepots.setIconSize(QSize(50, 50))
        self.Entrepots.setCheckable(True)
        self.Entrepots.setAutoExclusive(True)

        self.gridLayout.addWidget(self.Entrepots, 0, 3, 1, 1)

        self.Stocks = QPushButton(self.widget)
        self.Stocks.setObjectName(u"Stocks")
        self.Stocks.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"./images/stocks.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Stocks.setIcon(icon4)
        self.Stocks.setIconSize(QSize(50, 50))
        self.Stocks.setCheckable(True)
        self.Stocks.setAutoExclusive(True)

        self.gridLayout.addWidget(self.Stocks, 0, 4, 1, 1)

        self.Entrees = QPushButton(self.widget)
        self.Entrees.setObjectName(u"Entrees")
        self.Entrees.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"./images/entrees.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Entrees.setIcon(icon5)
        self.Entrees.setIconSize(QSize(50, 50))
        self.Entrees.setCheckable(True)
        self.Entrees.setAutoExclusive(True)

        self.gridLayout.addWidget(self.Entrees, 0, 5, 1, 1)

        self.Sorties = QPushButton(self.widget)
        self.Sorties.setObjectName(u"Sorties")
        self.Sorties.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"./images/sortie.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Sorties.setIcon(icon6)
        self.Sorties.setIconSize(QSize(50, 50))
        self.Sorties.setCheckable(True)
        self.Sorties.setAutoExclusive(True)

        self.gridLayout.addWidget(self.Sorties, 1, 0, 1, 1)

        self.CommandeFournisseur = QPushButton(self.widget)
        self.CommandeFournisseur.setObjectName(u"CommandeFournisseur")
        self.CommandeFournisseur.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u"./images/commande_fournisseurs.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.CommandeFournisseur.setIcon(icon7)
        self.CommandeFournisseur.setIconSize(QSize(50, 50))
        self.CommandeFournisseur.setCheckable(True)
        self.CommandeFournisseur.setAutoExclusive(True)

        self.gridLayout.addWidget(self.CommandeFournisseur, 1, 1, 1, 1)

        self.CommandeClients = QPushButton(self.widget)
        self.CommandeClients.setObjectName(u"CommandeClients")
        self.CommandeClients.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u"./images/commande_client.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.CommandeClients.setIcon(icon8)
        self.CommandeClients.setIconSize(QSize(50, 50))
        self.CommandeClients.setCheckable(True)
        self.CommandeClients.setAutoExclusive(True)

        self.gridLayout.addWidget(self.CommandeClients, 1, 2, 1, 1)

        self.Utilisateurs = QPushButton(self.widget)
        self.Utilisateurs.setObjectName(u"Utilisateurs")
        self.Utilisateurs.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u"./images/utilisateurs.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Utilisateurs.setIcon(icon9)
        self.Utilisateurs.setIconSize(QSize(50, 50))
        self.Utilisateurs.setCheckable(True)
        self.Utilisateurs.setAutoExclusive(True)

        self.gridLayout.addWidget(self.Utilisateurs, 1, 3, 1, 1)

        self.Fermeture = QPushButton(self.widget)
        self.Fermeture.setObjectName(u"Fermeture")
        self.Fermeture.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u"./images/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Fermeture.setIcon(icon10)
        self.Fermeture.setIconSize(QSize(50, 50))
        self.Fermeture.setCheckable(True)
        self.Fermeture.setAutoExclusive(True)

        self.gridLayout.addWidget(self.Fermeture, 1, 4, 1, 1)


        self.verticalLayout.addWidget(self.widget)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        PageCentralisatrice.setCentralWidget(self.centralwidget)

        self.retranslateUi(PageCentralisatrice)

        QMetaObject.connectSlotsByName(PageCentralisatrice)
    # setupUi

    def retranslateUi(self, PageCentralisatrice):
        PageCentralisatrice.setWindowTitle(QCoreApplication.translate("PageCentralisatrice", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("PageCentralisatrice", u"EunOBel", None))
#if QT_CONFIG(tooltip)
        self.Accueil.setToolTip(QCoreApplication.translate("PageCentralisatrice", u"<html><head/><body><p>Accueil</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Accueil.setText("")
#if QT_CONFIG(tooltip)
        self.Produits.setToolTip(QCoreApplication.translate("PageCentralisatrice", u"<html><head/><body><p>Produits</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Produits.setText("")
#if QT_CONFIG(tooltip)
        self.Clients.setToolTip(QCoreApplication.translate("PageCentralisatrice", u"<html><head/><body><p>Clients</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Clients.setText("")
#if QT_CONFIG(tooltip)
        self.Entrepots.setToolTip(QCoreApplication.translate("PageCentralisatrice", u"<html><head/><body><p>Entrepots</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Entrepots.setText("")
#if QT_CONFIG(tooltip)
        self.Stocks.setToolTip(QCoreApplication.translate("PageCentralisatrice", u"<html><head/><body><p>Stocks</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Stocks.setText("")
#if QT_CONFIG(tooltip)
        self.Entrees.setToolTip(QCoreApplication.translate("PageCentralisatrice", u"<html><head/><body><p>Entrees</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Entrees.setText("")
#if QT_CONFIG(tooltip)
        self.Sorties.setToolTip(QCoreApplication.translate("PageCentralisatrice", u"<html><head/><body><p>Sorties</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Sorties.setText("")
#if QT_CONFIG(tooltip)
        self.CommandeFournisseur.setToolTip(QCoreApplication.translate("PageCentralisatrice", u"<html><head/><body><p>Commande Fournisseur</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.CommandeFournisseur.setText("")
#if QT_CONFIG(tooltip)
        self.CommandeClients.setToolTip(QCoreApplication.translate("PageCentralisatrice", u"<html><head/><body><p>Commande Client</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.CommandeClients.setText("")
#if QT_CONFIG(tooltip)
        self.Utilisateurs.setToolTip(QCoreApplication.translate("PageCentralisatrice", u"<html><head/><body><p>Utilisateurs</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Utilisateurs.setText("")
#if QT_CONFIG(tooltip)
        self.Fermeture.setToolTip(QCoreApplication.translate("PageCentralisatrice", u"<html><head/><body><p>Fermer la page</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Fermeture.setText("")
    # retranslateUi

if __name__=='__main__':
        app =QApplication(sys.argv)
        ecran = QMainWindow()
        ui_ecran = Ui_PageCentralisatrice()
        ui_ecran.setupUi(ecran)
        ecran.show()
        sys.exit(app.exec())
