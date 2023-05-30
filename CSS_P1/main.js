// panier
let cartIcon = document.querySelector("#cart-icon")
let cart = document.querySelector(".cart")
let closeCart = document.querySelector("#close-cart")

// ouverir panier
cartIcon.onclick = () => {
	cart.classList.add("active");
};
// fermer panier
closeCart.onclick = () => {
	cart.classList.remove("active");
};