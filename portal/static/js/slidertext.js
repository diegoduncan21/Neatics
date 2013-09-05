$(document).ready(function() {
	(function($) {
		var slider = function(elem,tiem) {
			var elements = $(elem).children();
			var i = 1
			var tiempo = tiem;
			var animar = function() {
				if (elements.length != i) {
					$(elements[i-1]).fadeOut(function() {
						$(elements[i]).fadeIn();
						i++;
						setTimeout(animar,tiempo);
					});
				} else{
					$(elements[i-1]).fadeOut(function() {
						$(elements[0]).fadeIn();
						i=1;
						setTimeout(animar,tiempo);
					});
				};
			};
			$.each(elements,function() {
				$(this).hide();
			})
			$(elements[0]).fadeIn();
			setTimeout(animar,tiempo)
		};
		$('.slidertext').data({ slider : slider })
	})(jQuery)
})