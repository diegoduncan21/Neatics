$(document).ready(function() {
	
	
	function flip(elem, duration){
		var $elem = $(elem);
		$elem.animate({width:'0%'}, duration || 100, function(){
			if($elem.hasClass("gray")){
				$elem.removeClass("gray");
				$elem.addClass("white");
				
			}else if ($elem.hasClass("white")){
				$elem.removeClass("white");
				$elem.addClass("gray");
			}
			$elem.animate({width:'100%'}, duration || 100 );
		});
	}
	
	var whites = [0,8,13,14,16,18,19];
	
	var grays = [1,3,6,7,10,12,15,17,20,22];
				  
	var squares = [];
	
	for(var i = 0; i <24; i++){
		
		var squareContainer = $("<div>");
		squareContainer.attr("class","squareContainer");
		squareContainer.appendTo("#squares-wrapper");
		
		var square = $("<div>");
		square.attr("class","square");
		square.appendTo(squareContainer);
		
		square.hover(function(){
			flip(this)
		});
		
		squares.push(square);
	}
	
	for(var w in whites){
		squares[whites[w]].addClass("white");
	}
	
	for(var g in grays){
		squares[grays[g]].addClass("gray");
	}
	
	
	window.setInterval(function(){
		
		window.setTimeout(function(){
			var index = Math.floor(Math.random()*24);
			flip(squares[index], 600);
		}, 100)
		
		window.setTimeout(function(){
			var index = Math.floor(Math.random()*24);
			flip(squares[index], 600);
		}, 300)
		
		window.setTimeout(function(){
			var index = Math.floor(Math.random()*24);
			flip(squares[index], 600);
		}, 500)

	}, 4000)
})
