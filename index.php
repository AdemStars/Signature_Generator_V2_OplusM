<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div id="feedback-form">
  <h2 class="header">OplusM Signature Generator</h2>
  <div>   
<form method="post" enctype="multipart/form-data">
<label for="mode">Mode</label> 
<select id="mode" name="mode">
    <option value="choix">Choix du mode</option>
    <option value="manuel">Manuel</option>
    <option value="CSV">CSV</option>
</select>
<label for="prenom" id="prenom-label">Prénom</label>
<input type="text" name="prenom" id="prenom-input" required/>
<label for="nom" id="nom-label">Nom</label>
<input type="text" name="nom" id="nom-input" required/>
<label for="email" id="email-label">E-mail</label>
<input type="email" name="email" id="email-input" required/>
<label for="tel" id="tel-label">Téléphone</label>
<input type="tel" name="tel" id="tel-input" required/>
<label for="poste" id="poste-label">Poste</label>
<input type="text" name="poste" id="poste-input" required/>
        <br>
	<label for='fichier'>Ajouter le CSV </label>
        <input type="file" name="fichier[]" id="fichier" multiple>
    <div>
        <button type="hidden" class="btn" id="exemple"><i class="fa fa-download"></i> Exemple CSV</button>    
	    <button type="submit" class="btn" id="generer-btn">Générer</button>
</div>
</form>
</div>
</div>
 <!-- Inclusion du fichier JavaScript contenant la fonction dessinerTexteSurImage -->
 <script src="sign.js"></script>
  <script>
    // Écouter l'événement de soumission du formulaire et appeler la fonction dessinerTexteSurImage
    document.getElementById("generer-btn").addEventListener("click", function() {
    

      // Récupérer les valeurs des champs de formulaire
      var prenom = document.getElementById("prenom-input").value;
      var nom = document.getElementById("nom-input").value;
      var email = document.getElementById("email-input").value;
      var tel = document.getElementById("tel-input").value;
      var poste = document.getElementById("poste-input").value;

      // Créer un objet avec les informations
      var information = {
        prenom: prenom,
        nom: nom,
        email: email,
        tel: tel,
        poste: poste
      };

      // Appeler la fonction pour générer l'image avec les informations
      dessinerTexteSurImage(information, function(imageURL) {
        // Ouvrir une fenêtre de dialogue pour enregistrer l'image
        window.open(imageURL, "_blank");
      });
    });
  </script>
</body>
<script>
    const modeSelect = document.getElementById("mode");
    const prenomLabel = document.getElementById("prenom-label");
    const prenomInput = document.getElementById("prenom-input");
    const nomLabel = document.getElementById("nom-label");
    const nomInput = document.getElementById("nom-input");
    const emailLabel = document.getElementById("email-label");
    const emailInput = document.getElementById("email-input");
    const telLabel = document.getElementById("tel-label");
    const telInput = document.getElementById("tel-input");
    const posteLabel = document.getElementById("poste-label");
    const posteInput = document.getElementById("poste-input");
    const exempledll = document.getElementById("exemple");

    modeSelect.addEventListener("change", (event) => {
        const mode = event.target.value;
        if (mode === "CSV") {
            prenomLabel.style.display = "none";
            prenomInput.style.display = "none";
            nomLabel.style.display = "none";
            nomInput.style.display = "none";
            emailLabel.style.display = "none";
            emailInput.style.display = "none";
            telLabel.style.display = "none";
            telInput.style.display = "none";
            posteLabel.style.display = "none";
            posteInput.style.display = "none";
            exempledll.style.display = "block";
        } else {
            prenomLabel.style.display = "block";
            prenomInput.style.display = "block";
            nomLabel.style.display = "block";
            nomInput.style.display = "block";
            emailLabel.style.display = "block";
            emailInput.style.display = "block";
            telLabel.style.display = "block";
            telInput.style.display = "block";
            posteLabel.style.display = "block";
            posteInput.style.display = "block";
            exempledll.style.display = "none";

        }
    });
</script>