<?php

/**
 * String functions - system functions who takes care about format html codes and all details taken from database - it formats, trims, prepare for usind...
 *
 */

function plain($str)
{
    return htmlspecialchars($str, ENT_QUOTES);
}


/**
 * Word Limiter
 *
 * Limits a string to X number of words.
 *
 * @param string
 * @param int
 * @param string    the end character. Usually an ellipsis
 * @return    string
 */
function word_limiter($str, $limit = 100, $end_char = '&#8230;')
{
    if (trim($str) === '') {
        return $str;
    }

    preg_match('/^\s*+(?:\S++\s*+){1,' . (int)$limit . '}/', $str, $matches);

    if (strlen($str) === strlen($matches[0])) {
        $end_char = '';
    }

    return rtrim($matches[0]) . $end_char;
}


function format_cars($car)
{
    $car = array_map('trim', $car);
    $car['znacka'] = mb_strtoupper(plain($car['znacka']));
    $car['typ'] = mb_strtoupper(plain($car['typ']));
    $car['rok'] = plain($car['rok']);
    $car['kilometry'] = number_format(plain($car['kilometry']), 0, '.', ' ') . ' km';
    $car['motor'] = mb_strtoupper(word_limiter((plain($car['motor'])), 8));
    $car['barva'] = mb_strtoupper(word_limiter((plain($car['barva'])), 4));
    $car['palivo'] = mb_strtoupper(plain($car['palivo']));
    $car['cena'] = number_format(plain($car['cena']), 0, ',', ' ') . ',-';

    //LINK TO A PHOTO

    $car['photolink'] = "/assets/img/{$car['id']}";
    $car['photolink'] = filter_var($car['photolink'], FILTER_SANITIZE_URL);

    // SHORT DESCRIPTION OF THE CAR
    $car['vybava'] = word_limiter(ucfirst((mb_strtolower(plain($car['vybava'])))), 40);
    $car['historie'] = word_limiter(ucfirst((mb_strtolower(plain($car['historie'])))), 40);


    //LINK TO A CAR

    $car['link'] = get_car_link($car);

    return (object)$car;  //php has lots of function to work with array than object, so i use this my function to transform the array to object

}

;
