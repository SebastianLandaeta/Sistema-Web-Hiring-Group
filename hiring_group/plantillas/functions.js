// Obtener el botón
var mybutton = document.getElementById("back-to-top");

// Mostrar el botón cuando el usuario se desplaza hacia abajo 20px desde el principio de la página
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

// Al hacer clic en el botón, volver al principio de la página
function topFunction() {
    document.body.scrollTop = 0; // Para Safari
    document.documentElement.scrollTop = 0; // Para Chrome, Firefox, IE y Opera
}