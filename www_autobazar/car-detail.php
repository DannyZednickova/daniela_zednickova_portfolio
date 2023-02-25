<?php

include_once "_partials/header.php";
$car = (object)get_car_detail();
?>

<?
$path_car = ' <a href="' . BASE_URL . '"> home </a> / <a href="' . BASE_URL . '/cars "> vozidla </a> / ' . ($car->znacka) . " " . ($car->typ);
$carTitle = ($car->znacka) . " " . ($car->typ);
?>
<!--CAR BOX-->

<div class="container">
    <span class="path-title"> <?php
        echo $path_car ?> </span>
    <div class="car-title">
        <div class="car-title-left">
            <?php
            echo $carTitle ?>
        </div>
        <div class="car-title-right">
            <i class="fas fa-print"></i>
            <i class="fas fa-print"></i>
            <i class="fas fa-print"></i>
        </div>
    </div>
</div>

<div class="car-container">
    <div class="car-info-box">
        <div class="car-photo-info">
            <div class="car-photo">

                <img class="car-detail-photo" src="../../../assets/img/car.JPG" alt="Card image cap">

                <div class="car-thumb-nails-box">
                    <img class="car-thumb-nail " src="../../../assets/img/car.JPG" alt="">
                    <img class="car-thumb-nail " src="../../../assets/img/car.JPG" alt="">
                    <img class="car-thumb-nail " src="../../../assets/img/car.JPG" alt="">
                    <img class="car-thumb-nail " src="../../../assets/img/car.JPG" alt="">
                    <img class="car-thumb-nail " src="../../../assets/img/car.JPG" alt="">
                    <img class="car-thumb-nail " src="../../../assets/img/car.JPG" alt="">


                </div>
            </div>
            <div class="car-info">
                <div class="engine-info">
                    <span><i class="fab fa-accusoft"></i><?= $car->motor ?> </span>
                    <span><i class="fab fa-accusoft"></i><?= $car->kilometry ?> </span>
                    <span><i class="fab fa-accusoft"></i> <?= $car->palivo ?></span>
                    <span><i class="fab fa-accusoft"></i> automat  </span>
                </div>
                <div class="sales-info">
                    <span class="sales-detail">CENA: <?= $car->cena ?> </span>
                    <span class="sales-detail-odd"> VIN: <?= $car->vin ?> </span>
                    <span class="sales-detail"> <?php
                        if (($car->dph) === "1") {
                            echo "S DPH";
                        } else {
                            echo "BEZ DPH ";
                        } ?></span>
                    <span class="sales-detail-odd"> Z NEMECKA </span>
                </div>
            </div>
        </div>
    </div>
    <table class="table-car">
        <tbody>
        <tr>
            <th>V provozu od:</th>
            <td><?= $car->rok ?></td>
        </tr>
        <tr>
            <th>Km:</th>
            <td><?= $car->kilometry ?></td>
        </tr>
        <tr class="hide">
            <th>Objem:</th>
            <td><?= $car->motor ?></td>
        </tr>
        <tr>
            <th>Barva:</th>
            <td><?= $car->barva ?></td>
        </tr>
        <tr>
            <th>Karosérie:</th>
            <td><?= $car->karoserie ?></td>
        </tr>
        <tr>
            <th>Servisní knížka:</th>
            <td><?php
                if (($car->serviska) === "1") {
                    echo "ANO";
                } else {
                    echo "NE";
                } ?></td>
        </tr>
        <tr>
            <th>V případě zájmu volejte</th>
            <td> 777 144 288 - Petr Drábek</td>
        </tr>
        </tbody>
    </table>

        <div class="edit-links">
            <a href="<?= get_car_link($car, 'edit') ?> "> edit /</a>
            <a href="<?= get_car_link($car,'delete') ?> "> delet /</a>
            <a href=" <?= BASE_URL ?>/edit-list "> editacni list aut </a>
        </div>

</div>


<div class="container-car-detail">
    <?php
    include_once "_partials/footer.php" ?>
</div>
	
