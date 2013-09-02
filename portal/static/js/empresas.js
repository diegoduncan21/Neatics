function initialize() {
  var myLatlng = new google.maps.LatLng(-25.363882,131.044922);
  var mapOptions = {
    zoom: 4,
    center: myLatlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  var map = new google.maps.Map(document.getElementById('mapa-empresa'), mapOptions);

  var marker = new google.maps.Marker({
      position: myLatlng,
      map: map,
      title: 'Nombre de la empresa'
  });
}

google.maps.event.addDomListener(window, 'load', initialize);
