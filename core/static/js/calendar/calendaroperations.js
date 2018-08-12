$(function() {

  $('#calendar').fullCalendar({

    header: {
      left: 'prev,next today',
      center: 'title',
      right: 'month,listYear'
    },

    displayEventTime: false, // don't show the time column in list view

    // THIS KEY WON'T WORK IN PRODUCTION!!!
    // To make your own Google API key, follow the directions here:
    // http://fullcalendar.io/docs/google_calendar/
    googleCalendarApiKey: 'AIzaSyBIF-wWrAJvGoLIXuAVQ0sVJCpaHJ4Pkjk',

    // US Holidays
    events: 'controlapet@gmail.com',

    eventClick: function(event) {
      // opens events in a popup window
      window.open(event.url, '_blank', 'width=700,height=600');
      return false;
    }

  });

});
