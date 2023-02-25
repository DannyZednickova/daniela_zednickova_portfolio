<?php
require '../_inc/config.php';


global $databaseAD;

$id = filter_input(INPUT_POST, 'id', FILTER_SANITIZE_NUMBER_INT);
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
if (isset($_POST['tip_auto'])) {
    $tip_auto = $_POST['tip_auto'];
} else {
    $tip_auto = '0';
}


$insertdate = $_POST['insertdate'];

//FLASH

if (!$znacka = trim($znacka)) {
    flash()->error(' hele vypln tu znacku jooo');
}

if ((!$kilometry) || (!$vin) || (!$cena)) {
    flash()->error(' hele vypln ty kilometry, roky a cenu poradne, jooo');
}


if (flash()->hasMessages()) {
    header("Location: http://localhost/www_autobazar/edit/$id"); /* Redirect browser */

    /* Make sure that code below does not get executed when we redirect. */
    exit;
} else {
    (flash()->success('podarilo se ti to zmenit ;D'));
}


$update_car = $databaseAD->prepare("
UPDATE cars SET 
tip_auto = :tip_auto,
vin = :vin,
znacka = :znacka,
typ = :typ,
cena = :cena,
kilometry = :kilometry,
motor = :motor,
rok = :rok,
barva = :barva,
karoserie = :karoserie,
palivo = :palivo,
vybava = :vybava,
historie = :historie,
dph = :dph,
serviska = :serviska,
insertdate = :insertdate
    
WHERE id = :id
");

$update_car->execute([
    'id' => $id,
    'tip_auto' => $tip_auto,
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


header("Location: http://localhost/www_autobazar/edit/$id");
exit;
?>


