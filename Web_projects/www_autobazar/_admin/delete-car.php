<?php require '../_inc/config.php';


global $databaseAD;
$id = filter_input(INPUT_POST, 'id', FILTER_SANITIZE_NUMBER_INT);

//FLASH

if ( ! $id ) {
    flash()->error(' nekde se stala kurevska chyba ');
}


if (flash()->hasMessages( )) {

header("Location: http://localhost/www_autobazar/edit-list"); /* Redirect browser */

/* Make sure that code below does not get executed when we redirect. */
exit;
} else ( flash()->success('huraaa smazali jsme nejake autooo ;D'));


$delete_car = $databaseAD->prepare("
DELETE FROM  cars 
WHERE id = :id
"  );

$delete_car->execute([
    'id' => $id
]);

if(!$delete_car) {
    flash()->error('kua neco se stalo....');
}
header("Location: http://localhost/www_autobazar/edit-list");
exit;


