<?php //NEPOUZIVAM, PROTOZE NEVIM, JAK PRESNE POUZIT COMPACT FUKCI - COMPACT NEFUNGUJE....

function validate_inputs()
{
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
        $dph = false;
    }
    if (isset($_POST['serviska'])) {
        $serviska = $_POST['serviska'];
    } else {
        $serviska = false;
    }

    $insertdate = $_POST['insertdate'];

    if (isset($_POST['id'])) {
        $id = filter_input(INPUT_POST, 'id', FILTER_SANITIZE_NUMBER_INT);
    } else {
        $id = false;
    }


//FLASH

    if (!$znacka = trim($znacka)) {
        flash()->error(' hele vypln tu znacku jooo');
    }

    if (!$cena && ((is_int($cena) === false))) {
        flash()->error(' hele vypln tu cenu jooo');
    }

    if (flash()->hasMessages()) {
        return false;
    } else {
        (flash()->success('podarilo se ti to tam vlozit ;D'));
    }
    return compact(
        'vin', 'znacka', 'typ', 'cena', 'kilometry', 'motor', 'rok', 'barva', 'karoserie', 'palivo', 'vybava' ,'historie', 'dph', 'serviska', 'insertdate',
        $vin, $znacka, $typ, $cena, $kilometry, $motor, $rok, $barva, $karoserie, $palivo, $vybava, $historie, $dph, $serviska, $insertdate
    );
}

