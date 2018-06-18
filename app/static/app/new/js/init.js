(function($){
  $(function(){

    $('.sidenav').sidenav({
      edge: 'left', // Choose the horizontal origin
      closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
      draggable: true // Choose whether you can drag to open on touch screens
    });
    $('.parallax').parallax();

  }); // end of document ready
})(jQuery); // end of jQuery name space
