var scroll = new SmoothScroll('a[href*="#"]');
$(document).ready(function () {
    $(".button-collapse").sideNav();
    $('.slider').slider();
});
window.sr = ScrollReveal();
sr.reveal('.navbar-fixed', {
     duration: 500,
     origin: 'top', 
});
sr.reveal('#start', {
    duration: 500,
    delay: 1000,
    origin: 'top', 
});
sr.reveal('#services', {
    duration: 500,
    origin: 'bottom', 
});

