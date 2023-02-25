<?php

include_once __DIR__ . '/_inc/config.php';


// Require composer autoloader
require __DIR__ . '/vendor/autoload.php';

// Create Router instance
$router = new \Bramus\Router\Router();


//home
$router->get('/', function () { require_once 'home.php'; });
$router->get('/cars', function () { require_once 'cars.php'; });
$router->get('/car_detail/(\d+)/(\w+)-(\d+)', function($name) {
    require_once 'car-detail.php';
});

//ADMINISTRATION
$router->match('GET|POST', '/reg', function() use ($auth) { require_once '_admin/register.php';  });
$router->match('GET|POST', '/login', function() use ($auth) { require_once '_admin/login.php';  });
$router->match('GET|POST', '/logout', function() use ($auth) { require_once '_admin/logout.php';  });
$router->match('GET|POST', '/add', function() { require_once '_admin/add.php';  });
$router->get('/edit-list', function () { require_once '_admin/edit-list.php'; });
$router->post('/edit', function () { require_once '_admin/edit-car.php'; });
$router->post('/delete', function () { require_once '_admin/delete-car.php'; });


//EDIT AND DELETE a CAR - delete/id + edit/id
$router->get('/edit/(\d+)', function($name) {
    require_once '_admin\edit.php';
});
$router->get('/delete/(\d+)', function($name) {
    require_once '_admin\delete.php';
});

// Run it!
$router->run();


//old version of routing
/*$routes = [

    '/' => [
        'GET' => 'home.php ',
    ],
    '/home' => [
        'GET' => 'home.php ',
    ],
    '/cars' => [
        'GET' => 'cars.php',
        'POST' => '_inc/cars-listing.php',
    ],
    '/car_detail' => [
        'GET' => 'car-detail.php',
    ],


// ADMINISTRATION
    '/login' => [ // log in to admin ...
        'GET' => '_admin/login.php',
    ],
    '/edit-list' => [ // list of editing cars...
        'GET' => '_admin/edit-list.php',
    ],
    '/add' => [
        'GET' => 'add.php',
        'POST' => '_admin/add-car.php',
    ],
    '/edit' => [
        'GET' => 'edit.php',
        'POST' => '_admin/edit-car.php',
    ],
    '/delete' => [
        'GET' => 'delete.php',
        'POST' => '_admin/delete-car.php',
    ],
];


$pages = segment(1);
$method = $_SERVER['REQUEST_METHOD'];  //this tells me if its get or post method....


if (!isset($routes ["/$pages"][$method])) {  //if in routes is NOT /pages (/delete, /post, / ) and also if there is NO method, then show 404

    show_404();
}


require $routes["/$pages"][$method]; // print_r = home.php if i am at "/" pages just....


*/
