from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def map():
    # Charger les données depuis le fichier CSV
    df = pd.read_csv(os.getcwd() + "/output/ORANGE_2024-04-22_16_38_06.csv", sep=",")

    # Convertir les coordonnées en chaînes de caractères
    df['coordonnees_str'] = df['coordonnees'].apply(lambda x: ','.join(str(i) for i in x))

    # Grouper les valeurs de 'emr_lb_systeme' pour chaque valeur de 'coordonnees'
    grouped_emr_lb_systeme = df.groupby('coordonnees_str')['emr_lb_systeme'].apply(list).reset_index()

    # Joindre les données groupées avec le DataFrame principal
    df = pd.merge(df, grouped_emr_lb_systeme, on='coordonnees_str')

    # Créer une liste de dictionnaires contenant les données nécessaires
    data = df[['adm_lb_nom', 'generation', 'coordonnees', 'emr_lb_systeme']].to_dict(orient='records')

    return render_template('map.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
