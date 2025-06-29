from PySide6.QtWidgets import * 
from formulaire_fournisseur_ui import Ui_MainWindow
import sqlite3
from tkinter import messagebox

class Logique_fournisseur(QMainWindow):
    def __init__(self):

        def enregistrer_fournisseur():
            id_fournisseur = self.ui_ecran.id_fournisseur_input.text()
            nom_fournisseur = self.ui_ecran.nom_fournisseur_input.text()
            adresse_fournisseur = self.ui_ecran.adresse_fournisseur_input.text()
            telephone_fournisseur = self.ui_ecran.telephone_fournisseur_input.text()
            email_fournisseur = self.ui_ecran.email_fournisseur_input.text()
            
            if id_fournisseur and nom_fournisseur and adresse_fournisseur and telephone_fournisseur and email_fournisseur:
                try:
                    conn = sqlite3.connect('Gestion.db')
                    cursor = conn.cursor()
                    cursor.execute("""INSERT INTO fournisseurs (id_forunisseur, nom_forunisseur, adresse, telephone, email)
                                    VALUES (?, ?, ?, ?, ?)""",
                                (id_fournisseur, nom_fournisseur, adresse_fournisseur, telephone_fournisseur, email_fournisseur))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo(title='SUCCESS', message=f'Le fournisseur {nom_fournisseur} a été ajouté avec succès!!')
                except Exception as e:
                    messagebox.showerror(title='FAILURE', message=f'Échec de l\'enregistrement: {e}')
            else:
                messagebox.showerror(title='ERREUR', message='Un ou plusieurs champs semblent être vides, veuillez vérifier svp.')

            # Clear the input fields after successful submission
            self.ui_ecran.id_fournisseur_input.setText('')
            self.ui_ecran.nom_fournisseur_input.setText('')
            self.ui_ecran.adresse_fournisseur_input.setText('')
            self.ui_ecran.telephone_fournisseur_input.setText('')
            self.ui_ecran.email_fournisseur_input.setText('')



        super().__init__()
        self.ui_ecran = Ui_MainWindow()
        self.ui_ecran.setupUi(self)
        #Declaration slot
        
        
        
        
        #Declaration action
        self.ui_ecran.save_fournisseur_btn.clicked.connect(enregistrer_fournisseur)
        
        
    
    
       
        
       