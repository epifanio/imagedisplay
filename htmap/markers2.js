var cities2 = new L.LayerGroup();

L.marker([49.61, -105.02]).bindPopup('This is Littleton, CO.').addTo(cities2),
L.marker([49.74, -104.99]).bindPopup('This is Denver, CO.').addTo(cities2),
L.marker([49.73, -104.8]).bindPopup('This is Aurora, CO.').addTo(cities2),
L.marker([49.77, -105.23]).bindPopup('This is Golden, CO.').addTo(cities2);
	
	
var overlays2 = {
	"Cities2": cities2
};

L.control.layers(overlays2).addTo(map);