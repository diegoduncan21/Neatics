$(function() {

	var $uni = $(".universidad");
	var $checks_uni = $(".optionsRadios");
	

	$checks_uni.click(function() {
		if ($("input[name='optionsRadios']:checked").val() == "no") {
			$uni.hide();
		} else {
			$uni.show();
		}
	});

});