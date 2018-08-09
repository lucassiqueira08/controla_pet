// -------------MASCARAS----------------
var cpf      = document.getElementById("cpf");
var rg       = document.getElementById("rg");
var celular  = document.getElementById("celular");
var telefone = document.getElementById("telefone");
var cep      = document.getElementById("cep");

function mascara_cpf() {
  var key = event.keyCode || event.charCode;

  if (cpf.value.length == 3){
    cpf.value =cpf.value + "."; ; 
  }

  if (cpf.value.length == 7){
    cpf.value = cpf.value + "."; 
  }

  if (cpf.value.length == 11){
    cpf.value = cpf.value + "-";
  }

  if( key == 8 || key == 46 ){
    cpf.value = "";
  }
}

function mascara_celular() {
  var key = event.keyCode || event.charCode;

  if (celular.value.length == 1){
    celular.value = "(" + celular.value ; 
  }

  if (celular.value.length == 3){
    celular.value = celular.value + ")"; 
  }
  if (celular.value.length == 9){
   celular.value = celular.value + "-" ; 
 }
 if( key == 8 || key == 46 ){
  cpf.value = "";
}

}
function mascara_rg() {
  var key = event.keyCode || event.charCode;

  if (rg.value.length == 2){
    rg.value = rg.value + "."; 
  }
  if (rg.value.length == 6){
    rg.value = rg.value + "."; 
  }
  if (rg.value.length == 10){
    rg.value = rg.value + "-"; 
  }
  if( key == 8 || key == 46 ){
    cpf.value = "";
  }

}
function mascara_telefone() {
  var key = event.keyCode || event.charCode;

  if (telefone.value.length == 1){
    telefone.value = "(" + telefone.value ; 
  }

  if (telefone.value.length == 3){
    telefone.value = telefone.value + ")"; 
  }
  if (telefone.value.length == 8){
   telefone.value = telefone.value + "-" ; 
 }
 if( key == 8 || key == 46 ){
   cpf.value = "";
 }
}
function mascara_cep() {
  var key = event.keyCode || event.charCode;

  if (cep.value.length == 5){
    cep.value = cep.value + "-"; ; 
  }

  if( key == 8 || key == 46 ){
    cpf.value = "";
  }
}

function mascara_apenas_numeros(e) {
  if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110]) !== -1 ||
    (e.keyCode == 65 && (e.ctrlKey === true || e.metaKey === true)) ||
    (e.keyCode == 67 && (e.ctrlKey === true || e.metaKey === true)) ||
    (e.keyCode == 88 && (e.ctrlKey === true || e.metaKey === true)) ||
    (e.keyCode >= 35 && e.keyCode <= 39)) {
    return;
}
if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {e.preventDefault();}
}


// -------------ALERTS----------------
function aviso_acessoAoSistema(){
  swal({
    title: "Esse funcionário terá acesso ao Sistema Controla Pet?",
    icon: "img/logoControlaPet.png",
    buttons: ["Não","Sim"],
    dangerMode: true,
  })
  .then((willDelete) => {
    if (willDelete) {
      swal("Acesso adicionado com sucesso!", 
      {
        icon: "success",
      }

      );
    } else {
      swal("Funcionário sem acesso!",
      {
       icon: "warning",
     }
     )}
    })
}


// -------------APIs----------------
function preenche_endereco(){
  url = "http://api.postmon.com.br/v1/cep/" + cep.value;
  var xhr = new XMLHttpRequest();
  xhr.open('GET', url, true);
  xhr.send();
  
  xhr.onreadystatechange = processRequest;
  function processRequest(e) {
    if (xhr.readyState == 4 && xhr.status == 200) {
      var response = JSON.parse(xhr.responseText);
      document.getElementById("endereco").value = response.logradouro;
      document.getElementById("bairro").value = response.bairro;
      document.getElementById("cidade").value = response.cidade;
    }
  }
}