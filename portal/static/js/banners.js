$(document).ready(function() {
      var opc = ['informatorio','empresas','empleos','polo','estudiar'];
      $(".logo_seccion").click(function(e) {
            $(".seccionActivado").toggleClass('seccionActivado');
            var clase = $(this).attr('class').split(' ')[0];
            opc.slice(opc.indexOf(clase),1)
            $.each(opc,function(i,e) {
                  $(".subMenu_"+e+"").slideUp(800);
            })
            $(this).toggleClass('seccionActivado');
            $(".subMenu_"+clase+"").slideDown(800,function(){
            });
      })
})