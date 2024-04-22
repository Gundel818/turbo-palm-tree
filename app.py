from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def map():
    # Charger les données depuis le fichier CSV
    df = pd.read_csv(os.getcwd() + "/output/2024-04-22_16_30_03.csv", sep=",")
    
    df[['latitude', 'longitude']] = df['coordonnees'].str.split(',', expand=True)
    df['latitude'] = df['latitude'].astype(float)
    df['longitude'] = df['longitude'].astype(float)

    # Convertir les coordonnées en chaînes de caractères
    # Grouper les valeurs de 'emr_lb_systeme' pour chaque valeur de 'coordonnees'
    grouped_emr_lb_systeme = df.groupby('sup_id')['emr_lb_systeme'].apply(list).reset_index()

    # Joindre les données groupées avec le DataFrame principal
    df = pd.merge(df, grouped_emr_lb_systeme, on='sup_id')

    df = df.drop_duplicates(subset=['sup_id']);
    #print(df.head)
    df.to_csv("output/test.csv")

    # Créer une liste de dictionnaires contenant les données nécessaires
    data = df[['adm_lb_nom', 'generation', 'latitude', 'longitude', 'emr_lb_systeme_y', 'adr_lb_add1']].to_dict(orient='records')

    return render_template('map.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
