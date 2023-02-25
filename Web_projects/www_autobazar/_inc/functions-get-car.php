<?php

/**
 *  function to get all af details for specific car and show it - based on ID
 *  plus there is also a function :car tip: which gets details of a car we want and show them in the bottom of the page in CAR TIPS....
 */

function get_car_detail($id = 0, $auto_format = true)
{
    if (!$id && !$id = segment(2)) {
        return false;
    }

    global $databaseAD;
    $query = $databaseAD->prepare("
			SELECT * FROM `cars`
		    WHERE id = :id 
	");

    $query->execute(['id' => $id]);

    if ($query->rowCount() === 1) {
        $result = $query->fetch(PDO::FETCH_ASSOC);

        if ($auto_format) {
            $result = format_cars($result); //pouzivam funkci z function - string, funkci format_post
        } else {
            $result = (object)$result;
        }
    } else {
        $result = [];
    }

    return $result;
}

;


/**
 * GET edit list FOR CARS IN 'CAR DETAILS LISTING '
 */

function get_edit_list()
{
    global $databaseAD;
    $sql = "SELECT id, znacka, typ, cena, rok, insertdate FROM cars  ORDER BY insertdate DESC";

    $editList = $databaseAD->query($sql)->fetchAll(PDO::FETCH_OBJ);

    return $editList;
}


/**
 * GET 4 tips FOR CARS IN 'CAR DETAILS LISTING '
 */

function car_tips_detail () {

    $sql = 	"SELECT id, znacka, typ, cena, motor, rok, kilometry FROM `cars`
		WHERE tip_auto = :tip
		LIMIT 4 ";

global $databaseAD;
	$query = $databaseAD->prepare( $sql );

	$query->execute(['tip' => 1]);


 if ( $query -> rowCount() )
 {
 	 $tip = $query -> fetchAll( PDO::FETCH_OBJ );
 }

 else
 {
 	$tip = [];

 }

 return $tip;

}



function get_car_link($car, $type = 'car_detail')
{
    if (is_object($car)) {
        $id = $car->id;
        $znacka = $car->znacka;
        $rok = $car->rok;
    } else {
        $id = $car['id'];
        $znacka = $car['znacka'];
        $rok = $car['rok'];
    }
    $znacka = strtolower(trim(($znacka)));
    $link = BASE_URL . "/$type/$id";

    if ($type === 'car_detail') {
        $link .= "/$znacka-$rok";
    }


    $link = filter_var($link, FILTER_SANITIZE_URL);
    return $link;
}

