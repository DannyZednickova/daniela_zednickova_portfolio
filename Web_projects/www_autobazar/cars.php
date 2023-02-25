<?php

include_once __DIR__ . "/_partials/header.php";


try {
    $cars = get_cars($_GET);
} catch (PDOException $e) {
    $error = date('j M Y, G:i') . PHP_EOL;
    $error .= '-----------------------------' . PHP_EOL;  // .= znamená, že na string error vytvořený výše se nalepí tento string na tomto řádku! ... pokud neudělám .= tak si budu furt $error přepisovat!
    $error .= $e->getMessage() . ' in [ ' . __FILE__ . ' : ' . __LINE__ . '] ' . PHP_EOL . PHP_EOL; // getMessage is object method - in __file__ and __line__tels us where it is"
    file_put_contents(APP_PATH . '/_inc/error.log', $error,
        FILE_APPEND); // file append zpusobí, že file_put_content nebude stále přepisovat data, ale PŘIPÍŠE je!
    $results = false;
}
global $databaseAD;
$auth = new \Delight\Auth\Auth($databaseAD);

?>

<?php
dannyprint($_GET) ?>
    <div class="container">
        <h2> VYHLEDEJ VOZIDLA </h2>
        <section class="listing-car" style="
    BORDER: 1px grey solid;
    padding: 1em;">
            <div class="find-forms">
                <?php
                include_once "_inc/search-form.php" ?>
            </div>

        </section>
        <?
        if ($auth->isLoggedIn()) { ?>
            uzivatel je prihlasen <br>
            <div class="edit-links">
                <a href=" <?= BASE_URL ?>/edit-list "> editacni list aut </a>
            </div>
            <?
        } ?>
        <?php
        if (count($cars)) : foreach ($cars as $car) : $car = format_cars($car) ?>
            <div class="blog-card">
                <div class="meta">
                    <div class="photo">
                        <img src="http://localhost/www_autobazar/assets/img/car.jpg" alt="" class="car-listing-photo">
                        <!--  <div class="photo" style="background-image: url(https://storage.googleapis.com/chydlx/codepen/blog-cards/image-1.jpg)"></div> STARE RESENI FOTKY -->
                    </div>
                    <ul class="details">
                        <li class="author"><?= strtoupper($car->znacka) ?> </li>
                        <li class="date"> <?= ($car->kilometry) ?> </li>
                        <li class="tags">
                            <ul>
                                <li> <?= ($car->palivo) ?> &nbsp;|&nbsp;</li>
                                <li> <?= ($car->cena) ?> &nbsp;|&nbsp;</li>
                                <li><?= ($car->motor) ?> &nbsp;|&nbsp;</li>
                                <li> <?= ($car->rok) ?> </li>
                            </ul>
                        </li>
                    </ul>
                </div>
                <div class="description">
                    <h1>  <?= $car->znacka ?>&nbsp;<?= $car->typ ?>  </h1>
                    <h2><?= ($car->motor) ?>&nbsp;|&nbsp;<?= ($car->palivo) ?>&nbsp;|&nbsp;<?= ($car->rok) ?> </h2>
                    <h2> <?= $car->cena ?>  </h2>
                    <h2> <?= $car->kilometry ?>  </h2>
                    <p>  <?= ($car->historie) ?> </p>
                    <p class="read-more">
                        <a href=" <?= ($car->link) ?>   "> Vic info zde</a>
                    </p>
                </div>
            </div>

        <?php
        endforeach;
        else: ?>
            <p>
                NEMAM NIC </p>
        <?php
        endif ?>

    </div>
<?php
include_once __DIR__ . "/_partials/footer.php" ?>