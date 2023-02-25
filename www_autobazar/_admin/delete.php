<?php

include_once "_partials/header_sm.php";

$car = get_car_detail(segment(2), false);
$car_array = array($car);

if (!$car) {
    show_404();
}
global $databaseAD;
$auth = new \Delight\Auth\Auth($databaseAD);

?>
<?  if($auth->isLoggedIn()) { ?>
uzivatel je prihlasen <br>
<div class="container-no-aligncenter" style="max-width: 60%">
    <a href=" <?= get_car_link($car) ?> "> vypis auta </a> &nbsp;
    <a href=" <?= BASE_URL ?>/edit-list "> Delete list aut </a>
    <section class="box">
        <form action="<?= BASE_URL ?>/_admin/delete-car.php" method="post" id="form">
            <header class="edit-header">
                <h1 class="box-head">
                    SMAZAT AUTO: <?= plain($car->znacka) ?> <?= plain($car->typ); ?>
                </h1>
                VIN: <?= $car->vin ?><br>
                CENA: <?= $car->cena ?> <br>
                <input type="hidden" name="id" value="<?= $car->id ?>">
                <input type="submit" class="btn edit-button-alert" value="SMAZAT"> or
                <a href=" <?= get_car_link($car) ?> "> cancel </a>
            </div>
        </form>
</div>

<hr>
<?  } ?>
<?php
include_once '_partials/footer_sm.php' ?>



