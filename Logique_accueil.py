from PySide6.QtWidgets import QMainWindow 
from Eunobel_3_ui import EcranPrincipal
import sys 

class Logique_accueil(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_ecran = EcranPrincipal()
        ui_ecran.setupUi(self)