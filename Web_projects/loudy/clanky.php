<?php 

   $page_name = basename($_SERVER['SCRIPT_NAME'], '.php');
   if ( $page_name == 'index' ) $page_name = 'home';

 ?>

  <?php
    include 'partial/arrays.php';
  ?>
  


<!DOCTYPE html>
  <html>
  <head>

 
	<meta charset="utf-8">
	<title><?php echo  ucfirst($page_name) ?> / Cestovateslký blog </title>
  <meta name="description" content="Motorky, cizina, ztraceni, hladoví, spocení, usměvaví: To by nás na cestě světem na motorce asi popsalo. BLázni z Kroměříže milující motorky a to se na nich ztratit za každou cenu :) ">
  <meta name="keywords" content="moto, cestovatelé, motorky, moto cestovatelé, loudy na cestě, motorkáři, moto blog, kroměříž">
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






   <nav id="menu" class="navbar">
       <div class="endurotulaci">
          <a href="https://www.loudynaceste.cz/"> ZPĚT NA HLAVNÍ STRÁNKU </a>

       </div>
            
         <a href="https://www.facebook.com/dannyzednickovacz"  target="_blank" >  <i class="fab fa-facebook-f"> </i> </a> 
         <a href="https://www.instagram.com/dannyzednickovacz/"  target="_blank">  <i class="fab fa-instagram"> </i> </a> 
    </nav>



   <nav id="menu-hamburger" class="navbar-hamburger">

    <span><i class="fas fa-bars"></i></span>

    </nav>


    <nav id="menu-toggle" class="navbar-toggle">

      <div class="hamburger-left">
        <li class="endurotulaci"> 
            <a href="#home"> ZPĚT NA HLAVNÍ STRÁNKU </a>
          </li> 
      </div>
      <span><i class="far fa-window-close"></i></span>
    </nav>





   


   
   </div>  
</body>


  <?php
    include 'partial/footer.php';
  ?>
      




  <!-- scripts -->
  <script src="https://kit.fontawesome.com/d668eb2f40.js" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.js"></script>
  <script src="js/script.js"></script>

</html>


