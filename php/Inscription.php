<?php
session_start();
error_reporting(E_ALL); ini_set("display_errors", 1);
// Configuration SQLite (fichier local)
define('DB_FILE', __DIR__ . '/../bibliotheque.db');
$link = mysqli_connect("localhost", "root");
if (!$link) {
    die("Connection failed: " . mysqli_error($link));
}
mysqli_select_db($link, "bibliothèque_agile");
$erreurs = [];
$succes = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST')
{
    $nom = trim((string)($_POST['nom'] ?? ''));
    $prenom = trim((string)($_POST['prenom'] ?? ''));
    $contact = trim((string)($_POST['contact'] ?? ''));

    // Validation
    if ($nom     === '') $erreurs[] = 'Le nom est requis.';
    if ($prenom  === '') $erreurs[] = 'Le prénom est requis.';
    if ($contact === '') $erreurs[] = 'L\'adresse e-mail est requise.';
    elseif (!filter_var($contact, FILTER_VALIDATE_EMAIL))
        $erreurs[] = 'L\'adresse e-mail n\'est pas valide.';

    if (empty($erreurs))
    {

        $query = "INSERT INTO usagers (nom, prenom, contact) VALUES ('".$nom."', '".$prenom."', '".$contact."')";
        if(mysqli_query($link, $query)) {
            $succes = 'Inscription réussie.';
        } else {
            if (strpos(mysqli_error($link), 'UNIQUE') !== false) {
                $erreurs[] = 'Cette adresse e-mail est déjà utilisée.';
            } else {
                $erreurs[] = 'Erreur serveur, réessayez plus tard.';
            }
        }
    }
}
mysqli_close($link);
?>
<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>Inscription</title>
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <style>
        body{font-family:Arial,Helvetica,sans-serif;max-width:600px;margin:2rem auto;padding:0 1rem}
        form{display:grid;gap:.5rem}
        label{font-weight:600}
        input[type="text"],input[type="email"]{padding:.5rem;border:1px solid #ccc;border-radius:4px}
        .errors{color:#a00}
        .success{color:#080}
    </style>
</head>
<body>
    <h1>Inscription</h1>

    <?php if ($erreurs): ?>
        <div class="errors">
            <ul>
                <?php foreach ($erreurs as $e): ?>
                    <li><?= htmlspecialchars($e, ENT_QUOTES | ENT_SUBSTITUTE) ?></li>
                <?php endforeach; ?>
            </ul>
        </div>
    <?php endif; ?>

    <?php if ($succes): ?>
        <p class="success"><?= htmlspecialchars($succes, ENT_QUOTES | ENT_SUBSTITUTE) ?></p>
    <?php endif; ?>

    <form method="post" novalidate>
        <div>
            <label for="nom">Nom</label><br>
            <input id="nom" name="nom" type="text" maxlength="100" required
             value="<?= isset($nom) ? htmlspecialchars($nom, ENT_QUOTES | ENT_SUBSTITUTE) : '' ?>">
        </div>
        <div>
            <label for="prenom">Prénom</label><br>
            <input id="prenom" name="prenom" type="text" maxlength="100" required
             value="<?= isset($prenom) ? htmlspecialchars($prenom, ENT_QUOTES | ENT_SUBSTITUTE) : '' ?>">
        </div>
        <div>
            <label for="contact">Adresse email</label><br>
            <input id="contact" name="contact" type="email" maxlength="255" required
             value="<?= isset($contact) ? htmlspecialchars($contact, ENT_QUOTES | ENT_SUBSTITUTE) : '' ?>">
        </div>
        <div>
            <button type="submit">S'inscrire</button>
        </div>
    </form>
</body>
</html>
