
  $(document).ready(function() {

    $('#calendar').fullCalendar({

     theme: true,    
      themeSystem:'bootstrap4',

      header: {
        left: 'prev,next today',
        center: 'title',
        right: 'month,agendaWeek,agendaDay,listWeek'
      },
      defaultDate: Date() ,
	  locale:'pt-br',
      navLinks: true, //Permite navegar entre o dia e a semana.
      editable: true,
      eventLimit: true, // allow "more" link when too many events
	selectable : true,	  
	  	  
	   eventClick: function(events) {
	   $('#visualizar #Nome').text(events.title);
	   $('#visualizar #NomeAnimal').val(events.title);
	   $('#visualizar #DataInicio').text(events.start.format('DD/MM/YYYY HH:mm:ss'));
	   
	   $('#visualizar #datahora').val(events.start.format('DD/MM/YYYY HH:mm:ss'));
       $('#visualizar').modal('show');
	   return false;
	//	alert('Event: ' + calEvent.title);
	//	alert('Coordinates: ' + jsEvent.pageX + ',' + jsEvent.pageY);
	//	alert('View: ' + view.name);

				// change the border color just for fun
	//		$(this).css('border-color', 'red');
	
     
	  },
	    selectHelper: true,
	  	  select:function(start,end){
	  $('#cadastrar #start').val(moment(start).format('DD/MM/YYYY HH:mm:ss'));
	  $('#cadastrar #end').val(moment(end).format('DD/MM/YYYY HH:mm:ss'));
	  $('#cadastrar').modal('show');
	  },
	  
      events: [
        {
          title: 'Floquinho',
          start: '2018-05-01',
	
        },
        {
          title: 'scooby',
          start: '2018-05-07',
          end: '2018-05-07'
        },
        {
          id: 999,
          title: 'Urso',
          start: '2018-05-09T16:00:00'
        },
        {
          id: 999,
          title: 'Usinho',
          start: '2018-05-16T16:00:00'
        },
        {
          title: 'VOLIBEAR',
          start: '2018-05-11',
          end: '2018-05-11'
        },
        {
          title: 'KAKA',
          start: '2018-05-12T10:30:00',
          end: '2018-05-12T12:30:00'
        },
        {
          title: 'LULU',
          start: '2018-03-12T12:00:00'
        },
        {
          title: 'TRAVESSO',
          start: '2018-05-12T14:30:00'
        },
        {
          title: 'Pretinho',
          start: '2018-09-12T17:30:00'
        },
         {
          title: 'Pretinho',
          start: '2018-09-12T17:30:00'
        },
         {
          title: 'Pretinho',
          start: '2018-09-12T17:30:00'
        },
         {
          title: 'Pretinho',
          start: '2018-09-12T17:30:00'
        },
         {
          title: 'Pretinho',
          start: '2018-09-12T17:30:00'
        },
        {
          title: 'lala',
          start: '2018-09-12T20:00:00'
        },
        {
          title: 'Lucas',
          start: '2018-05-13T07:00:00'
        },
        {
          title: 'Lucas siqueira',
          url: 'http://google.com/',
          start: '2018-09-28'
        }
      ]
    });

  });