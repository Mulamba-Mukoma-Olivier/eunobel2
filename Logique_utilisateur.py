from formulaire_utilisateur_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow 
from tkinter import messagebox 
import sqlite3

class Logique_utilisateur(QMainWindow):
    def __init__(self):
        def fonction_utilisateur():
            nom_user = self.ui_ecran.nom_utilisateur_input.text()
            passwrd = self.ui_ecran.mot_de_passe_input.text()

            try:
                if nom_user != '' and passwrd != '':
                    conn = sqlite3.connect('Gestion.db')
                    cursor = conn.cursor()
                    cursor.execute("""INSERT INTO utilisateur (nom_utilisateur, mot_de_passe)
                        VALUES (?, ?)
                    """, (nom_user, passwrd))
                    conn.commit()
                    conn.close()

                    self.ui_ecran.nom_utilisateur_input.setText('')
                    self.ui_ecran.mot_de_passe_input.setText('')

                    messagebox.showinfo(title='SUCCESS', message='Les entrees ont ete ajouter avec succes!')
                else:
                    messagebox.showerror(title='ERREUR', message='Le ou les champs semblent être vides, veuillez remplir tous les champs.')
            except sqlite3.Error as e:
                messagebox.showerror(title='FAILURE', message=f'Echec d\'enregistrement: {str(e)}')

        super().__init__()
        self.ui_ecran = Ui_MainWindow()
        self.ui_ecran.setupUi(self)
        
        self.ui_ecran.save_utilisateur_btn.clicked.connect(fonction_utilisateur)