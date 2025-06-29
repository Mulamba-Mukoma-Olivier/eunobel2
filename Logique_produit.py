from PySide6.QtWidgets import * 
from formulaire_produit_ui import Ui_MainWindow
import sqlite3
from tkinter import messagebox

class Logique_produit(QMainWindow):
    def __init__(self):
        def enregistrer_produit():
            id_produit = self.ui_ecran.id_produit_input.text()
            id_categorie = self.ui_ecran.id_categorie_produit_input.text()
            nom_produit = self.ui_ecran.nom_produit_input.text()
            prix_achat = self.ui_ecran.prix_achat_produit_input.text()
            description = self.ui_ecran.description_produit_input.text()
            prix_vente = self.ui_ecran.prix_vente_produit_input.text()
            code_barre = self.ui_ecran.code_barre_produit_input.text()
            seuil_alerte = self.ui_ecran.seuil_alerte_produit_input.text() 
            try:
                conn = sqlite3.connect('Gestion.db')
                cursor = conn.cursor()
                if id_produit=='' or id_categorie != '' or prix_achat !='' or prix_vente !='' or description !='' or code_barre !='' or seuil_alerte !='':
                    cursor.execute("""INSERT INTO 
                               produit(id_produit_, nom_produit, descriptions, code_barres, id_categorie, prix_achat, prix_vente, seuil_alerte)
                               VALUES
                               (?,?,?,?,?,?,?,?)
                               """, (id_produit, nom_produit, description, code_barre, id_categorie, prix_achat, prix_vente, seuil_alerte))
                    
                else:
                    messagebox.showerror(title='ERREUR', message='Le ou les champs semble etre vide, veiller svp')
                    
                conn.commit()
                conn.close()
                
                id_produit == '' 
                id_categorie == '' 
                nom_produit == '' 
                prix_achat == '' 
                description == '' 
                prix_vente == '' 
                code_barre == '' 
                seuil_alerte == ''
                
                messagebox.showinfo(title='SUCCESS', message=f'Le produit {nom_produit} a ete ajouter avec succes!!')
            except:
                messagebox.showerror(title='FAILURE', message=f'Echec d\'enregistrement')
                
        super().__init__()
        self.ui_ecran = Ui_MainWindow()
        self.ui_ecran.setupUi(self)
        #Declaration slot
        
        
        
        
        #Declaration action
        self.ui_ecran.save_produit_btn.clicked.connect(enregistrer_produit)
        
        
    
    
       
        
       