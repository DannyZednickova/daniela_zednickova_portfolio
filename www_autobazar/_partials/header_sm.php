<?php

$page_name = basename($_SERVER['SCRIPT_NAME'], '.php');
if ($page_name == 'index') {
    $page_name = 'home';
}

?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title> <?php
        echo ucfirst($page_name) ?> / Autobazar Drábek </title>

    <link rel="stylesheet" href="<?= asset('/css/normalize.css') ?>">
    <link rel="stylesheet" href="<?= asset('/css/all.css') ?>">
    <link rel="stylesheet" href="<?= asset('/css/animate.css') ?>">
    <link href="https://fonts.googleapis.com/css?family=Anton&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap">
    <link rel="stylesheet" href="<?= asset('/css/abd-style.css') ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Global site tag (gtag.js) - Google Analytics -->

    <!--[if lt IE 9]>
    <script src="http://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.2/html5shiv.min.js"></script>
    <script src="http://cdnjs.cloudflare.com/ajax/libs/selectivizr/1.0.2/selectivizr-min.js"></script>    <![endif]-->
</head>

<body>

<section class="topbar container">

    <div class="title">
        <a href=""><h1>AUTO BAZAR DRÁBEK</h1></a>
    </div>

    <div class="contacts">

        Volejte: <strong class="call"> 777 144 288 </strong>

    </div>
</section>

<section class="navigation container">

    <div class="nav-link"><a href="<?= BASE_URL ?>"> HOME </a></div>
    <div class="nav-link"><a href="<?= BASE_URL . '/cars' ?>"> CARS </a></div>
    <div class="nav-link"><a href="<?= BASE_URL ?>"> NAVIGACE </a></div>
    <div class="nav-link"><a href="<?= BASE_URL ?>"> NAVIGACE </a></div>
    <div class="nav-link"><a href="<?= BASE_URL . '/edit-list' ?>"> EDIT </a></div>

</section>

<?= flash()->display(); ?>


	