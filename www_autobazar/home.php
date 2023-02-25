<?php


include_once __DIR__ . "/_partials/header.php";
?>


    <main class="container">
    <section class="listing-car">
        <div class="button find-button">
            HLEDAT VOZIDLA
        </div>
        <div class="find-form">
            <?php
            include_once "_inc/search-form.php" ?>
        </div>
    </section>

    <div class="news">
        <div class="new-text"><i class="fas fa-car"></i></div>
        <div class="new-counter">
            <h2 class="code">0</h2>
            <h2>NA SKLADĚ!</h2>
        </div>
        <div class="news-text">
            NOVÉ VOZY PRÁVĚ DORAZILY! <br> AKCE! LETNÍ KOLA K VYBRANÝM VOZŮM ZDARMA<br> SOUTĚŽ! VÍCE INFO ZDE!<br>
        </div>
    </div>
    <div class="container smaller">
    <div class="box-container">
        <?php
        $tip = car_tips_detail();
        ?>

        <?php
        if (count($tip)) : foreach ($tip as $tip) : $tip ?>
            <div class="box-quote">
                <div class="quotes design">
                    <h2><a href=" <?= get_car_link($tip) ?>"><?= strtoupper($tip->znacka) ?> <?= $tip->motor ?> </a>
                    </h2>
                    <img class="car-tip" src="assets/img/cover.jpg" alt="Card image cap"> NAJETO: <?= number_format($tip->kilometry,
                        0, ' ', ' ') ?> km <br> VYROBENO: <?= $tip->rok ?> <br>
                    <span class="tip-inf"> CENA:  <?= number_format($tip->cena, 0, ',', ' ') . ',-' ?></span>
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
    <div class="offer">
        <div class="offer-one">
            <h2>Půjčovna vozíků</h2>
            <i class="fas fa-hand-holding"></i>
            <p>
                K zapůjčení nabízíme různé druhy přívěsných vozíků. </p>
            <div class="button"> BUTTON</div>
        </div>
        <div class="offer-two">
            <h2>Financování</h2>
            <i class="fas fa-funnel-dollar"></i>
            <p>
                K zapůjčení nabízíme různé druhy přívěsných vozíků. </p>
            <div class="button"> BUTTON</div>
        </div>
        <div class="offer-three">
            <h2> Znalecké posudky </h2>
            <i class="far fa-file-alt"></i>
            <p>
                K zapůjčení nabízíme různé druhy přívěsných vozíků. </p>
            <div class="button"> BUTTON</div>
        </div>
        <div class="offer-three">
            <h2> Poradenství </h2>
            <i class="fas fa-question"></i>
            <p>
                K zapůjčení nabízíme různé druhy přívěsných vozíků. </p>
            <div class="button"> BUTTON</div>
        </div>
    </div>

    <hr>

<?php
include_once "_partials/footer.php" ?>