<?php

/**
 * @var \Delight\Auth\Auth $auth
 */
include_once __DIR__ . "/../_partials/header_sm.php";

?>

    <main class="container">
<?php

setcookie('logout', 1 , time() + (8640), "/" );
$auth->logOut();

// or

try {
    $auth->logOutEverywhereElse();
} catch (\Delight\Auth\NotLoggedInException $e) {
    header ('Location:http://localhost/www_autobazar/');
    die('Not logged in');
}

// or

try {
    $auth->logOutEverywhere();
} catch (\Delight\Auth\NotLoggedInException $e) {
    header ('Location:http://localhost/www_autobazar/');
    die('Not logged in');
}
header ('Location:http://localhost/www_autobazar/');

?>
    </main>
