<?php

/**
 * main function takes care about getting cars from database based on filter which is shown in home.php and cars.php
 *

 */

function get_cars(array $filter
)  // z metody $_GET formular // ve $filter mam ulozene vsechny udaje ktere zadavam ve formulari... + tomu rikam, ze to je to ve forme array
{
    global $databaseAD;

    $where = [];
    $queryParams = [];

    foreach (['znacka', 'palivo'] as $condition) {
        if (!empty($filter[$condition])) {
            $where[] = "$condition = :$condition"; //tady mam ulozeno co hledam (objektivne), ze bylo zadano znacka, palivo, kilometry ... atp...
            $queryParams[$condition] = $filter[$condition];
            // tady mam ulozeno uz konkretne bmw, nafta, 0-50.000 km // ZEPTAT SE - proc nemuzu nechat jen $filter[$confition] - proc to musim davat do nove promene.... ???
        }
    }

    $sql = ' SELECT * FROM cars';

    foreach (['cena', 'kilometry', 'rok'] as $conditionName) {
        if (!empty($filter[$conditionName])) {
            $conditionValue = $filter[$conditionName];
            $range = explode('-', $conditionValue); // vytvori pole $range[0] a


//		$where[] = $conditionName . ' BETWEEN ' . $range[0] . ' AND ' . $range[1];
            $where[] = $conditionName . ' BETWEEN :' . $conditionName . '_min AND :' . $conditionName . '_max';    // rok BETWEEN :rok_min AND :rok_max
            $queryParams[$conditionName . '_min'] = $range[0];
            $queryParams[$conditionName . '_max'] = $range[1];
        }
    }

    $dph = $_GET ['dph'] ?? null;
    if ($dph) {
        $where[] = ' dph = 1 ';
    }

    if ($where) {
        $sql .= ' WHERE ';
        $sql .= implode(' AND ', $where);
    }

    if (isset($_GET['orderby']) && ($_GET['orderby'] == 'cenasestupne') ){
        $sql .= ' ORDER BY cena ASC ';
    }

    if (isset($_GET['orderby']) && ($_GET['orderby'] == 'cenavzestupne') ){
        $sql .= ' ORDER BY cena DESC ';
    }
      if (isset($_GET['orderby']) && ($_GET['orderby'] == 'kmsestupne') ){
        $sql .= ' ORDER BY kilometry ASC ';
    }

    if (isset($_GET['orderby']) && ($_GET['orderby']  == 'kmvzestupne')) {
        $sql .= ' ORDER BY kilometry DESC ';
    }


    dannyprint($sql);


    $querycar = $databaseAD->prepare($sql);
    $querycar->execute($queryParams);


    if ($querycar->rowCount()) {
        $cars = $querycar->fetchAll(PDO::FETCH_ASSOC);
    } else {
        $cars = [];
    }
    return $cars;
}


/**
 * Functions take care about filtering form - basically format and automatise all of items in filter
 */


// dej mi znacky z databaze >P
function get_brands()
{
    global $databaseAD;

    $sql = 'SELECT DISTINCT znacka FROM cars ORDER BY znacka ';

    $result = $databaseAD->query($sql)->fetchAll(PDO::FETCH_NUM);
    $brands = [];

    foreach ($result as $row) {
        $brands[] = $row[0];
    }

    return $brands;
}

//dej mi palivo z databaze

function get_fuel()
{
    global $databaseAD;

    $sql = 'SELECT DISTINCT palivo FROM cars ORDER BY palivo ';

    $result = $databaseAD->query($sql)->fetchAll(PDO::FETCH_NUM);
    $brands = [];

    foreach ($result as $row) {
        $fuels[] = $row[0];
    }

    return $fuels;
}


function make_options(array $options, $defaultValue)
{ // je to jedna z tech options

    $html = "";

    foreach ($options as $option) {  // $options = to, co si zvolim v tom rofmulari

        $isDefault = $option == $defaultValue;
        $html .= " <option value=\"$option\" " . ($isDefault ? 'selected' : '') . "> $option </option> ";
    }

    return $html;
}

function make_option_range($options, $defaultValue)
{
    $html = "";
    foreach ($options as $option => $range) {  // $options = to, co si zvolim v tom rofmulari
        $isDefault = $option == $defaultValue;
        $html .= " <option value=\"$option\" " . ($isDefault ? 'selected' : '') . "> $range </option> ";
    }
    return $html;
}










