$(document).ready(function() {
	(function($) {
	var animar =function (sentido) {
		if (sentido==1) {
			$('#logos').stop(true,false).animate({
				left:(sentido*-largo)+$('#logos').parent().innerWidth()
			}, 18000,'linear',function() {animar(-sentido)})	
		}else{
			$('#logos').stop(true,false).animate({
				left:0
			}, 18000,'linear',function() {animar(-sentido)})	
		}
	}
	
	var largo = 0;
	$('#banner-logo').css('width',$('#banner-logo').parent().innerWidth())
	$.each($('#logos').children(),function() {
		largo +=$(this).width()+10;
	})
	$('#logos').css('width',largo);
	var sentido = 1
	animar(sentido);

	})(jQuery)

})