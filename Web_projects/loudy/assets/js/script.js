
$(function() {

var title = $('.title');
var sponzori = $('.partners');






//ANIMACE ZE SPODU A Z BOKU NA ELEMENTY...
  $(window).scroll(function() {
    if ($(document).scrollTop() > 100) {
      title.fadeOut()
    } else {
      title.fadeIn();
    }
  });



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








//ODPOČET MINUT DO ODJEZDU
// Set the date we're counting down to
var countDownDate = new Date("Jul 10, 2021 08:00:00").getTime();

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





//aktivni/pasivni pridani class do horniho menu

    $('#menu li a').on('click', function( event ){
    $('li a.current').removeClass('current');
    $(this).addClass('current');
    


});



//aktivní button toggle :)

//$('button').click(function () {
//  $('ul').toggleClass('active');

//});




var menuToggle =$('#menu-toggle');
var menuHamburger =$('#menu-hamburger');
var closeIcon = $('.fa-window-close');
closeIcon.hide();
menuToggle.hide();
menuHamburger.on('click', function(){
  closeIcon.show();

  menuToggle.slideDown();
  event.stopPropagation();

});


var click = $('.closeIcon, body')


if ( menuToggle.length > 0 ) {
 click .on ('click', function() {

    menuToggle.slideUp();
  });
};






//jokes acordeon :D

var akordeon= $('.akordeon');
 akordeon.find('dd').hide();
 akordeon.find('dt').on ('click', function ( event ) {

    $(this).next().slideToggle() 
      .siblings('dd').slideUp();

    event.preventDefault();

    });





//scroll k #

var menu = $('.navigation'),
  menuLink = menu.find('a');

  menuLink.on ('click', function (event) {
      event.preventDefault();
      var id = this.hash;

      $('html,body').animate ({scrollTop: $(id).offset().top}, 1000, function() {
        window.location.hash = id;

      });

  });



//navigace zmtaveni
   $(window).scroll(function () {
      if ($(this).scrollTop() > 500) {
         $('.navbar').addClass('scroll-nav')
      }
      if ($(this).scrollTop() < 500) {
         $('.navbar').removeClass('scroll-nav')
      }
   });


//






//ajax k vypsani clanku pouzity s load funkci 

var a = $('.control-menu').find('a');

a.on('click', function ( event ){
  event.preventDefault();

  var href = $(this).attr('href');
  $('.show-article').load( href + ' .blog-articles'); //load is short version of ajax 

});






//AJAXOVÉ PŘÍKAZY S LOADINGEM

$html = $("html");

$(document).on({
    ajaxStart: function() { $html.addClass("loading");    },
     ajaxStop: function() { $html.removeClass("loading"); }    
});







//NAČÍST DALŠÍ OBSAH
var newsButton = $('.news-button');
var newsButtonSecond = $('.news-button-two');
var loadNextNews = $('.load-next-news');


loadNextNews.hide();
newsButtonSecond.hide();

newsButton.on('click', function( ){


  loadNextNews.slideDown();
  $('html, body').animate({
    scrollTop: ($('#blog').offset().top)
},500);

 newsButton.hide();
  newsButtonSecond.show();


});

newsButtonSecond.on('click', function() {


  loadNextNews.slideUp();
  newsButtonSecond.hide();
   newsButton.show();
     $('html, body').animate({
    scrollTop: ($('#news').offset().top)
},500);



}) ;








//back to top

var backToTop= $('<a>', {
     href: '#home',
     class: 'back-to-top',
     style: 'color:red',
     html: '<i class="fas fa-sort-up"></i>' 


    });

backToTop
  .hide()
  .appendTo( 'body')
  .on ('click', function () {
      $('html,body').animate ( { scrollTop: 0 }, 2000);
  });


  var win = $(window);
  win.on('scroll', function(){
    if ( win.scrollTop() >= 800 ) backToTop.fadeIn();
      else backToTop.hide();



  });


 });


//LOADING CELÉ PAGES
window.addEventListener("load", function(){
  const loader = document.querySelector(".loader");
  loader.className += " hidden";


});



