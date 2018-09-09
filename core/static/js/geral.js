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
const FileInput     = $("#formEtapasFileInput")
const FileInputBtn  = $("#fileInputBtn")
var   fileInputSpan   = document.getElementById("fileInputSpan")

FileInputBtn.addEventListener("click", function(){
	FileInput.click();
});
FileInputBtn.addEventListener("change", function(){
	if (FileInput.value) {
		fileInputSpan.innerHTML =  FileInput.value;//.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/);
	}
	else {
		fileInputSpan.innerHTML = "Nenhum arquivo selecionado...";
	}
});

//=====================cheboxoesEstadia=======================
function checkboxesEstadia() { 
				if (document.getElementById('brinquedo').checked || document.getElementById('roupas').checked || document.getElementById('remedios').checked)    
					{ document.getElementById('obscheckbox').disabled = false; } 
				else 
					{ document.getElementById('obscheckbox').disabled = true; } } 