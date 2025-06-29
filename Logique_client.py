from PySide6.QtWidgets import * 
from formulaire_client_ui import Ui_MainWindow
from tkinter import messagebox
import sqlite3

class Logique_client(QMainWindow):
    def __init__(self):
        def enregistrer_client():
            id_client = self.ui_ecran.id_client_input.text()
            nom_client = self.ui_ecran.nom_client_input.text()
            adresse_client = self.ui_ecran.adresse_client_input.text()
            telephone_client = self.ui_ecran.telephone_client_input.text()
            email_client = self.ui_ecran.email_client_input.text()

            try:
                conn = sqlite3.connect('Gestion.db')
                cursor = conn.cursor()

                if id_client != '' and nom_client != '' and adresse_client != '' and telephone_client != '' and email_client != '':
                    cursor.execute("""INSERT INTO 
                                        client(id_client, nom_client, adress, telephone, email)
                                        VALUES
                                        (?,?,?,?,?)
                                    """, (id_client, nom_client, adresse_client, telephone_client, email_client))
                    conn.commit()
                    messagebox.showinfo(title='SUCCESS', message=f'Le client {nom_client} a été ajouté avec succès!!')
                else:
                    messagebox.showerror(title='ERREUR', message='Le ou les champs semblent être vides, veuillez vérifier SVP')
                
                conn.close()

                # Clear the input fields after successful insertion
                self.ui_ecran.id_client_input.setText('')
                self.ui_ecran.nom_client_input.setText('')
                self.ui_ecran.adresse_client_input.setText('')
                self.ui_ecran.telephone_client_input.setText('')
                self.ui_ecran.email_client_input.setText('')
            
            except sqlite3.Error as e:
                messagebox.showerror(title='FAILURE', message=f'Échec d\'enregistrement: {e}')

        super().__init__()
        self.ui_ecran = Ui_MainWindow()
        self.ui_ecran.setupUi(self)
        
        self.ui_ecran.save_client_btn.clicked.connect(enregistrer_client)
        
        