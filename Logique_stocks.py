from PySide6.QtWidgets import QMainWindow
from formulaire_stocks_ui import Ui_MainWindow 
from tkinter import messagebox 
import sqlite3

class Logique_stocks(QMainWindow):
    def __init__(self):
        def stock_fonction():
            
            id_produit = self.ui_ecran.id_produit_stock_input.text()
            id_entrepot = self.ui_ecran.id_entrepot_stock_input.text()
            quantite = self.ui_ecran.quantite_stock_input.text()
            
            try:
                conn = sqlite3.connect('Gestion.db')
                cursor = conn.cursor()

                if id_produit != '' and id_entrepot != '' and quantite != '':
                    cursor.execute("""INSERT INTO 
                                        stocks(id_produit,id_entrepot, quantite)
                                        VALUES
                                        (?,?,?)
                                    """, (id_produit, id_entrepot, quantite))
                    conn.commit()
                    messagebox.showinfo(title='SUCCESS', message=f'Le stock a été ajouté avec succès!!')
                else:
                    messagebox.showerror(title='ERREUR', message='Le ou les champs semblent être vides, veuillez vérifier SVP')
                
                conn.close()

                # Clear the input fields after successful insertion
                self.ui_ecran.id_produit_stock_input.setText('')
                self.ui_ecran.id_entrepot_stock_input.setText('')
                self.ui_ecran.quantite_stock_input.setText('')
            except sqlite3.Error as e:
                messagebox.showerror(title='FAILURE', message=f'Échec d\'enregistrement: {e}')
        super().__init__()
        self.ui_ecran = Ui_MainWindow()
        self.ui_ecran.setupUi(self)
        
        self.ui_ecran.save_stock_btn.clicked.connect(stock_fonction)