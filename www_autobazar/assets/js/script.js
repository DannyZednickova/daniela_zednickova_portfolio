
(function($) {




$({ countNum: $('.code').html() }).animate({ countNum: 100 }, {
            duration: 800,
            easing: 'linear',
            step: function () {
            $('.code').html(Math.floor(this.countNum) + "+ VOZIDEL");
        },
        complete: function () {
            $('.code').html(this.countNum + "+ VOZIDEL");
            //alert('finished');
        }
        });





//BOUNCE ANIMACE

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




//FIND A CAR TOGGLE

var findButton = $('.find-button');
var findForm = $('.find-form');

findButton.on ('click', function(event) {
	findForm.slideToggle();

});

$('.edit-button-alert').click(function() {
    return confirm('Opravdu to chceš udelat? ')
  });

$('.fa-times').click(function() {
    return confirm('Opravdu to chceš smazat? ')
  });



}(jQuery));