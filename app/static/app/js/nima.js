// var scroll = new SmoothScroll('a[href*="#"]');
// $(document).ready(function () {
//     $(".button-collapse").sideNav();
//     $('.slider').slider();
// });


window.sr = ScrollReveal();
sr.reveal('#start', {
     duration: 400,
     origin: 'top', 
});
sr.reveal('.callsupport', {
    duration: 500,
    delay: 500,
    // origin: 'buttom',
    easing: 'cubic-bezier(0.6, 0.2, 0.1, 1)',
});
sr.reveal('.text--inblue', {
    duration: 500,
    origin: 'right',
    viewFactor: 0.5,
});

