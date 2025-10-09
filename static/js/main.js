const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", () => {
    // Ajoute/retire la classe "active" sur l'icône
    hamburger.classList.toggle("active");
    // Ajoute/retire la classe "active" sur le menu
    navMenu.classList.toggle("active");
});
