<?php
mb_internal_encoding("utf-8");
$error = "";
$email = filter_var($_POST['email'], FILTER_VALIDATE_EMAIL);
$name = $_POST['name'];
$year = $_POST['year'];
$text = $_POST['text-email'];


if ($_POST) {
    if (isset( $name ) && $name &&   // exist? and if, is there something??
       isset ( $email) && $email &&
       isset ( $year ) && $year == date('Y') &&
       isset ( $text  ) && $text
        )
    {
        $header = 'From:' . $email;   //.= spojuje, nikoliv nahrazuje \n = novy radek,
        $header.= "\nMine-Version: 1.0\n";
        $header.= "Content-Type: text/html; charset=\"utf-8\" \n " ;
        $adress = 'daniela.zednickova@gmail.com';
        $subject = 'Nova zprava z www loudy na ceste';
        $success = mb_send_mail($adress, $subject, $text, $header);
        //.= spojuje, nikoliv nahrazuje \n = put it to new line
        if($success) {
            $error = "diky moc za email";
        }
        else {
            $error = "Bohuzel nam sprava nedosla, zkontroluj udaje ;]";
        }
    }

    else {
        $error = "Formular neni OK";
    }
}

?>

<?php
    if ($error)
    echo '<p>' . $error . '</p>';
?>
    <form class="form" method ="POST">
        <input type="text" name="name" placeholder="Kdo nám píše?">
        <input type="email" name="email" placeholder="Máš email? :)">
        <input type="number" name="year" placeholder="Jaký je rok? "> <small>/ antispam</small> <br>

        <textarea name="text-email" cols="80" rows="10" placeholder=" Copak bys rád věděl? :) Děkujeme! "></textarea><br>
            <input class="submit" type="submit" value="odeslat">
    </form>

