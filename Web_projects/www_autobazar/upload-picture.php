
<?php
var_dump($_FILES['pictures']);

if (!empty($_FILES['pictures'])) {

    $carId = "1334";

    $uploadDir = __DIR__ . '/../pictures/' . $carId;
    if (!file_exists($uploadDir)) {
        mkdir($uploadDir, 0700);
    }

    foreach ($_FILES["pictures"]["error"] as $key => $error) {
        if ($error != UPLOAD_ERR_OK) {
            echo 'chyba';
            continue;
        }

        $uploadFile = $uploadDir . '/' . $key . '-picture.jpg';

        if (move_uploaded_file($_FILES['pictures']['tmp_name'][$key], $uploadFile)) {
            echo 'hura';
        } else {
            echo 'Nevim proc se nepodarilo presunout nahrany obrazek';
        }
    }

}
