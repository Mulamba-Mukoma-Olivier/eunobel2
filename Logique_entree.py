from PySide6.QtWidgets import * 
from formulaire_entree_ui import Ui_MainWindow 
from tkinter import messagebox 
import sqlite3


    
class Logique_entree(QMainWindow):
    def __init__(self):
        def entree_fonction():
            id_entree = self.ui_ecran.id_entree_fournisseur_input.text()
            date_entree = self.ui_ecran.date_entree_input.text()
            id_entree_produit = self.ui_ecran.id_entree_produit_input.text()
            quantite_entree = self.ui_ecran.quantite_entree_input.text()
            id_entree_entrepot = self.ui_ecran.id_entrepot_entree_input.text()
            try:
                conn = sqlite3.connect('Gestion.db')
                cursor = conn.cursor()
                if id_entree =='' or date_entree != '' or id_entree_produit !='' or quantite_entree !='' or id_entree_entrepot:
                    cursor.execute("""INSERT INTO 
                               entrees(id_fournisseur, date_entree, id_produit, quantite, id_entrepot)
                               VALUES
                               (?,?,?,?,?)
                               """, (id_entree, date_entree, id_entree_produit, quantite_entree, id_entree_entrepot))
                    
                else:
                    messagebox.showerror(title='ERREUR', message='Le ou les champs semble etre vide, veiller svp')
                    
                conn.commit()
                conn.close()
                
                self.ui_ecran.id_entree_fournisseur_input.text()
                self.ui_ecran.date_entree_input.text()
                self.ui_ecran.id_entree_produit_input.text()
                self.ui_ecran.quantite_entree_input.text()
                self.ui_ecran.id_entrepot_entree_input.text()
                
                messagebox.showinfo(title='SUCCESS', message=f'Les entrees ont ete ajouter avec succes!!')
            except:
                messagebox.showerror(title='FAILURE', message=f'Echec d\'enregistrement')
        super().__init__()
        self.ui_ecran = Ui_MainWindow()
        self.ui_ecran.setupUi(self)
        
        self.ui_ecran.save_entree_btn.clicked.connect(entree_fonction)