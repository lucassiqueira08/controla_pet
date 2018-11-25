
// ============== Menu notificação ==============

$('#ckbSino').attr('checked', false)
$('#notificacoes').addClass('hide')
// document.getElementById("ckbSino").checked = false;
// document.getElementById("notificacoes").className = "hide";
function fadeInOut(){
	document.getElementById("ckbSino").click();
	if(document.getElementById("ckbSino").checked){
		document.getElementById("sinoNotificacao").className = "sinoNotificacaoAtivo";
		document.getElementById("notificacoes").className = "show";
	}
	else {
		document.getElementById("sinoNotificacao").className = "sinoNotificacaoInativo";
		document.getElementById("notificacoes").className = "hide";
	}

};

function Mudar(el){
	var display = document.getElementById(el).style.display;
	if(display == "none"){
		document.getElementById(el).style.display = 'block';
  }

	 else{

   	document.getElementById(el).style.display ='none';
   }
  if(display == "block")
  {
    document.getElementById(el).style.display ='none';
  }
}

function MudarFechar(el){
  var display = document.getElementById(el).style.display;
  if(display == "block")
  {
    document.getElementById(el).style.display ='none';
  }
}



function change(elemento){
	document.getElementById(elemento).className.replace("invis", "");
}

function verifica_horario_notificacao(dataJson){
  var d           = new Date();
  var hora_atual  = d.toString().substring(16,24);

  for (var item in dataJson) {
    var hora  = (dataJson[item]['data_solicitacao']).substring(11,19);
    var dono  = dataJson[item]['id_animal__cpf_cliente__nome'];
    if (hora == hora_atual) {
      alerta("Hora de fazer um atendimento ao Bixinho do " + dono,"aviso",7000);
    }

  }
}

$.get('/get_notificacao', function(data){
  var notificacoes = $('#notificacoes')
  var notificacao  =
                     '<div class="card card-body">'
                   +   '<ul>'
                   +     '<li class="notificacao">'
                   +       '<p class="notificacaoHorario">##hora</p>'
                   +       '<p class="notificacaoBichinho">##bichinho</p>'
                   +       '<p class="notificacaoProcedimento">##procedimento</p>'
                   +     '</li>'
                   +   '</ul>'
                   + '</div>';

	dataJson = JSON.parse(data)

  for (var item in dataJson) {
    var id                    = dataJson[item]['id'];
    var data                  = (dataJson[item]['data_solicitacao']).substring(0,10).replace("-","/");
    var hora                  = (dataJson[item]['data_solicitacao']).substring(11,16);
    var dono                  = dataJson[item]['id_animal__cpf_cliente__nome'];
    var especie               = dataJson[item]['id_animal__especie'];
    var cpf_cliente           = dataJson[item]['id_animal__cpf_cliente__cpf'];
    var procedimento_clinico  = dataJson[item]['atendimentoprocclinico_atendimento__id_proc_clinico__nome'];
    var procedimento_estetico = dataJson[item]['atendimentoprocestetico_atendimento__id_proc_estetico__nome'];
    var responsavel           = dataJson[item]['feitopor_atendimento__id_funcionario__primeiro_nome'];
    var status_atendimento    = dataJson[item]['statusatendimento_atendimento__id_status__nome'];

    var procedimento          = dataJson[item]['atendimentoprocclinico_atendimento__id_proc_clinico__nome'] != null ? dataJson[item]['atendimentoprocclinico_atendimento__id_proc_clinico__nome'] : dataJson[item]['atendimentoprocestetico_atendimento__id_proc_estetico__nome'] != null ? dataJson[item]['atendimentoprocestetico_atendimento__id_proc_estetico__nome'] : "Sem procedimento!";
    var final                 = notificacao.replace("##hora", hora).replace("##bichinho",dono).replace("##procedimento",procedimento);


    notificacoes.append(final)
  }
	let timerId = setInterval(() => verifica_horario_notificacao(dataJson), 1000);
})

//============================================

$(function(){
	var atual_fs, next_fs, prev_fs;

	$('.next').click(function(){
		atual_fs = $(this).parent().parent();
		next_fs  = $(this).parent().parent().next();

		$('#progress li').eq($('fieldset').index(next_fs)).addClass('ativo');
		atual_fs.hide();
		next_fs.show();
	});

	$('.prev').click(function(){
		atual_fs = $(this).parent().parent();
		prev_fs  = $(this).parent().parent().prev();

		$('#progress li').eq($('fieldset').index(atual_fs)).removeClass('ativo');
		atual_fs.hide();
		prev_fs.show();
	});

	$('.formEtapas input[type=submit]').click(function(){
		return false;
	});

});

//=====================Campo data=======================

$( function() {
  $( "#Data" ).datepicker();
  $( "#Data2" ).datepicker();
});

$("#formularioModal :input").prop('readonly', true);
$('.btnEditar').click(function(){
	$("#formularioModal :input").prop('readonly', false);
});

//=====================Modal=======================

$('#FormModal').on('shown.bs.modal', function () {
  $('#FormModal').trigger('focus')
})

$(window).on('load',function(){
    $('#modalBemVindo').modal('show');
});

function DisableCampos(){
		$("input").attr('disabled','disabled');
}
function EditFields(){
	if ($("input").attr('disabled','disabled')) {
		$("input").removeAttr('disabled');
	}
	else {
		$("input").attr('disabled','disabled');
	}
}

//=====================File Input=======================
// const FileInput     	= $("#formEtapasFileInput")
// const FileInputBtn  	= $("#fileInputBtn")
// var   fileInputSpan   = document.getElementById("fileInputSpan")

// FileInputBtn.addEventListener("click", function(){
// 	FileInput.click();
// });
// FileInputBtn.addEventListener("change", function(){
// 	if (FileInput.value) {
// 		fileInputSpan.innerHTML =  FileInput.value;//.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/);
// 	}
// 	else {
// 		fileInputSpan.innerHTML = "Nenhum arquivo selecionado...";
// 	}
// });

// }
//=====================File Input=======================

$(document).ready(function() {
var x = 1;
var maximo      = 10;
var container       = $(".containerMais");
var add_button      = $(".btnAdd");

$(add_button).click(function(e){
    e.preventDefault();
    if(x < maximo){
		var conteudo	= '<div class="centralizado"><input type="text" class="inputProduto" name="produto' + x +'"> &nbsp; &nbsp;<input type="text" class="inputValor dinheiro" name="valor' + x +'"><a class="delete"><img class="icone" src="/static/img/delete.png" alt="Deletar"></a></div>';
		conteudo 		= conteudo.replace(/##/gi, "'");
        x++;
        container.append(conteudo); //add input box
    }
else
{
alert('Você atingiu o limite de produtos!')
}
});

$(container).on("click",".delete", function(e){
    e.preventDefault(); $(this).parent('div').remove(); x--;
})
});

// ============== Func MenuOpções ==============



function OpenMenu(evt, menuName, tabela = false) {
  var i, x, tablinks;
  x = document.getElementsByClassName("menuOpcoes");
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < x.length; i++) {
     tablinks[i].className = tablinks[i].className.replace(" border-orange", "");
  }
	if (tabela) {
  	document.getElementById(menuName).style.display = "table";
  	document.getElementById(menuName).style.display = "table";
	}
	else {
  	document.getElementById(menuName).style.display = "flex";
	}
  evt.currentTarget.firstElementChild.className += " border-orange";
}

//FUNC EXIBE OU ESCONDE ELEMENTOS
function HideShow(show, hide1, hide2=null, hide3=null, hide4=null){
	document.getElementById(show).style.display  = "block";
	document.getElementById(hide1).style.display = "none";
	if(hide2 != null)
		document.getElementById(hide2).style.display = "none";
	if(hide3 != null)
		document.getElementById(hide3).style.display = "none";
	if(hide4 != null)
		document.getElementById(hide4).style.display = "none";
}



//---FILE INPUT ------------------------------------------------
function addFile(){
	var files = $("#fileInput")[0].files
	for (var i=0; i<file.length; i++){
		alert(files[i].name)
	}
}
