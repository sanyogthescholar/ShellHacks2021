var mymap = L.map('mapid').setView([51.505, -0.09], 13);
L.tileLayer('https://{s}.tile.openstreetmap.de/tiles/osmde/{z}/{x}/{y}.png', {
	maxZoom: 18,
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);
console.log("map.js succesfully executed");
var marker = L.marker([51.5, -0.09]).addTo(mymap);
var temperature = $('#temperature')[0].attributes[1].nodeValue;
var humidity = $('#humidity')[0].attributes[1].nodeValue;
console.log(temperature);
console.log(humidity);
marker.bindPopup("Temperature is "+ parseFloat(temperature).toFixed(2) +"° C and humidity is "+ parseFloat(humidity).toFixed(2) + "%").openPopup();