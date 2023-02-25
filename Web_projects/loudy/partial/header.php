<?php 

   $page_name = basename($_SERVER['SCRIPT_NAME'], '.php');
   if ( $page_name == 'index' ) $page_name = 'home';
    include 'partial/arrays.php';

 ?>

<!DOCTYPE html>
  <html>
  <head>

 
	<meta charset="utf-8">
	<title><?php echo  ucfirst($page_name) ?> / Cestovateslký blog </title>
  <meta name="description" content="LOUDY NA CESTĚ - Motorky, cizina, ztraceni, hladoví, spocení, usměvaví: To by nás na cestě světem na motorce asi popsalo. Blázni z Kroměříže milující motorky a to se na nich ztratit za každou cenu :) ">
  <meta name="keywords" content="moto, cestovatelé, motorky, moto cestovatelé, Loudy na cestě, motorkáři, moto blog, Kroměříž">
  <meta name="author" content="Danny Zedníčková">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="assets/css/normalize.css">
	<link rel="stylesheet" href="assets/css/all.css">
	<link rel="stylesheet" href="assets/css/animate.css">
  <!-- Place your kit's code here -->
  <link href="https://fonts.googleapis.com/css?family=Anton&display=swap" rel="stylesheet">
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
	<link rel="stylesheet" href="assets/css/loudastyle.css">
	<meta name="viewport" content="width=device-width, initial-scale=1">

      <!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-52B2SFK');</script>
<!-- End Google Tag Manager -->

<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-52B2SFK"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
      <!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-154459289-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-154459289-1');
</script>


	<!--[if lt IE 9]>
		<script src="http://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.2/html5shiv.min.js"></script>
		<script src="http://cdnjs.cloudflare.com/ajax/libs/selectivizr/1.0.2/selectivizr-min.js"></script>
	<![endif]-->
</head>


<body id = "home">


        <!-- Main navigation -->
   <header>

   <nav id="menu" class="navbar">
        <ul class="navigation">
          <li class="endurotulaci"> 
            <a href="#home"> ZRAVÍME! - DANNY A PETR </a>
          </li>  
            <?php foreach ($top_menu as $hashtag => $nazev_menu) { echo ' <li class="nav"> <a href="' . $hashtag  .'">' . $nazev_menu . '</a></li> '; }  ?>
        </ul>
         <a href="https://www.facebook.com/loudynaceste"  target="_blank" >  <i class="fab fa-facebook-f"> </i> </a>
         <a href="https://www.instagram.com/dannyzednickovacz/"  target="_blank">  <i class="fab fa-instagram"> </i> </a> 
    </nav>



   <nav id="menu-hamburger" class="navbar-hamburger">

    <span><i class="fas fa-bars"></i></span>

    </nav>


    <nav id="menu-toggle" class="navbar-toggle">

      <div class="hamburger-left">
        <?php foreach ($top_menu as $hashtag => $nazev_menu) { echo ' <span class="nav-hamburger"> <a href="' . $hashtag  .'">' . $nazev_menu . '</a></span> '; }  ?>

      </div>
      <span><i class="far fa-window-close"></i></span>
    </nav>






         
