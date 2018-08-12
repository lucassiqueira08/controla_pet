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

//=====================Calendário=======================

$( function() {
  $( "#Data" ).datepicker();
} );

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



function habilitaCampos(){
	document.getElementsByClassName("input.formInput").prop('disabled', false);
}