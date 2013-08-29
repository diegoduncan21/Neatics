$(document).ready(function() {
	function animar (sentido) {
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


	/*Animacion en el home barrita*/
	$(".perfil").mouseout(function(){
		$(".secreto1").attr('class','secreto');
	});

	$(".perfil").mouseenter(function(){
		$(".secreto").attr('class','secreto1');
	});

	$(".perfil1").mouseout(function(){
		$(".secreto1").attr('class','secreto');
	});

	$(".perfil1").mouseenter(function(){
		$(".secreto").attr('class','secreto1');
	});
})