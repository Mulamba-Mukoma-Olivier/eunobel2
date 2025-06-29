from PySide6.QtWidgets import QMainWindow 
from formulaire_commande_cli_ui import Ui_MainWindow 
from tkinter import messagebox 
import sqlite3

class Logique_commande_client(QMainWindow):
    def __init__(self):
        def fonction_commande_client():
            id_client = self.ui_ecran.id_client_cf_input.text()
            date_client = self.ui_ecran.date_commande_client_input.text()
            statut = self.ui_ecran.statut_commande_client_input.text()
            
            try:
                conn = sqlite3.connect('Gestion.db')
                cursor = conn.cursor()

                if id_client != '' and date_client != '' and statut != '':
                    cursor.execute("""INSERT INTO 
                                        commande_client(id_client, date_commande, statut)
                                        VALUES
                                        (?,?,?)
                                    """, (id_client, date_client, statut))
                    conn.commit()
                    messagebox.showinfo(title='SUCCESS', message=f'a été ajouté avec succès!!')
                else:
                    messagebox.showerror(title='ERREUR', message='Le ou les champs semblent être vides, veuillez vérifier SVP')
                
                conn.close()

                # Clear the input fields after successful insertion
                self.ui_ecran.id_client_cf_input.setText('')
                # self.ui_ecran.date_commande_client_input.setText('')
                self.ui_ecran.statut_commande_client_input.setText('')
                
            except sqlite3.Error as e:
                messagebox.showerror(title='FAILURE', message=f'Échec d\'enregistrement: {e}')
        super().__init__()
        self.ui_ecran = Ui_MainWindow()
        self.ui_ecran.setupUi(self)
        
        self.ui_ecran.save_cf_client_btn.clicked.connect(fonction_commande_client)