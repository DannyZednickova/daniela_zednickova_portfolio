<?php

// TODO: POZNAMKA


/**
 * @var \Delight\Auth\Auth $auth
 */
include_once __DIR__ . "/../_partials/header_sm.php";


if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        $userId = $auth->register($_POST['email'], $_POST['password'], $_POST['username'],
            function ($selector, $token) {
            });

        echo 'We have signed up a new user with the ID ' . $userId;
    } catch (\Delight\Auth\InvalidEmailException $e) {
        die('Invalid email address');
    } catch (\Delight\Auth\InvalidPasswordException $e) {
        die('Invalid password');
    } catch (\Delight\Auth\UserAlreadyExistsException $e) {
        die('User already exists');
    } catch (\Delight\Auth\TooManyRequestsException $e) {
        die('Too many requests');
    }
    dannyprint($_POST);
}
// nefunguje... nwm proc to nevidi $auth ... kdyz to vlastne vidi auth... a potrebuju se zbavit odesilani emailu...

?>

    <div class="container">

        <h1>ADMINISTRATION </h1>

        <div class="login">
            <div class="heading">
                <h2> REGISTER </h2>
                <form method="post" action="">

                    <div class="input-group">
                        <i class="fa fa-user"></i>
                        <div class="input-group">
                            <input type="text" name="username" class="form-login" placeholder="username">
                        </div>
                        <div class="input-group">
                            <input type="text" name="email" class="form-login" placeholder="email">
                        </div>
                        <div class="input-group">
                            <input type="password" name="password" class="form-login" placeholder="Password">
                        </div>

                        <button type="submit" class="button log-in-button">Register</button>
                </form>
            </div>
        </div>
        <!--
    <div class="admin-box">
        <a href="<?= BASE_URL ?>/add-car" class="button"> PŘIDAT AUTO  </a> <br>
        <a href="<?= BASE_URL ?>/edit-car" class="button"> UPRAVIT AUTO </a> <br>
        <a href="<?= BASE_URL ?>/delete-car" class="button"> VYMAZAT AUTO  </a> <br>
    </div>
-->

    </div>

<?php
include_once "_partials/footer.php" ?>