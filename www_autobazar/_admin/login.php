<?php


/**
 * @var \Delight\Auth\Auth $auth
 */
include_once __DIR__ . "/../_partials/header_sm.php";



if ($_SERVER['REQUEST_METHOD'] === 'POST') {
// nefunguje... nwm proc to nevidi $auth ... kdyz to vlastne vidi auth... a potrebuju se zbavit odesilani emailu...
    try {
        $auth->login($_POST['email'], $_POST['password']);  //pass 82008200aA-

        echo 'User is logged in';
    } catch (\Delight\Auth\InvalidEmailException $e) {
        die('Wrong email address');
    } catch (\Delight\Auth\InvalidPasswordException $e) {
        die('Wrong password');
    } catch (\Delight\Auth\EmailNotVerifiedException $e) {
        die('Email not verified');
    } catch (\Delight\Auth\TooManyRequestsException $e) {
    }

}


?>

    <div class="container">

        <h1>ADMINISTRATION </h1>

        <div class="login">
            <div class="heading">
                <h2> LOGIN </h2>
                <form method="post" action="">

                    <div class="input-group">
                        <i class="fa fa-user"></i>
                        <input type="text" name="email" class="form-login" placeholder="email">
                    </div>
                    <div class="input-group">
                        <i class="fa fa-lock"></i>
                        <input type="password" name="password" class="form-login" placeholder="Password">
                    </div>
                    <button type="submit" class="button log-in-button">login</button>
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