<?php

include_once "_partials/header_sm.php";

$car = get_car_detail(segment(2), false);
$car_array = array($car);
dannyprint($car_array);


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
    <a href=" <?= BASE_URL ?>/edit-list "> editacni list aut </a>
    <section class="box">
        <form action="<?= BASE_URL ?>/_admin/edit-car.php" method="post" id="form">
            <header class="edit-header">
                <h1 class="box-head">
                    EDIT <?= plain($car->znacka) ?> <?= plain($car->typ);
                    dannyprint(date('Y-d-m H:i:s')); ?>

                </h1>
            </header>
            <input type="hidden" name="id" value="<?= $car->id ?>">
            <input type="hidden" name="insertdate" value="<?= date('Y-d-m H:i:s') ?>">
            <div class="row">
                <div class="col-25">
                    <label for="vin"> VIN </label>
                </div>
                <div class="col-75">
                    <input maxlength='20' type="text" name="vin" class="form-control" value="<?= $car->vin ?>">
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="znacka"> ZNACKA </label>
                </div>
                <div class="col-75">
                    <input maxlength='20' type="text" name="znacka" class="form-control" value="<?= $car->znacka ?>">
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="motor"> TYP AUTA </label>
                </div>
                <div class="col-75">
                    <input maxlength='20' type="text" name="typ" class="form-control" value="<?= $car->typ ?>">
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="cena"> CENA </label>
                </div>
                <div class="col-75">
                    <input maxlength='20' type="text" name="cena" class="form-control" value="<?= $car->cena ?>">
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="kilometry"> KILOMETRY </label>
                </div>
                <div class="col-75">
                    <input maxlength='20' type="text" name="kilometry" class="form-control" value="<?= $car->kilometry ?>">
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="motor"> MOTOR </label>
                </div>
                <div class="col-75">
                    <input maxlength='20' type="text" name="motor" class="form-control" value="<?= $car->motor ?>">
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="rok"> ROK </label>
                </div>
                <div class="col-75">
                    <input maxlength='20' type="text" name="rok" class="form-control" value="<?= $car->rok ?>">
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="barva"> BARVA </label>
                </div>
                <div class="col-75">
                    <input maxlength='20' type="text" name="barva" class="form-control" value="<?= $car->barva ?>">
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="karoserie">KAROSERIE</label>
                </div>
                <div class="col-75">
                    <select name="karoserie" class="edit-selectors">
                        <option value=" "> Vyber</option>
                        <?php
                        echo make_options($array = ['sedan', 'hatchback', 'pick up', 'dodávka'],
                            $car->karoserie ?? null) ?>
                    </select>
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="palivo"> PALIVO </label>
                </div>
                <div class="col-75">
                    <select name="palivo" class="edit-selectors">
                        <option value=" "> Vyber</option>
                        <?php
                        echo make_options($array = ['benzin', 'nafta', 'plyn', 'hybrid', 'jiné'],
                            $car->palivo ?? null) ?>
                    </select>
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="vybava"> VYBAVA </label>
                </div>
                <div class="col-75">
                    <textarea name="vybava" style="height:200px" class="edit-textarea"><?= $car->vybava ?></textarea>
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="historie"> HISTORIE MAJITELE </label>
                </div>
                <div class="col-75">
                    <textarea name="historie" style="height:200px" class="edit-textarea"><?= $car->historie ?></textarea>
                </div>
            </div>
            <div class="row bottom-buttons">

                <label for="dph"> MÁ / NEMÁ DPH</label>
                <input type="checkbox" name="dph" value="1" <?= ($car->dph) === 1 ? 'checked' : '' ?> ><br>
                <label for="serviska"> MÁ / NEMÁ SERVISNÍ KNIHU </label>
                <input type="checkbox" name="serviska" value="1" <?= ($car->serviska) === 1 ? 'checked' : '' ?> > <br>
                <label for="tip_auto"> ZARADIT MEZI TIPY </label>
                <input type="checkbox" name="tip_auto" value="1" <?= ($car->tip_auto) === 1 ? 'checked' : '' ?> ><br>

                <input type="submit" class="btn edit-button-alert" value="EDITOVAT"> or
                <a href=" <?= get_car_link($car) ?> "> cancel </a>
            </div>
        </form>
</div>

<hr>
<?  } ?>
<?php
include_once '_partials/footer_sm.php' ?>



