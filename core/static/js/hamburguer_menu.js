var checkbox = document.getElementById('navicon');
var menuLateral = document.getElementById('menuLateral');
function menuSlide() {
	if (checkbox.checked == true) {
		menuLateral.style.marginLeft = "-299px";
	}
	if (checkbox.checked == false) {
		menuLateral.style.marginLeft = "0px";
	}
}