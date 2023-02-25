

//  POČÍTÁNÍ ....


function soucin (cislo) {
	return cislo * 3;
}
var vysledek = soucin(11);
console.log("Trojnásobek je:" + vysledek);






//SEZNAM PŘEDÁVÁNÍ FUNKCE DÁL V ELEMENTECH//
var menu = $('.zoznam');


menu.find('li:first-child, li:eq(2)').addClass('highlight');




//druhej list - předávání funkce dál v elementech
var ul=$('.list');
ul.on('click', 'li', function(){
	ul.append('<li> Ja jsem tu novy!!!</li>');

});




//MODRÉ FTIPKY A KOPÍRUJÍCÍ OD SEBE ATP.,//
//






var jokes = $('.jokes');
	copy = $('.copy') ;



	jokes.find('dd').hide();
	jokes.find('dt').on ('click', function ( event ) {


		$(this).next().slideToggle() //v rámci této funkce si našel DT = this
		//od něj najdí DALŠÍ (next) což jsou elementy dd a těm dej funkci TOGGLE. V moentě
		//kdy jeden dd je vysunut, dalšís sourozence (siblings) zasuň nahoru
			.siblings('dd').slideUp();


		var dt = $(this), //dt = $this - zkopíruje se JEN to co obsahuje TENTO jeden dt, ne všechny!!!
		dd = dt.next();

		var novejObsah = dt.text() + dd.text();
		copy.append( novejObsah + '<hr>' );


		event.preventDefault();



		});













//JUSTIN A LOADOVÁNÍ + TIMER

	var jb = $('.justin'), 
		loader = $('.loadin'), 
		siteWidth   = $('body').width(),
		justinWidth = jb.width();


	jb.on('click', function() {
		loader.fadeIn();
		$(this).animate({ left: (siteWidth - justinWidth)  }, 4000, function() {
			loader.fadeOut();

		});

	});

	jb.on('contextmenu', function(event) {
	
		loader.fadeIn();
			$(this).animate({ left: (siteWidth - justinWidth) }, 4000);
			setTimeout(function() {
				loader.fadeOut();
			}, 1500);

		// preventDefault, pretoze normalne ked kliknes pravym, vyskoci to menu kde je "inspect element" atd
		// a tomu chceme zabranit
		event.preventDefault();

	});









//MOJE POHYBY NA STRÁNCE - ORANŽOVEJ PIČUS
//



var slide = $('.hybese'),
	icon = $('.icon'),
	sirkastr = $('body').width(),
	sirkaelementu = slide.width();



	slide.on ('click', function () {
		icon.fadeIn();
	$(this).animate( { left: (sirkastr - sirkaelementu)}, 1000, function (){
		icon.fadeOut( 'slowly');

	});



	});









//OKOPÍROVANÁ ANIMACE FADE IN ZE SPODU


var $animation_elements = $('.animation-element');
var $window = $(window);

function check_if_in_view() {
  var window_height = $window.height();
  var window_top_position = $window.scrollTop();
  var window_bottom_position = (window_top_position + window_height);

  $.each($animation_elements, function() {
    var $element = $(this);
    var element_height = $element.outerHeight();
    var element_top_position = $element.offset().top;
    var element_bottom_position = (element_top_position + element_height);

    //check to see if this current container is within viewport
    if ((element_bottom_position >= window_top_position) &&
      (element_top_position <= window_bottom_position)) {
      $element.addClass('in-view');
    } else {
      $element.removeClass('in-view');
    }
  });
}

$window.on('scroll resize', check_if_in_view);
$window.trigger('scroll');









//GALERIE - opacity


var galerie = $('.galerie');
var zacatecniOpacity = galerie.find('img').css('opacity');
galerie.find('img').on ('mouseenter mouseleave', function ( event ){


	var opacity; 
	if (event.type === 'mouseenter')  opacity = 1;
	else opacity = zacatecniOpacity;
		$(this).stop().fadeTo (200, opacity);

});










//ANIMACE VÝSTUPU OBRÁZKU PO KLIKNUTÍ
var overlaydva = $('<div/>', { id: 'overlaydva'}); // vytvoří <div id="overlaydva"></div>
    overlaydva.appendTo('body').hide();

galerie.find('a').on('click', function( event ){

  var href = $(this).attr('href'),
      img = $('<img>', { src: href, alt: 'foto' });


    overlaydva.html( img ).show();
    event.preventDefault();

  });
overlaydva.on('click', function(){
  overlaydva.hide();
}) ;











//up 87 left 65 right  68 83

//PLAY IMG DOMACI ULOHA

var playimg = $('.playimg');

$(document).on ('keyup', function ( event ) {
	var posunout = event.keyCode,
		animuj = playimg.stop().animate;


		if ( posunout == 65 ) {
			playimg.stop().animate( {  left: "-=10px" } );
				

		}

		if ( posunout == 87 ) {
			playimg.stop().animate( {  top: "-=10px" });
				

		}


		if ( posunout == 68 ) {
			playimg.stop().animate( {  left: "+=100px" } );
				

		}


		if ( posunout == 83 ) {
			playimg.stop().animate( {  top: "+=10px" }  );
				

		}


	
});












/*LOADING YABLKO*/

	var button = $('.button'),
		overlay = $('#overlay');

	// progress barujeme
	button.on('click', function() {
		button.fadeOut('fast');
		overlay.fadeIn('fast', function() {
			overlay.find('.bar').animate({ width: '100%' }, 2000, function() {
			overlay.fadeOut('fast', function() {
				
		});
				button.fadeIn('fast');

			});

		});


	});






/*muj vadny loading.....*/
	var buttondva= $('.buttondva'),
		nacitac = $('.nacitac'),
		progress = $('.drzic');
			
			buttondva.on('click', function() {
				nacitac.show().animate( {width: '100%'}, 2000 , function () {
					progress.fadeOut( 'slow', function(){
				


					});


				});


			});




//SCROLOVANÍ NA STRÁNCE
//

var menu = $('.nav'),
	menuLink = menu.find('a');

	menuLink.on ('click', function (event) {

			event.preventDefault();

			var id = this.hash;

			$('html,body').animate ({scrollTop: $(id).offset().top}, 1000, function() {

				window.location.hash = id;


			});


	});















//GALERIE- JEDNA SEKCE ZMIZNE A PŘIDÁ SE DRUHÁ SEKCE






	var galleries = $('.gallery-set'),
		menuLinks = $('.controls a');

	// skryjeme vsetky galerie, okrem prvej
	galleries.not(':first').hide();

	// po kliknuti na link ideme robit veci
	menuLinks.on('click', function(event) {

		// ked sa pozrieme do HTML, vidime, ze hodnota href linku sa rovna idcku prislusnej sekcie
		var id = $(this).attr('href');

		// skryjeme galerie
		galleries.hide();

		// kedze href je rovny idcku galeriu, mozeme ju podla neho vytiahnut a nechat zobrazit
		// toto je to iste, ako keby sme napisali napr. $('#video').fadeIn();
		$(id).fadeIn();

		// klasika
		event.preventDefault();

	});















//BACK TO TOP
//


var backToTop= $('<a>', {
		 href: '#home',
		 class: 'back-to-top',
		 html: '<i class="fas fa-arrows-alt-v"></i>' 


		});

backToTop
	.hide()
	.appendTo( 'body')
	.on ('click', function () {
			$('html,body').animate ( { scrollTop: 0 }, 2000);
	});


	var win = $(window);
	win.on('scroll', function(){
		if ( win.scrollTop() >= 500 ) backToTop.fadeIn();
		  else backToTop.hide();



	});















	//ANIMACE POZADÍ OBRÁZLŮ SET TIMEOUT
	//
	

	var cover = $('.cover'),
		covers= $('.fadecover');

		covers.children(':not(:last)').hide(); //ODSTRANÍ JIŽ EXISTUJÍCÍ
		//FOTKY POD ANIMACÍ, TAKŽE NEVZNIKNE DIVNÝ PŘECHOD
		//
		//
		/*var sliderInterval = setInterval( function() { //VŠECHNY FUNKCE SE VE SKUTEČNOSTI 
			//pojí k windows, akorát to tam nikdo nepíše...

			covers.children(':last').fadeOut( 1500, function() {
				$(this).prependTo( covers );
			}).prev().fadeIn(1500);


		}, 3500);
		

		covers.on('click', function () {
			clearInterval ( sliderInterval);
		});*/



//OBJEKTIVNĚ ORIENTOVANÍ PROGRAMOVÁNÍ V JQUERY - SLIDER NA POZADÍ

var slider = {
	intervalID: null,
	running: false,

	set: function( id){
		this.intervalID = id;  //this = slider
	},

	

	get: function() {
		return 'IDcko intervalu je:' + this.intervalID;
	},



	start: function () {

		this.intervalID = setInterval( function() { //VŠECHNY FUNKCE SE VE SKUTEČNOSTI 
			//pojí k windows, akorát to tam nikdo nepíše...

			covers.children(':last').fadeOut( 500, function() {
				$(this).prependTo( covers );
			}).prev().fadeIn(500);


		}, 1000);

		this.running = true;

	},
	pause: function() {

		clearInterval(this.intervalID);
		this.intervalID = null;
		this.running = false; //funguje s tohhle, pauza na klikanec

	},
	resume: function() {
		if ( !this.intervalID) this.start();

	},

	toggle: function() {
		if (this.running) this.pause();
		else this.resume();
	}

}

slider.start();


covers.on('click', function () {
			slider.toggle();

		});














//ODPOČÍTÁVÍNÍ


// Set the date we're counting down to
var countDownDate = new Date("Jul 10, 2020 08:00:00").getTime();

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();
    
  // Find the distance between now and the count down date
  var distance = countDownDate - now;
    
  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
  // Output the result in an element with id="demo"
  document.getElementById("demo").innerHTML = days + "d " + hours + "h "
  + minutes + "m " + seconds + "s ";
    
  // If the count down is over, write some text 
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("demo").innerHTML = "A JSME VZITÍ";
  }
}, 1000);











//ANIMACE
var animace = $('.odleti');
	animace.css({ position: 'relative' })
			.addClass ('round-round-baby')
			.animate( { left: 400 }, {  //animace se vrství na sebe
				duration: 1000,//můžu ale animaci dát objekt a zakázat vrstvení a obě se sputí sama
				//easing: 'swing' - můžeme používat i u jQUery - stjně jako css :) 
				queue: false,


			})
			//.delay(2000) zdržení mezi animacemi
			.animate( { top: -400}, 500);


//animace dva

var animacedva = $('.hybesenaklik');
	animacedva.css({ position: 'relative' })
	.on ('click', function () {

		$(this).animate( {left: '+=50' }); //po kazdém kliknutí posune o padesát
	});
//animace TŘI


	var animatri= $('.tocimsenaklik');
	animatri.css({ position: 'relative' })
	
	animatri.on('click', function () {
		var e = $(this),
			className = 'round-round-baby';
			
			e.toggleClass(className); //roztočí a zastaví animaci

	});

//BAREVNÉ ANIMACE NA MENU A LI ELEMENTY 
//
//

var colors = [ '#3b0ae1', '#f6be00', '#e64134', 'black'];


$('.animacepozadi').find( 'h1' ).on('mouseenter', function() {
	if ( $(this).is(':animated')) return; //toto zajistí neopakování animace//

	var newColor = colors [Math.floor(Math.random() * colors.length)];
	$(this).animate({ backgroundColor: newColor });


});






//PŘIDÁNÍ HTML DO STRÁNKY



$('#box').append (
	$('<div/>')
	.attr ("id", "newDiv")
    .addClass ( "class novyclass jestejeden")
    .append ("<span/>")
    .text ("tENTO TEXT JE PŘIDÁN POMOCÍ JQUERY A NAPOJENEJ POMOCÍ APPEND NA DALŠÍ ELEMENT")
    );
    





    
//PŘIDÁNÍ A ODEBRÁNÍ CLASS V NAVIGACI

    $('#menu li a').on('click', function( event ){
    $('li a.current').removeClass('current');
    $(this).addClass('current');
    event.preventDefault();


});









//animace skrolování a objevení obrázku
var cerna = $('<div/>', { id: 'cerna'}); // vytvoří <div id="overlaydva"></div>
    cerna.appendTo('body').hide();
$(window).on('scroll', function(){

  
      var img = $('<img>', { src: 'img/samurai/thumb-3.jpg', alt: 'foto',});
      	imgclass = img.addClass("overlayphoto");



    cerna.html( imgclass ).show("slow");
     event.stopPropagation();
     ; 

  });
cerna.on('click', function(){
 cerna.hide("slow");
 $(window).off('scroll'); //zabrání znovu zpuštění animace
 
}) ;




var a = $('.control-menu').find('a');

a.on('click', function ( event ){
	event.preventDefault();

	var href = $(this).attr('href');
	$('.vypsani-clanku').load( href + ' .clanky');

});