// Initialize and add the map
window.initMap = initMap;
function initMap() {
	const unimelb = { lat: -37.797702, lng: 144.961029 };
	const map = new google.maps.Map(document.getElementById('map'), {
		zoom: 8,
		center: unimelb,
	});
	window.map = map; //temp
	map.data.loadGeoJson(geoJSON);
	map.data.setStyle(function (feature) {
		return {
			fillColor: 'blue',
			strokeWeight: 1
		}
	});
	map.data.addListener('mouseover', function (event) {
		setText(getName(event.feature));
	});
}

function getName(feature) {
	return feature.j.name;
}

function setText(text) {
	document.getElementById('textField').innerHTML = text;
}
