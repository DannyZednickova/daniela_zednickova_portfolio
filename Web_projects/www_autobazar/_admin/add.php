<?php

include_once "_partials/header_sm.php";

if (isset($_SESSION['form_add_data'])){
    extract($_SESSION['form_add_data']);
    unset($_SESSION['form_add_data']);
}
global $databaseAD;
$auth = new \Delight\Auth\Auth($databaseAD);

?>
<?php
if($auth->isLoggedIn()) { ?>
uzivatel je prihlasen <br>
<div class="container-no-aligncenter" style="max-width: 60%">

    <a href=" <?= BASE_URL ?>/edit-list "> Editacni list aut </a>
    <section class="box">
        <form action="<?= BASE_URL ?>/_admin/add-car.php" method="post" id="form" >
            <header class="edit-header">
                <h1 class="box-head">
                    VLOZIT AUTO
                    <?= (date('Y-d-m H:i:s')); ?>

                </h1>
            </header>
            <input type="hidden" name="id" value=" ">
            <input type="hidden" name="insertdate" value="<?= date('Y-d-m H:i:s') ?>">
            <div class="row">
                <div class="col-25">
                    <label for="vin"> VIN </label>
                </div>
                <div class="col-75">
                    <input maxlength='20' type="text" name="vin" class="form-control" value="<?= $vin ?: ''?>">
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="znacka"> ZNACKA </label>
                </div>
                <div class="col-75">
                    <input maxlength='20' type="text" name="znacka" class="form-control" value="<?= $znacka ?: ''?> ">
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="motor"> TYP AUTA </label>
                </div>
                <div class="col-75">
                    <input maxlength='20' type="text" name="typ" class="form-control" value="<?= $typ ?: '' ?>">
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="cena"> CENA </label>
                </div>
                <div class="col-75">
                    <input maxlength='20' type="text" name="cena" class="form-control" value=" <?= $cena ?: '' ?>">
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="kilometry"> KILOMETRY </label>
                </div>
                <div class="col-75">
                    <input maxlength='20' type="text" name="kilometry" class="form-control" value=" <?= $kilometry ?: '' ?>">
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="motor"> MOTOR </label>
                </div>
                <div class="col-75">
                    <input maxlength='20' type="text" name="motor" class="form-control" value=" <?= $motor ?: '' ?>">
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="rok"> ROK </label>
                </div>
                <div class="col-75">
                    <input maxlength='20' type="text" name="rok" class="form-control" value=" <?= $rok ?: '' ?>">
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="barva"> BARVA </label>
                </div>
                <div class="col-75">
                    <input maxlength='20' type="text" name="barva" class="form-control" value=" <?= $barva ?: '' ?>">
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
                            'vyber' ?? null) ?>
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
                            'vyber' ?? null) ?>
                    </select>
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="vybava"> VYBAVA </label>
                </div>
                <div class="col-75">
                    <textarea name="vybava" style="height:200px" class="edit-textarea" > <?= $vybava ?: '' ?> </textarea>
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="historie"> HISTORIE MAJITELE </label>
                </div>
                <div class="col-75">
                    <textarea name="historie" style="height:200px" class="edit-textarea"> <?= $historie ?: '' ?> </textarea>
                </div>
            </div>
               <div class="row bottom-buttons">

                <label for="dph"> MÁ / NEMÁ DPH</label>
                <input type="checkbox" name="dph" value="1" <?= ($dph) === '1' ? 'checked' : '' ?> ><br>
                <label for="serviska"> MÁ / NEMÁ SERVISNÍ KNIHU </label>
                <input type="checkbox" name="serviska" value="1" <?= ($serviska) === '1' ? 'checked' : '' ?> > <br>
                <label for="tip_auto"> ZARADIT MEZI TIPY </label>
                <input type="checkbox" name="tip_auto" value="1" <?= ($tip_auto) === '1' ? 'checked' : '' ?> ><br>

                <input type="submit" class="btn edit-button-alert" value="VLOZIT AUTO DO DATABÁZE">

            </div>
        </form>

        <form action="" enctype="multipart/form-data"> <!-- absoltune nevim, jak spojit dva form dohromady!-->
            <p>
                Send this file: <input name="pictures" type="file" /><br>
            </p>
        </form>



</div>
<?php
} ?>
<?php
include_once '_partials/footer.php' ?>



