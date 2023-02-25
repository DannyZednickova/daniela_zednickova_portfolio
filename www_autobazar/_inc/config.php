<?php

//PART OF HTACCESS CONFIG - php_value include_path:
set_include_path(get_include_path() . PATH_SEPARATOR . 'C:\www\www_autobazar');

// show all errors
ini_set('display_startup_errors', 1);
ini_set('display_errors', 1);
error_reporting(E_ALL & ~E_NOTICE);

//required - sessions and cookies package
// Start a Session
if (!session_id()) {
    @session_start();
}

// Initialize Composer Autoload
require_once __DIR__ . '/../vendor/autoload.php'; //packages - 1.flash messages


// constants & settings (i will never change them - that is done during our app)
define('BASE_URL', 'http://localhost/www_autobazar');
define('APP_PATH', realpath(__DIR__ . '/../'));


// database 'autobazar; for real shit
$databaseAD = new PDO('mysql:host=localhost;dbname=autobazar;charset=utf8mb4', 'root', 'root');
$databaseAD->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$databaseAD->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);

//PHP DELIGHT AUTH
$auth = new \Delight\Auth\Auth($databaseAD);

/**
 *
 * // connect to db and error logs ( errmode_exception atp ) to a new file - i can chack whenever there is a mistake in SQL and my app will still carry on
 *
 * try {
 * $query  = $db->query("SELECT * FROM tags" );
 *
 * echo'<pre>';
 * echo print_r( $query->fetchAll( PDO::FETCH_ASSOC ));
 * echo'</pre> ';
 * }
 *
 * catch ( PDOException $e ) {
 * $error = date( 'j M Y, G:i') . PHP_EOL;
 * $error .= '-----------------------------' . PHP_EOL;  // .= znamená, že na string error vytvořený výše se nalepí tento string na tomto řádku! ... pokud neudělám .= tak si budu furt $error přepisovat!
 * $error .= $e ->getMessage() . ' in [ ' . __FILE__ .' : ' . __LINE__ . '] ' . PHP_EOL . PHP_EOL; // getMessage is object method - in __file__ and __line__tels us where it is"
 * file_put_contents( APP_PATH . '/_inc/error.log', $error, FILE_APPEND ); // file append zpusobí, že file_put_content nebude stále přepisovat data, ale PŘIPÍŠE je!
 * }
 **/


/*
 *  global functions
*/

include_once '_inc/functions-string-format.php'; //funcstions format all the strings, mainly taken from database....
include_once '_inc/functions-general.php'; // all system functions /segments , danny print etc
include_once '_inc/functions-get-car.php'; //get details and get tips - functions shows tips for cars and getting details for ist of cars
include_once '_inc/arrays.php'; //all the arrays i set for my project
include_once '_inc/functions-filter-car.php'; //get a car - main function based on filter

