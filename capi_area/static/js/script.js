window.addEventListener("resize", function() {
    const cartaBox = document.querySelector(".cartaBox");
    if (window.innerWidth >= 500) {
      cartaBox.style.display = "grid";
      cartaBox.style.flexWrap = "wrap";
    } else {
      cartaBox.style.display = "wrap";
      cartaBox.style.flexWrap = "";
    }
});
