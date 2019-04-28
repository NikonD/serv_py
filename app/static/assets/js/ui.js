window.onload = function() {
	
	const ITEM_HAMBURGER = document.getElementsByClassName('hamburger')[0];
	const ITEM_USER_AREA = document.getElementsByClassName('user')[0];
	const ITEM_DROP_MENU = document.getElementsByClassName('dropdown_content')[0];
	
	var drop_menu = "off"; // dropdown menu must be hidden by default
	
	function hamburger_hover(color) {
		var x = document.getElementsByClassName('ham');
		for (var i=0; i<x.length; i++) {
		  x[i].style.backgroundColor = color;
		}
	}
	
	// Hamburger hover effect
	ITEM_HAMBURGER.onmouseover = function() {
		hamburger_hover('#ddc46c');
	};
	ITEM_HAMBURGER.onmouseout = function() {
		hamburger_hover('#ccc');
	};
	
	// Dropdown menu trigger
	ITEM_USER_AREA.onclick = function() {
		if(drop_menu != "on") {
		    ITEM_DROP_MENU.style.opacity = "1";
			drop_menu = "on"; // dropdown enabled
		} else if (drop_menu == "on") {
			ITEM_DROP_MENU.style.opacity = "0";
			drop_menu = "off"; // dropdown disabled
		}
	};
	
};
