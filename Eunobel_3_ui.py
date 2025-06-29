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
from PySide6 import QtSql
from tkinter import messagebox
import ressources_rc
import sys
import sqlite3



class EcranPrincipal(object):
      
    def setupUi(self, MainWindow):
        
        def produit_function():
            self.stackWidgetMain.setCurrentIndex(0)
            conn = sqlite3.connect('Gestion.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM produits""")
            data = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            conn.close()
            
            self.table_produit.setRowCount(len(data))
            self.table_produit.setColumnCount(len(columns))
            self.table_produit.setHorizontalHeaderLabels(columns)
            
            for row_index, row_data in enumerate(data):
                for col_index, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.table_produit.setItem(row_index, col_index, item)
        
        def fournisseurs_function():
            self.stackWidgetMain.setCurrentIndex(1)  
            conn = sqlite3.connect('Gestion.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM fournisseurs""")
            data = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            conn.close()
            
            self.table_fournisseur.setRowCount(len(data))
            self.table_fournisseur.setColumnCount(len(columns))
            self.table_fournisseur.setHorizontalHeaderLabels(columns)
            
            for row_index, row_data in enumerate(data):
                for col_index, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.table_fournisseur.setItem(row_index, col_index, item)     
        
        def client_function():
            self.stackWidgetMain.setCurrentIndex(2)  
            conn = sqlite3.connect('Gestion.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM client""")
            data = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            conn.close()
            
            self.table_client.setRowCount(len(data))
            self.table_client.setColumnCount(len(columns))
            self.table_client.setHorizontalHeaderLabels(columns)
            
            for row_index, row_data in enumerate(data):
                for col_index, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.table_client.setItem(row_index, col_index, item)
        
        def fonction_entrepot():
            self.stackWidgetMain.setCurrentIndex(3)  
            conn = sqlite3.connect('Gestion.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM entrepots""")
            data = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            conn.close()
            
            self.table_entrepot.setRowCount(len(data))
            self.table_entrepot.setColumnCount(len(columns))
            self.table_entrepot.setHorizontalHeaderLabels(columns)
            
            for row_index, row_data in enumerate(data):
                for col_index, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.table_entrepot.setItem(row_index, col_index, item)
        
        def fonction_entree():
            self.stackWidgetMain.setCurrentIndex(5)  
            conn = sqlite3.connect('Gestion.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM entrees""")
            data = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            conn.close()
            
            self.page_entree.setRowCount(len(data))
            self.page_entree.setColumnCount(len(columns))
            self.page_entree.setHorizontalHeaderLabels(columns)
            
            for row_index, row_data in enumerate(data):
                for col_index, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.page_entree.setItem(row_index, col_index, item)
        
        def fonction_stocks():
            self.stackWidgetMain.setCurrentIndex(4)  
            conn = sqlite3.connect('Gestion.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM stocks""")
            data = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            conn.close()
            
            self.table_stocks.setRowCount(len(data))
            self.table_stocks.setColumnCount(len(columns))
            self.table_stocks.setHorizontalHeaderLabels(columns)
            
            for row_index, row_data in enumerate(data):
                for col_index, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.table_stocks.setItem(row_index, col_index, item)
        
        def fonction_sorties():
            self.stackWidgetMain.setCurrentIndex(6)  
            conn = sqlite3.connect('Gestion.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM sorties""")
            data = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            conn.close()
            
            self.table_de_sorties.setRowCount(len(data))
            self.table_de_sorties.setColumnCount(len(columns))
            self.table_de_sorties.setHorizontalHeaderLabels(columns)
            
            for row_index, row_data in enumerate(data):
                for col_index, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.table_de_sorties.setItem(row_index, col_index, item)
        
        def fonction_commande_cf():
            self.stackWidgetMain.setCurrentIndex(7)  
            conn = sqlite3.connect('Gestion.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM commande_fournisseur""")
            data = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            conn.close()
            
            self.table_cf.setRowCount(len(data))
            self.table_cf.setColumnCount(len(columns))
            self.table_cf.setHorizontalHeaderLabels(columns)
            
            for row_index, row_data in enumerate(data):
                for col_index, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.table_cf.setItem(row_index, col_index, item)
        
        def fonction_commande_cli():
            self.stackWidgetMain.setCurrentIndex(8)  
            conn = sqlite3.connect('Gestion.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM commande_client""")
            data = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            conn.close()
            
            self.table_commande_cli.setRowCount(len(data))
            self.table_commande_cli.setColumnCount(len(columns))
            self.table_commande_cli.setHorizontalHeaderLabels(columns)
            
            for row_index, row_data in enumerate(data):
                for col_index, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.table_commande_cli.setItem(row_index, col_index, item)
        
        
        def fonction_utilisateur():
            self.stackWidgetMain.setCurrentIndex(9)  
            conn = sqlite3.connect('Gestion.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM utilisateur""")
            data = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            conn.close()
            
            self.table_utilisateur.setRowCount(len(data))
            self.table_utilisateur.setColumnCount(len(columns))
            self.table_utilisateur.setHorizontalHeaderLabels(columns)
            
            for row_index, row_data in enumerate(data):
                for col_index, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.table_utilisateur.setItem(row_index, col_index, item)
        
        # def close_window():
        #     EcranPrincipal.close()     
        
        # def fullscreen_fc():
        #     MainWindow.showFullScreen()   
        
        # def normalscreen():
        #     MainWindow.showNormal()     
                         
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(970, 584)
        MainWindow.setStyleSheet(u"")
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0,0,0,0)
        self.horizontalLayout.setSpacing(0)
        self.sidebar = QWidget(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMinimumSize(QSize(200, 0))
        self.sidebar.setMaximumSize(QSize(200, 16777215))
        self.sidebar.setStyleSheet(u"QWidget{\n"
"     background:#1c1c1c;\n"
"	 color: #fff;\n"
"	 font-weight: 900;\n"
"	 font-size: 12px; \n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align: left;\n"
"	padding: 10px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	text-align: left;\n"
"	padding: 5px;\n"
"	border: none;\n"
"	background: #fff;\n"
"	color: #1c1c1c;\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	text-align: left;\n"
"	padding: 5px;\n"
"	border: none;\n"
"	background: #fff;\n"
"	color: #1c1c1c;\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QLabel{\n"
"	font-size: 17px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 0, 10)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.sidebar)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/images/images/logo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_3 = QLabel(self.sidebar)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.sidebar)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.produit_btn = QPushButton(self.sidebar)
        self.produit_btn.setObjectName(u"produit_btn")
        self.produit_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/images/images/produits.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.produit_btn.setIcon(icon)
        self.produit_btn.setIconSize(QSize(20, 20))
        self.produit_btn.setCheckable(True)
        self.produit_btn.setAutoExclusive(True)
        self.produit_btn.clicked.connect(produit_function)

        self.verticalLayout.addWidget(self.produit_btn)

        self.fournisseurs_btn = QPushButton(self.sidebar)
        self.fournisseurs_btn.setObjectName(u"fournisseurs_btn")
        self.fournisseurs_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/fournisseurs.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.fournisseurs_btn.setIcon(icon1)
        self.fournisseurs_btn.setIconSize(QSize(20, 20))
        self.fournisseurs_btn.setCheckable(True)
        self.fournisseurs_btn.setAutoExclusive(True)
        self.fournisseurs_btn.clicked.connect(fournisseurs_function)

        self.verticalLayout.addWidget(self.fournisseurs_btn)

        self.clients_btn = QPushButton(self.sidebar)
        self.clients_btn.setObjectName(u"clients_btn")
        self.clients_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/images/images/clients.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clients_btn.setIcon(icon2)
        self.clients_btn.setIconSize(QSize(20, 20))
        self.clients_btn.setCheckable(True)
        self.clients_btn.setAutoExclusive(True)
        self.clients_btn.clicked.connect(client_function)

        self.verticalLayout.addWidget(self.clients_btn)

        self.entrepots_btn = QPushButton(self.sidebar)
        self.entrepots_btn.setObjectName(u"entrepots_btn")
        self.entrepots_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/images/images/store.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.entrepots_btn.setIcon(icon3)
        self.entrepots_btn.setIconSize(QSize(20, 20))
        self.entrepots_btn.setCheckable(True)
        self.entrepots_btn.setAutoExclusive(True)
        self.entrepots_btn.clicked.connect(fonction_entrepot)

        self.verticalLayout.addWidget(self.entrepots_btn)

        self.stocks_btn = QPushButton(self.sidebar)
        self.stocks_btn.setObjectName(u"stocks_btn")
        self.stocks_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/images/images/stocks.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stocks_btn.setIcon(icon4)
        self.stocks_btn.setIconSize(QSize(20, 20))
        self.stocks_btn.setCheckable(True)
        self.stocks_btn.setAutoExclusive(True)
        self.stocks_btn.clicked.connect(fonction_stocks)

        self.verticalLayout.addWidget(self.stocks_btn)

        self.entrees_btn = QPushButton(self.sidebar)
        self.entrees_btn.setObjectName(u"entrees_btn")
        self.entrees_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/images/images/entrees.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.entrees_btn.setIcon(icon5)
        self.entrees_btn.setIconSize(QSize(20, 20))
        self.entrees_btn.setCheckable(True)
        self.entrees_btn.setAutoExclusive(True)
        self.entrees_btn.clicked.connect(fonction_entree)

        self.verticalLayout.addWidget(self.entrees_btn)

        self.sorties_btn = QPushButton(self.sidebar)
        self.sorties_btn.setObjectName(u"sorties_btn")
        self.sorties_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/images/images/sortie.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sorties_btn.setIcon(icon6)
        self.sorties_btn.setIconSize(QSize(22, 22))
        self.sorties_btn.setCheckable(True)
        self.sorties_btn.setAutoExclusive(True)
        self.sorties_btn.clicked.connect(fonction_sorties)

        self.verticalLayout.addWidget(self.sorties_btn)

        self.commandes_fournisseurs_btn = QPushButton(self.sidebar)
        self.commandes_fournisseurs_btn.setObjectName(u"commandes_fournisseurs_btn")
        self.commandes_fournisseurs_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/images/images/commande_fournisseurs.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.commandes_fournisseurs_btn.setIcon(icon7)
        self.commandes_fournisseurs_btn.setIconSize(QSize(20, 20))
        self.commandes_fournisseurs_btn.setCheckable(True)
        self.commandes_fournisseurs_btn.setAutoExclusive(True)
        self.commandes_fournisseurs_btn.clicked.connect(fonction_commande_cf)
        
        self.verticalLayout.addWidget(self.commandes_fournisseurs_btn)

        self.commandes_clients_btn = QPushButton(self.sidebar)
        self.commandes_clients_btn.setObjectName(u"commandes_clients_btn")
        self.commandes_clients_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/images/images/commande_client.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.commandes_clients_btn.setIcon(icon8)
        self.commandes_clients_btn.setIconSize(QSize(22, 22))
        self.commandes_clients_btn.setCheckable(True)
        self.commandes_clients_btn.setAutoExclusive(True)
        self.commandes_clients_btn.clicked.connect(fonction_commande_cli)

        self.verticalLayout.addWidget(self.commandes_clients_btn)

        self.utilisateurs_btn = QPushButton(self.sidebar)
        self.utilisateurs_btn.setObjectName(u"utilisateurs_btn")
        self.utilisateurs_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/images/images/utilisateurs.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.utilisateurs_btn.setIcon(icon9)
        self.utilisateurs_btn.setIconSize(QSize(20, 20))
        self.utilisateurs_btn.setCheckable(True)
        self.utilisateurs_btn.setAutoExclusive(True)
        self.utilisateurs_btn.clicked.connect(fonction_utilisateur)

        self.verticalLayout.addWidget(self.utilisateurs_btn)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 107, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.deconnecter_btn = QPushButton(self.sidebar)
        self.deconnecter_btn.setObjectName(u"deconnecter_btn")
        self.deconnecter_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/images/images/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.deconnecter_btn.setIcon(icon10)
        self.deconnecter_btn.setIconSize(QSize(22, 22))
        self.deconnecter_btn.setCheckable(True)
        self.deconnecter_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.deconnecter_btn)


        self.horizontalLayout.addWidget(self.sidebar)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toolbar = QWidget(self.widget_2)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMinimumSize(QSize(0, 50))
        self.toolbar.setMaximumSize(QSize(16777215, 50))
        self.toolbar.setStyleSheet(u"QWidget{\n"
"     background: #1c1c1c;\n"
"	color: #fff;\n"
"	font-weight: 900;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton#search_btn{\n"
"	border: none;\n"
"	background: #fff;\n"
"	padding: 6px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background: #fff;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"")
        self.horizontalLayout_5 = QHBoxLayout(self.toolbar)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.toolbar)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(83, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.search_session = QHBoxLayout()
        self.search_session.setSpacing(0)
        self.search_session.setObjectName(u"search_session")
        self.search_input = QLineEdit(self.toolbar)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setMinimumSize(QSize(250, 0))
        self.search_input.setMaximumSize(QSize(300, 16777215))
        self.search_input.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.search_input.setStyleSheet(u"border: none;")

        self.search_session.addWidget(self.search_input)

        self.search_btn = QPushButton(self.toolbar)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setMinimumSize(QSize(50, 0))
        self.search_btn.setMaximumSize(QSize(50, 16777215))
        self.search_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.search_btn.setStyleSheet(u"border: none;")
        icon11 = QIcon()
        icon11.addFile(u":/images/images/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_btn.setIcon(icon11)
        self.search_btn.setCheckable(True)
        self.search_btn.setAutoExclusive(True)

        self.search_session.addWidget(self.search_btn)


        self.horizontalLayout_5.addLayout(self.search_session)

        self.horizontalSpacer_4 = QSpacerItem(83, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.hide_screen_btn = QPushButton(self.toolbar)
        self.hide_screen_btn.setObjectName(u"hide_screen_btn")
        self.hide_screen_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/images/images/hide.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.hide_screen_btn.setIcon(icon12)
        self.hide_screen_btn.setCheckable(True)
        self.hide_screen_btn.setAutoExclusive(True)
        # self.hide_screen_btn.clicked.connect(normalscreen)

        self.horizontalLayout_4.addWidget(self.hide_screen_btn)

        self.fullscreen_btn = QPushButton(self.toolbar)
        self.fullscreen_btn.setObjectName(u"fullscreen_btn")
        self.fullscreen_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/images/images/square.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.fullscreen_btn.setIcon(icon13)
        self.fullscreen_btn.setCheckable(True)
        self.fullscreen_btn.setAutoExclusive(True)
        # self.fullscreen_btn.clicked.connect(fullscreen_fc)

        self.horizontalLayout_4.addWidget(self.fullscreen_btn)

        self.close_btn = QPushButton(self.toolbar)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/images/images/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon14)
        self.close_btn.setCheckable(True)
        self.close_btn.setAutoExclusive(True)
        # self.close_btn.clicked.connect(close_window)

        self.horizontalLayout_4.addWidget(self.close_btn)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addWidget(self.toolbar)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackWidgetMain = QStackedWidget(self.widget)
        self.stackWidgetMain.setObjectName(u"stackWidgetMain")
        self.stackWidgetMain.setStyleSheet(u"background: #fff;color:#333;")
        self.stackWidgetMain.setFont(QFont('fantasy', pointSize=20, weight=900, italic=True))
        self.page_produit = QWidget()
        self.page_produit.setObjectName(u"page_produit")
        self.horizontalLayout_9 = QHBoxLayout(self.page_produit)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        # self.horizontalLayout_9.setContentsMargins(0,0,0,0)
        # self.horizontalLayout_9.setSpacing(0)
        self.page_produit1 = QWidget(self.page_produit)
        self.page_produit1.setObjectName(u"page_produit1")
        self.horizontalLayout_6 = QHBoxLayout(self.page_produit1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.page_produit1)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.table_produit = QTableWidget(self.widget_5)
        if (self.table_produit.columnCount() < 9):
            self.table_produit.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_produit.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_produit.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_produit.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_produit.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_produit.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_produit.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_produit.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_produit.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_produit.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.table_produit.setObjectName(u"table_produit")
        self.table_produit.setInputMethodHints(Qt.ImhNone)
        self.table_produit.setAlternatingRowColors(True)
        self.table_produit.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout_8.addWidget(self.table_produit)


        self.verticalLayout_4.addWidget(self.widget_5)


        self.horizontalLayout_6.addWidget(self.widget_3)


        self.horizontalLayout_9.addWidget(self.page_produit1)

        self.stackWidgetMain.addWidget(self.page_produit)
        self.page_fournisseur = QWidget()
        self.page_fournisseur.setObjectName(u"page_fournisseur")
        self.horizontalLayout_10 = QHBoxLayout(self.page_fournisseur)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.page_fournisseur1 = QWidget(self.page_fournisseur)
        self.page_fournisseur1.setObjectName(u"page_fournisseur1")
        self.verticalLayout_5 = QVBoxLayout(self.page_fournisseur1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.page_fournisseur1)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.table_fournisseur = QTableWidget(self.widget_7)
        if (self.table_fournisseur.columnCount() < 5):
            self.table_fournisseur.setColumnCount(5)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_fournisseur.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_fournisseur.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_fournisseur.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_fournisseur.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_fournisseur.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        self.table_fournisseur.setObjectName(u"table_fournisseur")

        self.horizontalLayout_12.addWidget(self.table_fournisseur)


        self.verticalLayout_5.addWidget(self.widget_7)


        self.horizontalLayout_10.addWidget(self.page_fournisseur1)

        self.stackWidgetMain.addWidget(self.page_fournisseur)
        self.page_client = QWidget()
        self.page_client.setObjectName(u"page_client")
        self.horizontalLayout_13 = QHBoxLayout(self.page_client)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.page_client1 = QWidget(self.page_client)
        self.page_client1.setObjectName(u"page_client1")
        self.verticalLayout_6 = QVBoxLayout(self.page_client1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.page_client1)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.table_client = QTableWidget(self.widget_6)
        if (self.table_client.columnCount() < 5):
            self.table_client.setColumnCount(5)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_client.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_client.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_client.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_client.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_client.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        self.table_client.setObjectName(u"table_client")

        self.horizontalLayout_15.addWidget(self.table_client)


        self.verticalLayout_6.addWidget(self.widget_6)


        self.horizontalLayout_13.addWidget(self.page_client1)

        self.stackWidgetMain.addWidget(self.page_client)
        self.page_entrepots = QWidget()
        self.page_entrepots.setObjectName(u"page_entrepots")
        self.horizontalLayout_16 = QHBoxLayout(self.page_entrepots)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.widget_4 = QWidget(self.page_entrepots)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_7 = QVBoxLayout(self.widget_4)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.table_entrepot = QTableWidget(self.widget_8)
        if (self.table_entrepot.columnCount() < 3):
            self.table_entrepot.setColumnCount(3)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_entrepot.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_entrepot.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_entrepot.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        self.table_entrepot.setObjectName(u"table_entrepot")

        self.horizontalLayout_18.addWidget(self.table_entrepot)


        self.verticalLayout_7.addWidget(self.widget_8)


        self.horizontalLayout_16.addWidget(self.widget_4)

        self.stackWidgetMain.addWidget(self.page_entrepots)
        self.page_de_stocks = QWidget()
        self.page_de_stocks.setObjectName(u"page_de_stocks")
        self.horizontalLayout_19 = QHBoxLayout(self.page_de_stocks)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.page_stocks = QWidget(self.page_de_stocks)
        self.page_stocks.setObjectName(u"page_stocks")
        self.verticalLayout_8 = QVBoxLayout(self.page_stocks)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.page_stocks)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.table_stocks = QTableWidget(self.widget_10)
        if (self.table_stocks.columnCount() < 4):
            self.table_stocks.setColumnCount(4)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_stocks.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_stocks.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_stocks.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_stocks.setHorizontalHeaderItem(3, __qtablewidgetitem25)
        self.table_stocks.setObjectName(u"table_stocks")

        self.horizontalLayout_21.addWidget(self.table_stocks)


        self.verticalLayout_8.addWidget(self.widget_10)


        self.horizontalLayout_19.addWidget(self.page_stocks)

        self.stackWidgetMain.addWidget(self.page_de_stocks)
        self.page_des_entrees = QWidget()
        self.page_des_entrees.setObjectName(u"page_des_entrees")
        self.horizontalLayout_20 = QHBoxLayout(self.page_des_entrees)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.page_des_entrees1 = QWidget(self.page_des_entrees)
        self.page_des_entrees1.setObjectName(u"page_des_entrees1")
        self.verticalLayout_9 = QVBoxLayout(self.page_des_entrees1)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.page_des_entrees1)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.page_entree = QTableWidget(self.widget_11)
        if (self.page_entree.columnCount() < 6):
            self.page_entree.setColumnCount(6)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.page_entree.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.page_entree.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.page_entree.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.page_entree.setHorizontalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.page_entree.setHorizontalHeaderItem(4, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.page_entree.setHorizontalHeaderItem(5, __qtablewidgetitem31)
        self.page_entree.setObjectName(u"page_entree")

        self.horizontalLayout_23.addWidget(self.page_entree)


        self.verticalLayout_9.addWidget(self.widget_11)


        self.horizontalLayout_20.addWidget(self.page_des_entrees1)

        self.stackWidgetMain.addWidget(self.page_des_entrees)
        self.page_de_sortie = QWidget()
        self.page_de_sortie.setObjectName(u"page_de_sortie")
        self.horizontalLayout_40 = QHBoxLayout(self.page_de_sortie)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.page_de_sorties = QWidget(self.page_de_sortie)
        self.page_de_sorties.setObjectName(u"page_de_sorties")
        self.verticalLayout_10 = QVBoxLayout(self.page_de_sorties)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.page_de_sorties)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.table_de_sorties = QTableWidget(self.widget_12)
        if (self.table_de_sorties.columnCount() < 6):
            self.table_de_sorties.setColumnCount(6)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.table_de_sorties.setHorizontalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.table_de_sorties.setHorizontalHeaderItem(1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.table_de_sorties.setHorizontalHeaderItem(2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.table_de_sorties.setHorizontalHeaderItem(3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.table_de_sorties.setHorizontalHeaderItem(4, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.table_de_sorties.setHorizontalHeaderItem(5, __qtablewidgetitem37)
        self.table_de_sorties.setObjectName(u"table_de_sorties")

        self.horizontalLayout_25.addWidget(self.table_de_sorties)


        self.verticalLayout_10.addWidget(self.widget_12)


        self.horizontalLayout_40.addWidget(self.page_de_sorties)

        self.stackWidgetMain.addWidget(self.page_de_sortie)
        self.page_commade_fournisseurs = QWidget()
        self.page_commade_fournisseurs.setObjectName(u"page_commade_fournisseurs")
        self.verticalLayout_22 = QVBoxLayout(self.page_commade_fournisseurs)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.widget_9 = QWidget(self.page_commade_fournisseurs)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_11 = QVBoxLayout(self.widget_9)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.widget_9)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.table_cf = QTableWidget(self.widget_13)
        if (self.table_cf.columnCount() < 4):
            self.table_cf.setColumnCount(4)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.table_cf.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.table_cf.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.table_cf.setHorizontalHeaderItem(2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.table_cf.setHorizontalHeaderItem(3, __qtablewidgetitem41)
        self.table_cf.setObjectName(u"table_cf")

        self.horizontalLayout_26.addWidget(self.table_cf)


        self.verticalLayout_11.addWidget(self.widget_13)


        self.verticalLayout_22.addWidget(self.widget_9)

        self.stackWidgetMain.addWidget(self.page_commade_fournisseurs)
        self.page_commade_client = QWidget()
        self.page_commade_client.setObjectName(u"page_commade_client")
        self.horizontalLayout_22 = QHBoxLayout(self.page_commade_client)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.widget_14 = QWidget(self.page_commade_client)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_12 = QVBoxLayout(self.widget_14)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_15 = QWidget(self.widget_14)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.table_commande_cli = QTableWidget(self.widget_15)
        if (self.table_commande_cli.columnCount() < 4):
            self.table_commande_cli.setColumnCount(4)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.table_commande_cli.setHorizontalHeaderItem(0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.table_commande_cli.setHorizontalHeaderItem(1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.table_commande_cli.setHorizontalHeaderItem(2, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.table_commande_cli.setHorizontalHeaderItem(3, __qtablewidgetitem45)
        self.table_commande_cli.setObjectName(u"table_commande_cli")

        self.horizontalLayout_27.addWidget(self.table_commande_cli)


        self.verticalLayout_12.addWidget(self.widget_15)


        self.horizontalLayout_22.addWidget(self.widget_14)

        self.stackWidgetMain.addWidget(self.page_commade_client)
        self.page_utiisateur = QWidget()
        self.page_utiisateur.setObjectName(u"page_utiisateur")
        self.verticalLayout_13 = QVBoxLayout(self.page_utiisateur)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_16 = QWidget(self.page_utiisateur)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(0, 48))
        self.widget_16.setMaximumSize(QSize(16777215, 48))
        self.widget_16.setStyleSheet(u"background: #4b7bb2;\n"
"color: #fff;")
        self.verticalLayout_14 = QVBoxLayout(self.widget_16)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_14 = QLabel(self.widget_16)
        self.label_14.setObjectName(u"label_14")
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label_14.setFont(font)

        self.verticalLayout_14.addWidget(self.label_14, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.page_utiisateur)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_15 = QVBoxLayout(self.widget_17)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.table_utilisateur = QTableWidget(self.widget_17)
        if (self.table_utilisateur.columnCount() < 3):
            self.table_utilisateur.setColumnCount(3)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.table_utilisateur.setHorizontalHeaderItem(0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.table_utilisateur.setHorizontalHeaderItem(1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.table_utilisateur.setHorizontalHeaderItem(2, __qtablewidgetitem48)
        self.table_utilisateur.setObjectName(u"table_utilisateur")

        self.verticalLayout_15.addWidget(self.table_utilisateur)


        self.verticalLayout_13.addWidget(self.widget_17)

        self.stackWidgetMain.addWidget(self.page_utiisateur)

        self.horizontalLayout_3.addWidget(self.stackWidgetMain)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackWidgetMain.setCurrentIndex(9)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
        fonction_utilisateur()
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"EunObel", None))
        self.produit_btn.setText(QCoreApplication.translate("MainWindow", u"Produits", None))
        self.fournisseurs_btn.setText(QCoreApplication.translate("MainWindow", u"Fournisseurs", None))
        self.clients_btn.setText(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.entrepots_btn.setText(QCoreApplication.translate("MainWindow", u"Entrepots", None))
        self.stocks_btn.setText(QCoreApplication.translate("MainWindow", u"Stocks", None))
        self.entrees_btn.setText(QCoreApplication.translate("MainWindow", u"Entrees", None))
        self.sorties_btn.setText(QCoreApplication.translate("MainWindow", u"Sorties", None))
        self.commandes_fournisseurs_btn.setText(QCoreApplication.translate("MainWindow", u"Commandes Fournisseurs", None))
        self.commandes_clients_btn.setText(QCoreApplication.translate("MainWindow", u"Commandes Clients", None))
        self.utilisateurs_btn.setText(QCoreApplication.translate("MainWindow", u"Utilisateurs", None))
        self.deconnecter_btn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"EunObel", None))
        self.search_btn.setText("")
        self.hide_screen_btn.setText("")
        self.fullscreen_btn.setText("")
        self.close_btn.setText("")
        ___qtablewidgetitem = self.table_produit.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID Produit", None));
        ___qtablewidgetitem1 = self.table_produit.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem2 = self.table_produit.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Code Barres", None));
        ___qtablewidgetitem3 = self.table_produit.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ID Categorie", None));
        ___qtablewidgetitem4 = self.table_produit.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Nouvelle colonne", None));
        ___qtablewidgetitem5 = self.table_produit.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Prix d'achat", None));
        ___qtablewidgetitem6 = self.table_produit.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Prix de Vente", None));
        ___qtablewidgetitem7 = self.table_produit.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Seuil d'alerte", None));
        ___qtablewidgetitem8 = self.table_produit.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Nom Produit", None));
        ___qtablewidgetitem9 = self.table_fournisseur.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"ID Fournisseur", None));
        ___qtablewidgetitem10 = self.table_fournisseur.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Nom Fournisseur", None));
        ___qtablewidgetitem11 = self.table_fournisseur.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Adresse", None));
        ___qtablewidgetitem12 = self.table_fournisseur.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Telephone", None));
        ___qtablewidgetitem13 = self.table_fournisseur.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem14 = self.table_client.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"ID Client", None));
        ___qtablewidgetitem15 = self.table_client.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Nom Client", None));
        ___qtablewidgetitem16 = self.table_client.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Adresse", None));
        ___qtablewidgetitem17 = self.table_client.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Telephone", None));
        ___qtablewidgetitem18 = self.table_client.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem19 = self.table_entrepot.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"ID Entrepot", None));
        ___qtablewidgetitem20 = self.table_entrepot.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Nom Entrepot", None));
        ___qtablewidgetitem21 = self.table_entrepot.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Adresse", None));
        ___qtablewidgetitem22 = self.table_stocks.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"ID Stocks", None));
        ___qtablewidgetitem23 = self.table_stocks.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"ID Produit", None));
        ___qtablewidgetitem24 = self.table_stocks.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"ID Entrepot", None));
        ___qtablewidgetitem25 = self.table_stocks.horizontalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Quantite", None));
        ___qtablewidgetitem26 = self.page_entree.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"ID Entree", None));
        ___qtablewidgetitem27 = self.page_entree.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"ID Fournisseur", None));
        ___qtablewidgetitem28 = self.page_entree.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Date Entree", None));
        ___qtablewidgetitem29 = self.page_entree.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"ID Produit", None));
        ___qtablewidgetitem30 = self.page_entree.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Nouvelle colonne", None));
        ___qtablewidgetitem31 = self.page_entree.horizontalHeaderItem(5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"ID Entrepot", None));
        ___qtablewidgetitem32 = self.table_de_sorties.horizontalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"ID Sorties", None));
        ___qtablewidgetitem33 = self.table_de_sorties.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"ID Client", None));
        ___qtablewidgetitem34 = self.table_de_sorties.horizontalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Date de Sortie", None));
        ___qtablewidgetitem35 = self.table_de_sorties.horizontalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"ID Produit", None));
        ___qtablewidgetitem36 = self.table_de_sorties.horizontalHeaderItem(4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Quantite", None));
        ___qtablewidgetitem37 = self.table_de_sorties.horizontalHeaderItem(5)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"ID Entrepot", None));
        ___qtablewidgetitem38 = self.table_cf.horizontalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"ID Commandes Fournisseurs", None));
        ___qtablewidgetitem39 = self.table_cf.horizontalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"ID Fournisseur", None));
        ___qtablewidgetitem40 = self.table_cf.horizontalHeaderItem(2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Date de commande", None));
        ___qtablewidgetitem41 = self.table_cf.horizontalHeaderItem(3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Statut", None));
        ___qtablewidgetitem42 = self.table_commande_cli.horizontalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"ID Commandes Client", None));
        ___qtablewidgetitem43 = self.table_commande_cli.horizontalHeaderItem(1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"ID Client", None));
        ___qtablewidgetitem44 = self.table_commande_cli.horizontalHeaderItem(2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Date Commande", None));
        ___qtablewidgetitem45 = self.table_commande_cli.horizontalHeaderItem(3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Statut ", None));
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Utilisateurs", None))
        ___qtablewidgetitem46 = self.table_utilisateur.horizontalHeaderItem(0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"ID Utilisateur", None));
        ___qtablewidgetitem47 = self.table_utilisateur.horizontalHeaderItem(1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Nom Utilisateur", None));
        ___qtablewidgetitem48 = self.table_utilisateur.horizontalHeaderItem(2)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Role", None));
    # retranslateUi

if __name__=='__main__':
    app =QApplication(sys.argv)
    ecran = QMainWindow()
    ui_ecran = EcranPrincipal()
    ui_ecran.setupUi(ecran)
    ecran.show()
    sys.exit(app.exec())
