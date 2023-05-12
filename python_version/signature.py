##OplusM Sign generator by Adi Lasri, January 2023
import os
import pandas as pd
import numpy as np
import csv
from PIL import Image,ImageFont,ImageDraw
from datetime import date
import time
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

#fonction qui corrige l'erreur du 0 invisible sur excel
def add_zero(n):
    if n[0] != "0":
        return "0" + str(n)
    return str(n)

def manual_input():



## RECUPERATION DES DONNEES
    ## MODE MANUEL
# Demandez à l'utilisateur de saisir son prénom et son nom puis son poste
    nom = input("Entrez le nom: ")
    nom = nom.upper()
    prenom = input("Entrez le prénom: ")
    prenom = prenom.capitalize()
    poste = input("Entrez le poste: ")
    poste = poste.capitalize() 
# Demandez le numéro de telephone
    while True:
        telephone = input("Entrez le téléphone: ")
        if telephone.isdigit() and len(telephone) == 10:
            #Le numéro de téléphone est valide, on peut sortir de la boucle
            break
        else:
            print("Numéro de téléphone non valide, veuillez réessayer.")
    tel_text = " ".join([telephone[i:i+2] for i in range(0, len(telephone), 2)])
# choisir l'agence
    # Demandez à l'utilisateur de choisir son lieu de domicile
    print("Veuillez choisir votre lieu de domicile parmi les options suivantes:")
    for i, lieu in enumerate(lieux):
        print(f"{i+1}. {lieu}")
    while True:
        choix = input("Entrez le numéro de votre choix: ")
        if choix.isdigit() and 1 <= int(choix) <= len(lieux):
            # Le choix est valide, on peut sortir de la boucle
            lieu_domicile = lieux[int(choix)-1]
            break
        else:
            print("Choix non valide, veuillez réessayer.")
    return (prenom, nom, poste, telephone, lieu_domicile)
## MODE IMPORT
def import_csv():
    xlsx = pd.read_excel('import.xlsx', skiprows=0)
    results=xlsx.values
    return results
## Création du tableau de données
def signature_generator(mode):
    if mode == 'manual':
        prenom, nom, poste, telephone, lieu_domicile = manual_input()
        manual_tab= [prenom, nom, poste, telephone, lieu_domicile]  
        results=[manual_tab]
    elif mode == 'import':
        results=import_csv()  
    else:
        results = "ERREUR : mauvaise entrer"
        print(results)
    return results    
#############################################################################

## BOUCLE DE GENERATION DES SIGNATURES
while True: 
    mode = input("Bienvenu dans l'OplusM Sign Generator. Tapez 'manual' pour généré une signature manuellement ou 'import' si vou avez un modèle de masse (import.xlsx) : ")
    results=signature_generator(mode)

    # Ouvrez l'image de base
    i=0
    start = time.time()
    for i in range (len(results)):
        base_image = Image.open('media\sample2.png')

        # Créez un nouveau fichier image pour la signature
        signature_image = base_image # Image.new("RGB", base_image.size, (255, 255, 255))

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
        signature_image.save('media/result/'+ nom_image, 'png')
        print(nom_image)
    
## gestion de la boucle
 ## Demandez à l'utilisateur s'il souhaite quitter ou recommencer
    end = time.time()
    elapsed = end - start

    print(f'Temps d\'exécution : {elapsed:.2}ms')
    choix = input("Souhaitez-vous quitter le programme (Q) ou recommencer (R) ? ")

    if choix.upper() == "Q":
            # L'utilisateur souhaite quitter, on peut sortir de la boucle
            break
    elif choix.upper() == "R":
            # L'utilisateur souhaite recommencer, on peut continuer la boucle
            continue
    else:
            # L'utilisateur a saisi une réponse non valide, on affiche un message d'erreur
            print("Réponse non valide, veuillez réessayer.")