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
  $("#subMenuInformatorio").attr('class','subMenu_activado');

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

  var preg1 = false;
  $("#preguntasInformatorio1").click(function(){
      if (preg1){  
        $("#respuestasInfor1").slideUp(700);
        $("#preguntasInformatorio1").attr('class','preguntasInformatorio');
        preg1 = false;
      }else{
        $("#preguntasInformatorio1").attr('class','preguntasInformatorioActivado');
        $("#preguntasInformatorio3").attr('class','preguntasInformatorio');
        $("#preguntasInformatorio2").attr('class','preguntasInformatorio');
        $("#respuestasInfor2").slideUp(400);
        $("#respuestasInfor3").slideUp(400);
        $("#respuestasInfor1").slideDown(700);
        preg1 = true;
      }
  });

  var preg2 = false;
  $("#preguntasInformatorio2").click(function(){
      if (preg2){  
        $("#respuestasInfor2").slideUp(700);
        $("#preguntasInformatorio2").attr('class','preguntasInformatorio');
        preg2 = false;
      }else{
        $("#preguntasInformatorio2").attr('class','preguntasInformatorioActivado');
        $("#preguntasInformatorio3").attr('class','preguntasInformatorio');
        $("#preguntasInformatorio1").attr('class','preguntasInformatorio');
        $("#respuestasInfor1").slideUp(400);
        $("#respuestasInfor3").slideUp(400);
        $("#respuestasInfor2").slideDown(700);
        preg2 = true;
      }
  });

  var preg3 = false;
  $("#preguntasInformatorio3").click(function(){
      if (preg3){  
        $("#respuestasInfor3").slideUp(700);
        $("#preguntasInformatorio3").attr('class','preguntasInformatorio');
        preg3 = false;
      }else{
        $("#preguntasInformatorio3").attr('class','preguntasInformatorioActivado');
        $("#preguntasInformatorio2").attr('class','preguntasInformatorio');
        $("#preguntasInformatorio1").attr('class','preguntasInformatorio');
        $("#respuestasInfor1").slideUp(400);
        $("#respuestasInfor2").slideUp(400);
        $("#respuestasInfor3").slideDown(700);
        preg3 = true;
      }
  });  
})