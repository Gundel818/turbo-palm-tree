from datetime import datetime
import pandas as pa

class BandSorter:
    def __init__(self, cellfile : str):
        dtype_options = {'coord': str}
        self.__df = pa.read_csv(cellfile, header=0, sep=';', index_col=False, dtype=dtype_options)
        self.__df.set_index('id', inplace=True)
        self.__ope = ""

    def setOPE(self, ope : str):
        ope = ope.upper()
        self.__ope = ope

    def getOPE(self):
        return self.__ope
 
    def chooseOPE(self):
        ope = input("Quel opérateur ? (Orange, Bouygues Telecom, SFR, Free Mobile, ou Aucun) : ")
        opeList = ["ORANGE", "BOUYGUES TELECOM", "SFR", "FREE"]

        if not ope in opeList:
            print("Opérateur non reconnu ou 'Aucun' entré. Tout les opérateurs seront affichés")
            return False
        self.setOPE(ope)
        return True

    def filter_group(self, group):
        # Vérifier si le groupe a une seule valeur unique dans la colonne 'generation'
        if group['generation'].nunique() == 1:
            # True uniquement si la seule valeur est '4G'
            return group['generation'].iloc[0] == '4G'
        else:
            return False
    
    def only4G(self): # Avoir des sites où il n'y a QUE la 4G 
        df = self.__df
        filtered_df = df.groupby('sup_id').filter(self.filter_group)

        print(filtered_df.head())
        self.save(filtered_df)

    def save(self, df):
        ajd = datetime.now()
        date_actu = ajd.strftime("%Y-%m-%d_%H_%M_%S")
        save = date_actu + '.csv'
        if self.chooseOPE():
            df = df.loc[df['adm_lb_nom'] == self.getOPE()]
            save = self.getOPE() + '_' + save

        df.to_csv('output/' + save, index=True)
        print("Fichier", save, "sauvegardé")