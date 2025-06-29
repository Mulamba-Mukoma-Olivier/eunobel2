from PySide6.QtWidgets import * 
from formulaire_entrepot_ui import Ui_MainWindow
from tkinter import messagebox
import sqlite3

class Logique_entrepot(QMainWindow):
    def __init__(self):
        def entrepot_function():
            id_entrepot = self.ui_ecran.id_entrepot_input.text()
            nom_entrepot = self.ui_ecran.nom_entrepot_input.text()
            adresse_entrepots = self.ui_ecran.adresse_entrepot_input.text()
            
            try:
                conn = sqlite3.connect('Gestion.db')
                cursor = conn.cursor()

                if id_entrepot != '' and nom_entrepot != '' and adresse_entrepots != '':
                    cursor.execute("""INSERT INTO 
                                        entrepots(id_entrepot, nom_entrepot, adresse)
                                        VALUES
                                        (?,?,?)
                                    """, (id_entrepot, nom_entrepot, adresse_entrepots))
                    conn.commit()
                    messagebox.showinfo(title='SUCCESS', message=f'Le client {nom_entrepot} a été ajouté avec succès!!')
                else:
                    messagebox.showerror(title='ERREUR', message='Le ou les champs semblent être vides, veuillez vérifier SVP')
                
                conn.close()

                # Clear the input fields after successful insertion
                self.ui_ecran.id_entrepot_input.setText('')
                self.ui_ecran.nom_entrepot_input.setText('')
                self.ui_ecran.adresse_entrepot_input.setText('')
                
            except sqlite3.Error as e:
                messagebox.showerror(title='FAILURE', message=f'Échec d\'enregistrement: {e}')
        super().__init__()
        self.ui_ecran = Ui_MainWindow()
        self.ui_ecran.setupUi(self)
        
        self.ui_ecran.save_entrepot_btn.clicked.connect(entrepot_function)
        
        