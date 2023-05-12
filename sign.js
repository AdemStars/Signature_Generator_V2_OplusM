<link rel="stylesheet" href="sign.css"></link>
// Position en pixels des informations sur l'image
var positions = {
  nom: { x: 50, y: 80 },
  prenom: { x: 50, y: 120 },
  telephone: { x: 50, y: 160 },
  mail: { x: 50, y: 200 },
  poste: { x: 50, y: 240 }
};

// Style du texte
var styles = {
  nom: { police: 'AcuminBold', couleur: "white", contour: "black", contourLargeur: 2 },
  prenom: { police: 'AcuminBold', couleur: "yellow", contour: "black", contourLargeur: 2 },
  telephone: { police: 'AcuminBold', couleur: "red", contour: "black", contourLargeur: 1 },
  mail: { police: 'AcuminBold', couleur: "green", contour: "black", contourLargeur: 1 },
  poste: { police: 'AcuminBold', couleur: "blue", contour: "black", contourLargeur: 1 }
};

// Chargement de l'image
var image = new Image();
image.src = "sample2.png";

// Fonction de dessin sur l'image
function dessinerTexteSurImage(information) {
     // Obtenir la date actuelle
  var dateActuelle = new Date();
  var annee = dateActuelle.getFullYear();
  var mois = ("0" + (dateActuelle.getMonth() + 1)).slice(-2);
  var jour = ("0" + dateActuelle.getDate()).slice(-2);

  // Générer le nom de l'image
  var nomImage = `signature_${information.prenom}_${information.nom}_${annee}_${mois}_${jour}.png`
  // Création d'un canvas pour dessiner sur l'image
  var canvas = document.createElement("canvas");
  canvas.width = image.width;
  canvas.height = image.height;

  // Dessin de l'image sur le canvas
  var ctx = canvas.getContext("2d");
  ctx.drawImage(image, 0, 0);

  // Dessin du texte avec les styles spécifiés
  Object.keys(information).forEach(function(key) {
    var position = positions[key];
    var style = styles[key];
    var texte = information[key];
    dessinerTexte(ctx, texte, position.x, position.y, style);
  });

  // Récupération de l'image avec les informations dessinées
  var imageAvecTexte = new Image();
  imageAvecTexte.src = canvas.toDataURL();

  // Création du lien de téléchargement
  var lienTelechargement = document.createElement("a");
  lienTelechargement.href = imageAvecTexte.src;
  lienTelechargement.download = nomImage;
  document.body.appendChild(lienTelechargement);
}