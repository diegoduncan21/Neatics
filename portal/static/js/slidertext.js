$(document).ready(function() {
	(function($) {
		var slider = function(elem) {
			var elements = $(elem).children();
			var i = 1
			var animar = function() {
				if (elements.length != i) {
					$(elements[i-1]).fadeOut(function() {
						$(elements[i]).fadeIn();
						i++;
						setTimeout(animar,3000);
					});
				} else{
					$(elements[i-1]).fadeOut(function() {
						$(elements[0]).fadeIn();
						i=1;
						setTimeout(animar,3000);
					});
				};
			};
			$.each(elements,function() {
				$(this).hide();
			})
			$(elements[0]).fadeIn();
			setTimeout(animar,3000)
		};
		$('.slidertext').data({ slider : slider })
	})(jQuery)
})