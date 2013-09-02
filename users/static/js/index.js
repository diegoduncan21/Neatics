$(document).ready(function(){
	$("#boton").click(function() {
		$.getJSON("/users/names_users/",
			{
				user : "d",
			},
			function(data){
				$("#user").text(data.username);
			});
	});
	
});
