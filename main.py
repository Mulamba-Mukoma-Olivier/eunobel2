from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
from PageCentralisatrice_ui import Ui_PageCentralisatrice
from Logique_produit import Logique_produit
from Logique_fournisseur import Logique_fournisseur
from Logique_client import Logique_client
from Logique_entrepot import Logique_entrepot
from Logique_entree import Logique_entree
from Logique_stocks import Logique_stocks
from Logique_sortie import Logique_sortie
from Logique_cf import Logique_cf
from Logique_accueil import Logique_accueil
from Logique_commande_client import Logique_commande_client
from Logique_utilisateur import Logique_utilisateur
from Eunobel_3_ui import EcranPrincipal
import sys
from PySide6 import QtSql
from tkinter import messagebox
import ressources_rc
import sys
import sqlite3

class Logique_centrale(QMainWindow):
    def __init__(self):
         super().__init__()
         self.ui_ecran = Ui_PageCentralisatrice()
         self.ui_ecran.setupUi(self)

         # Ajout d'un QStackedWidget pour la navigation entre pages
         self.stacked_widget = QStackedWidget(self)
         self.setCentralWidget(self.stacked_widget)

         # Instanciation de toutes les pages logiques
         self.page_accueil = Logique_accueil()
         self.page_produit = Logique_produit()
         self.page_fournisseur = Logique_fournisseur()
         self.page_client = Logique_client()
         self.page_entrepot = Logique_entrepot()
         self.page_entree = Logique_entree()
         self.page_stocks = Logique_stocks()
         self.page_sortie = Logique_sortie()
         self.page_cf = Logique_cf()
         self.page_commande_client = Logique_commande_client()
         self.page_utilisateur = Logique_utilisateur()

         # Ajout des pages au QStackedWidget
         self.stacked_widget.addWidget(self.page_accueil)
         self.stacked_widget.addWidget(self.page_produit)
         self.stacked_widget.addWidget(self.page_fournisseur)
         self.stacked_widget.addWidget(self.page_client)
         self.stacked_widget.addWidget(self.page_entrepot)
         self.stacked_widget.addWidget(self.page_entree)
         self.stacked_widget.addWidget(self.page_stocks)
         self.stacked_widget.addWidget(self.page_sortie)
         self.stacked_widget.addWidget(self.page_cf)
         self.stacked_widget.addWidget(self.page_commande_client)
         self.stacked_widget.addWidget(self.page_utilisateur)

    def changer_page(self, index):
        self.stacked_widget.setCurrentIndex(index)
         
        
if __name__=='__main__':
    app = QApplication(sys.argv)
       
    ecran_p = Logique_centrale()
    ecran_p.show()
    sys.exit(app.exec())