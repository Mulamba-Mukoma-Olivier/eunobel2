from PySide6.QtWidgets import * 
from formulaire_sortie_ui import Ui_MainWindow 
from tkinter import messagebox 
import sqlite3


    
class Logique_sortie(QMainWindow):
    def __init__(self):
        def entree_fonction():
            id_client = self.ui_ecran.id_client_sortie_input.text()
            date_sortie = self.ui_ecran.date_sortie_input.text()
            id_produit = self.ui_ecran.id_produit_sortie_input.text()
            quantite = self.ui_ecran.quantite_sortie_input.text()
            id_entrepot = self.ui_ecran.id_entrepot_sortie_input.text()
            try:
                conn = sqlite3.connect('Gestion.db')
                cursor = conn.cursor()
                if id_client != '' or date_sortie !='' or id_produit !='' or quantite != '' or id_entrepot != '':
                    cursor.execute("""INSERT INTO 
                               sorties(id_client, date_sortie, id_produit, quantite, id_entrepot)
                               VALUES
                               (?,?,?,?,?)
                               """, (id_client, date_sortie, id_produit, quantite, id_entrepot))
                    
                else:
                    messagebox.showerror(title='ERREUR', message='Le ou les champs semble etre vide, veiller svp')
                    
                conn.commit()
                conn.close()
                
                self.ui_ecran.id_client_sortie_input.setText('')
                # self.ui_ecran.date_sortie_input.setDate('2000/01/01')
                self.ui_ecran.id_produit_sortie_input.setText('')
                self.ui_ecran.quantite_sortie_input.setText('')
                self.ui_ecran.id_entrepot_sortie_input.setText('')
                
                messagebox.showinfo(title='SUCCESS', message=f'Les entrees ont ete ajouter avec succes!!')
            except:
                messagebox.showerror(title='FAILURE', message=f'Echec d\'enregistrement')
        super().__init__()
        self.ui_ecran = Ui_MainWindow()
        self.ui_ecran.setupUi(self)
        
        self.ui_ecran.save_sortie_btn.clicked.connect(entree_fonction)