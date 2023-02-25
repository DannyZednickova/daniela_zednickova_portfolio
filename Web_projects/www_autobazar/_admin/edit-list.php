<?php

include_once "_partials/header_sm.php";
$cars = get_edit_list();
global $databaseAD;
$auth = new \Delight\Auth\Auth($databaseAD);

?>
<?  if($auth->isLoggedIn()) { ?>
<div class="container">
    Uzivatel prihlasen <br>

    <a href="<?= BASE_URL?>/add" > VLOZIT NOVE AUTO   </a> &nbsp;  / &nbsp;
    <a href="<?= BASE_URL?>/cars" > VYPIS VSECH AUT UZIVATELUM </a>



    <h1> EDITACNI LIST AUT </h1>

    <div class="edit-list-box-header">
        <div class="edit-list-car">
            AUTA
        </div>
        <div class="edit-list-actions">
            smazat / editovat <span class="edit-list-update-date"> datum zmeny </span>
        </div>

    </div>

    <?php
    if (count($cars)) : foreach ($cars as $car) : ?>
        <div class="edit-list-box">
            <a href=" <?=get_car_link($car)?> "><div class="edit-list-car">
                <?= $car->znacka ?> <?= $car->typ ?>  <?= $car->rok ?> / CENA: <?= number_format(plain($car->cena), 0,
                    ',', ' ') . ',-' ?>
            </div> </a>
            <div class="edit-list-actions">
                <a href="<?= BASE_URL ?>/edit/<?= $car->id ?> "> <i class="fas fa-edit"></i> &nbsp; / &nbsp;
                    <a href="<?= BASE_URL ?>/delete/<?= $car->id ?> "><i class="fas fa-times"></i> </a>
                    <span class="edit-list-update-date"> <span class="insert-time"><?= $car->insertdate ?> </span>  </span>
            </div>
        </div>
    <?php
    endforeach;
    else: ?>
        <p>
            NEMAM NIC </p>
    <?php
    endif ?>
    <?  } ?>
    <?php
    include_once "_partials/footer.php" ?>

