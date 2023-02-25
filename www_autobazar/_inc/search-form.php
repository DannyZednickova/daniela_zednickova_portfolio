<?php

$years = [
    '0-2000' => "méně než 2000",
    '2001-2005' => "2001 - 2005",
    '2006-2010' => "2006 - 2010",
    '2011-2015' => "2011 - 2015",
    '2016-2019' => "2016 - 2019",
    '2020-2060' => "Nejnovější",
];
$km = [
    '0-50000' => "méně než 50 000",
    '50000-100000' => "50 000 - 100 000",
    '100001-150000' => "100 000 - 150 000",
    '150001-200000' => "150 000 - 200 000",
    '200001-250000' => "200 000 - 250 000",
    '250001-300000' => "250 000 - 300 000",
    '300001-350000' => "300 000 - 350 000",
    '350001-500000' => "vice nez 350 000",
];

$cena = [
    '0-50000' => "méně než 50 000",
    '50000-100000' => "50 000 - 100 000,-",
    '100001-200000' => "100 000 - 150 000,-",
    '200001-300000' => "200 000 - 300 000,-",
    '300001-400000' => "300 000 - 400 000,-",
    '350001-400000' => "350 000 - 400 000,-",
    '400001-500000' => "400 000 - 500 000,-",
    '500001-600000' => "500 000 - 600 000,-",
    '600001-2000000' => "vice nez 600 000,-",
];

$orderby = [
    'cenasestupne' => "Ceny sestupne",
    'cenavzestupne' => "Cena vzestupne",
    'kmsestupne' => "Kilometry sestupne",
    'kmvzestupne' => "Kilometry vzestupne",
];
//$isDefault = $option[$range] == $_GET['rok'];
//		$html .= " <option value=\"$option\"> $option[$range] </option> ";
?>
<form action="<?= BASE_URL ?>/cars" method="get">
    <select name="znacka">
        <option value=""> Znacka</option>
        <?php
        echo make_options(get_brands(), $_GET['znacka'] ?? null) ?>
    </select> <select name="rok">
        <option value=""> Rok Výroby</option>
        <?php
        echo make_option_range($years, $_GET['rok'] ?? null) ?>

    </select> <select name="kilometry">

        <option value=""> Kilometry</option>
        <?php
        echo make_option_range($km, $_GET['kilometry'] ?? null) ?>

    </select> <select name="cena">
        <option value=""> Cena</option>
        <?php
        echo make_option_range($cena, $_GET['cena'] ?? null) ?>
    </select> <select name="palivo">
        <option value=""> Palivo / Pohon</option>
        <?php
        echo make_options(get_fuel(), $_GET['palivo'] ?? null) ?>
    </select>

    <div class="search-form-bottom">
        <select name="orderby">
            <option value=""> SERADIT PODLE</option>
            <?php
            echo make_option_range($orderby, $_GET['orderby'] ?? null) ?>
        </select>

        <label for="dph"> ODPOCET DPH </label> <input type="checkbox" name="dph" value="1">

        <input type="submit" value="vyhledat" class="filter-button">

    </div>

</form>



