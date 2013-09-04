function initialize() {
  var myLatlng = new google.maps.LatLng(-27.453337,-58.987152);
  var mapOptions = {
    zoom: 15,
    center: myLatlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  console.log("ladero");
  var map = new google.maps.Map(document.getElementById('mapaUbicacionInformatorio'), mapOptions);

  var marker = new google.maps.Marker({
      position: myLatlng,
      map: map,
      title: 'Informatorio'
  });
}

google.maps.event.addDomListener(window, 'load', initialize);

$(document).ready(function(){
  var clases = ["contMasInfoModulo1","contMasInfoModulo2","contMasInfoModulo3","contMasInfoModulo4","contMasInfoModulo5"];
  $(".imgModulo").mouseenter(function(){
    var id = $(this).attr('id').split('')[10];
    id = id - 1;
    var modulo = clases[id];
    $("." + modulo).animate({
      opacity: "show"
    }, "slow")
  })

  $(".imgModulo").mouseleave(function(){
    var id = $(this).attr('id').split('')[10];
    id = id - 1;
    var modulo = clases[id];
    $("." + modulo).animate({
      opacity: "hide"
    }, "slow")
  })
})