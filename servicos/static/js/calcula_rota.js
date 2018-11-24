$("#buscar").on("click",function(){
  if ($("#destino").val().trim()!='' && $("#origem").val().trim()!='') {
    CalculaDistancia()
  }
  else {
    alerta("Por favor, digite uma origem e um destino válidos!", "aviso", 5000)
  }
})
function CalculaDistancia() {
  //Instanciar o DistanceMatrixService
  var service = new google.maps.DistanceMatrixService();
  var destinos =[$("#destino").val()]
  if($("#destino2").val().trim() != ''){
    destinos.push($("#destino2").val())
  }
  if($("#destino3").val().trim() != ''){
    destinos.push($("#destino3").val())
  }
  //executar o DistanceMatrixService
  service.getDistanceMatrix(
  {
        //Origem
        origins: [$("#origem").val()],
        //Destino
        destinations: destinos,
        //Modo (DRIVING | WALKING | BICYCLING)
        travelMode: google.maps.TravelMode.DRIVING,
        //Sistema de medida (METRIC | IMPERIAL)
        unitSystem: google.maps.UnitSystem.METRIC,
        //Vai chamar o callback
    }, callback);
  }
  //Tratar o retorno do DistanceMatrixService

function callback(response, status) {

  var formatter = new Intl.NumberFormat('pt-BR', {
    style: 'currency',
    currency: 'BRL',
    minimumFractionDigits: 2,
  });


    //Verificar o Status
    if (status != google.maps.DistanceMatrixStatus.OK){
      //Se o status não for "OK"
      alerta(status, "erro", 6000)

    }
    else {
      if (response.rows[0].elements[0].distance) {


        console.log(response)
        $('#informacoes').html(
          "<tr>"+
          "   <td>" +response.rows[0].elements[0].distance.text+"</td>"+
          "   <td>" +response.rows[0].elements[0].duration.text+"</td>"+
          "   <td>" +formatter.format(parseInt(response.rows[0].elements[0].distance.text)*4))+"</td>"+
          "</tr>"
        var zoom = 14
        //Atualizar o mapa
        var destinos = response.destinationAddresses


        var urlQuery = "https://maps.google.com/maps?saddr=" + response.originAddresses[0].replace(/\s/g, "+").replace(/\./g, "")
        for (var i = 0; i < destinos.length; i++) {
          if (i==0) {
            urlQuery += "&daddr=" + destinos[i].replace(/\s/g, "+")
          }
          else {
            urlQuery += "+to:" + destinos[i].replace(/\s/g, "+")
          }
        }
        urlQuery += "&output=embed&zoom="+zoom
        console.log(urlQuery);
        $("#map").attr("src", urlQuery);
        $('#modalRota').modal('show')
      }
      else {
        alerta("Por favor, digite uma origem e um destino válidos!", "aviso", 5000)
      }
    }
  }
