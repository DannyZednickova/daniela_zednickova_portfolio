<?php
require '../_inc/config.php';


global $databaseAD;
$vin = filter_input(INPUT_POST, 'vin', FILTER_SANITIZE_STRING);
$znacka = filter_input(INPUT_POST, 'znacka', FILTER_SANITIZE_STRING);
$typ = filter_input(INPUT_POST, 'typ', FILTER_SANITIZE_STRING);
$cena = filter_input(INPUT_POST, 'cena', FILTER_SANITIZE_NUMBER_INT);
$kilometry = filter_input(INPUT_POST, 'kilometry', FILTER_SANITIZE_NUMBER_INT);
$motor = filter_input(INPUT_POST, 'motor', FILTER_SANITIZE_STRING);
$rok = filter_input(INPUT_POST, 'rok', FILTER_SANITIZE_NUMBER_INT);
$barva = filter_input(INPUT_POST, 'barva', FILTER_SANITIZE_STRING);
$karoserie = filter_input(INPUT_POST, 'karoserie', FILTER_SANITIZE_STRING);
$palivo = filter_input(INPUT_POST, 'palivo', FILTER_SANITIZE_STRING);
$vybava = filter_input(INPUT_POST, 'vybava', FILTER_SANITIZE_STRING);
$historie = filter_input(INPUT_POST, 'historie', FILTER_SANITIZE_STRING);
if (isset($_POST['dph'])) {
    $dph = $_POST['dph'];
} else {
    $dph = '0';
}

if (isset($_POST['serviska'])) {
    $serviska = $_POST['serviska'];
} else {
    $serviska = '0';
}


$insertdate = $_POST['insertdate'];


//FLASH

if (!$znacka = trim($znacka)) {
    flash()->error(' hele vypln tu znacku jooo');
}

if (!$cena && ((is_int($cena) === false))) {
    flash()->error(' hele vypln tu cenu jooo');
}

if (flash()->hasMessages()) {
    header("Location: http://localhost/www_autobazar/add"); /* Redirect browser */

    $_SESSION['form_add_data'] = [
        'vin' => $vin,
        'typ' => $typ,
        'znacka' => $znacka,
        'cena' => $cena,
        'kilometry' => $kilometry,
        'motor' => $motor,
        'rok' => $rok,
        'barva' => $barva,
        'karoserie' => $karoserie,
        'palivo' => $palivo,
        'vybava' => $vybava,
        'historie' => $historie,
        'dph' => $dph,
        'serviska' => $serviska,
        'insertdate' => $insertdate

    ];
    /* Make sure that code below does not get executed when we redirect. */
    exit;
} else {
    flash()->success('podarilo se ti to tam vlozit - noveeee autooo ;D');
    header("Location: http://localhost/www_autobazar/add");
}


$insert_car = $databaseAD->prepare("
INSERT INTO cars 
(vin, znacka, typ, cena, kilometry, motor, rok, barva, karoserie, palivo, vybava, historie, dph, serviska, insertdate)
VALUES
(:vin, :znacka, :typ, :cena, :kilometry, :motor, :rok, :barva, :karoserie, :palivo, :vybava, :historie, :dph, :serviska, :insertdate)
");

$insert_car->execute([
    'vin' => $vin,
    'typ' => $typ,
    'znacka' => $znacka,
    'cena' => $cena,
    'kilometry' => $kilometry,
    'motor' => $motor,
    'rok' => $rok,
    'barva' => $barva,
    'karoserie' => $karoserie,
    'palivo' => $palivo,
    'vybava' => $vybava,
    'historie' => $historie,
    'dph' => $dph,
    'serviska' => $serviska,
    'insertdate' => $insertdate


]);


/*
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

} */


//header("Location: http://localhost/www_autobazar/cars");
//exit;
?>

