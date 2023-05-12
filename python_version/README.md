

<p align="center">
  <a href="https://oplusm.fr/">
    <img src="https://www.oplusm.fr/wp-content/uploads/2019/04/logo_OM_CMJN2.png" alt="Logo" width=240 height=180>
  </a>

  <h3 align="center">OplusM Sign Generator</h3>

  <p align="center">
    Ce code est un générateur de signature électronique pour des e-mails. Il peut être utilisé de manière manuelle ou en important un fichier xlsx "import.xlsx
  </p>
</p>


## Table des matières

- [Description](#description)
- [Fonctionnement](#fonctionnement)
- [Exemple d'architecture de dossier](#exemple-darchitecture-de-dossier)
- [Mode Manual](#mode-manual)
- [Contribution et Amélioration](#contribution-et-amélioration)
- [Créateur](#créateur)



## Description
Ce code est un générateur de signatures pour un service appelé "OplusM". Il importe les bibliothèques "os", "pandas", "numpy", "csv" et "PIL" qui seront utilisées tout au long du code.

Le code définit une liste nommée "lieux" qui contient les noms d'agences prédéfinies et une autre liste appelée "adresses" qui contient les adresses correspondantes. Il y a également une fonction "add_zero" pour corriger un problème de 0 invisible dans Excel.

Ensuite, il y a une fonction "manual_input" qui permet à l'utilisateur de saisir son nom, prénom, poste, numéro de téléphone et agence. La fonction "import_csv" importe des données depuis un fichier Excel nommé "import.xlsx".

La fonction "signature_generator" utilise soit les données saisies manuellement à l'aide de la fonction "manual_input", soit les données importées à l'aide de la fonction "import_csv" pour générer une signature.

Enfin, il y a une boucle qui permet à l'utilisateur de choisir entre la saisie manuelle des données ou l'importation de données à partir d'un fichier Excel, puis de générer la signature. La boucle s'exécute jusqu'à ce que l'utilisateur choisisse de sortir.


## Fonctionnement

Il vous faut [python](https://www.python.org/downloads/) 3.11 ou plus et Excel pour le mode "import".
Le fichier Import doit respecter certaines règles sinon le programme ne marchera pas correctement:

 - La première ligne n'ai pas lu et sert d'en-tête
 - l'ordre des colonnes doit être le même constamment (Nom Prénom Poste Téléphone et Agence)
 - Le Trigramme de l'agence doit être existant ( IDF,SWT,MED,....)
 - L'import doit être "propre" : numéro de téléphone long, mauvais nommage du poste,...
 - le fichier d'import doit en tous temps s'appeler "import.xlsx" et être à même hauteur que signature.exe
 
 Les signatures sorte sous ce format : signature_Prénom_NOM_ANNEE-JOUR-MOIS.png
 Pour utiliser le mode import il faut juste taper "import" dans le sélecteur.

## Exemple d'architecture de dossier

Signature.exe

```text
Dist/
└── Media/
    │   ├── sample2.png(fichier sample pour la génération de la signature)
    │   └── Result/ (dossier qui accueillera toutes les signatures généré)
    └── folder4/
├── signature.exe (programme à lancer)
└── import.xlsx ( fichier d'import)
```

## Mode Manual

Le mode "manual" soit manuel, est le plus simple et complet , vous devrez rentrez vous même les informations de l'utilisateur puis le programme vous proposera de recommencer, en cas de création de quelques utilisateur c'est une alternative plus puissante que le mode "import" à la différence le mode import peut générer près de 10 signatures à la seconde.

## Contribution et Amélioration
Le code source reste disponible , il est commenté afin d'aider les prochains utilisateur à l'améliorer.
## Créateur

**Adi Lasri**

- <https://github.com/AdemStars>


