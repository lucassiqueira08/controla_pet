//=====================Formulário em etapas=======================
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
} );

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