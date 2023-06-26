##OplusM Sign generator by Adi Lasri, January 2023
import requests
from js import document, console, Uint8Array, window, File
import os
import os.path
import pyodide
from datetime import date
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

results = []  ## tableau que l'on utilisera pour créer les signatures
    # Liste des d'agence prédéfinis
lieux = ['IDF', 'CTA', 'MED', 'SWT', 'CVL','WST',]
# deuxième liste mais avec les adresses des agence
adresses = {
    'IDF': "15 rue Paul Langevin - 78 370 Plaisir ",
    'CTA': '662 RUe des Jonchères - Bât. M - 69 730 Genay',
    'MED': '96 Rue de la Silice - 13 210 Saint Rémy de Provence',
    'SWT': "6 Rue Boulle - 32 600 L'isle Jourdain",
    'WST': "7 bis Rue Philippe Lebon - 44 980 St Luce sur Loire",
    'CVL': '22 Rue Gustave Eiffel - 45 380 La Chapelle Saint Mesmin',
    'SWT-BDX': "5 Rue des métiers - Parc d'activités du Cournalet - 33 290 Blanquefort",
}
""" 
#fonction qui corrige l'erreur du 0 invisible sur excel
def add_zero(n):
    if n[0] != "0":
        return "0" + str(n)
    return str(n)

## RECUPERATION DES DONNEES
## Création du tableau de données
def signature_generator(mode):
    if mode == 'manual':
        prenom, nom, poste, telephone, lieu_domicile = manual_input()
        manual_tab= [prenom, nom, poste, telephone, lieu_domicile]  
        results=[manual_tab]
    else:
        results = "ERREUR : mauvaise entrer"
        print(results)
    return results    """  
#############################################################################

## BOUCLE DE GENERATION DES SIGNATURES
def test(e):     
      #Get the first file from upload
    file_list = e.target.files
    first_item = file_list.item(0)
    array_buf = Uint8Array.new(first_item.arrayBuffer())
    bytes_list = bytearray(array_buf)
    my_bytes = io.BytesIO(bytes_list) 
    my_image = Image.open(my_bytes)
    console.log(f"{my_image.format= } {my_image.width= } {my_image.height= }")
    my_stream = io.BytesIO()
    my_image.save(my_stream, format="PNG")
    image_file = File.new([Uint8Array.new(my_stream.getvalue())], "new_image_file.png", {type: "image/png"})
    new_image = document.createElement('img')
    new_image.src = window.URL.createObjectURL(image_file)
    document.getElementById("output_upload_pillow").appendChild(new_image)
def signature(): 
        prenom=Element('prenom-input').value
        nom=Element('nom-input').value
        agence=Element('REG').value
        email=Element('email-input').value
        tel=Element('tel-input').value
        poste=Element('poste-input').value
        manual_tab= [prenom, nom, poste,email, tel, agence]  
        results=[manual_tab]

        # Ouvrez l'image de base
        i=0
        for i in range (len(results)):
            base_image = Image.open("sample.png")

        # Créez un nouveau fichier image pour la signature
            signature_image = base_image
            # Image.new("RGB", base_image.size, (255, 255, 255))

            # Chargez la police et définissez la taille de police
            acumin = ImageFont.truetype("/font/Acumin-RPro.otf", 36)
            Gacumin = ImageFont.truetype("/font/Acumin-RPro.otf", 40)
            Macumin = ImageFont.truetype("/font/Acumin-RPro.otf", 32)
            #Définissions de chaque balise d'écriture
            nom_complet = results[i][0] + " " + results[i][1]
            poste=results[i][2]
            tel_text=add_zero(str(results[i][3]))
            adresse_bureau=adresses[results[i][4]]

            # Dessinez le texte de la signature sur l'image
            draw = ImageDraw.Draw(signature_image)
            draw.text((680, 100), nom_complet, font=Gacumin, fill=(61,102,139),stroke_width=1)
            draw.text((680, 150), poste, font=Macumin, fill=(163,207,134),stroke_width=1)
            draw.text((740, 217), tel_text, font=acumin, fill=(61,102,139))
            draw.text((740, 267), adresse_bureau, font=acumin, fill=(61,102,139))
            
            # Collez l'image de base sur l'image de la signature
            signature_image.paste(base_image, (0, 0))

            #récupération de la date et assignation au nom de l'image
            nom_image = f"signature_{results[i][0] }_{results[i][1]}_{date.today()}.png"

            # Enregistrez l'image de la signature
            signature_image.save('Signatures/'+ nom_image, 'png')
            print(nom_image)
            return(nom_image)
