var mymap = L.map('mapid').setView([51.505, -0.09], 13);
L.tileLayer('https://{s}.tile.openstreetmap.de/tiles/osmde/{z}/{x}/{y}.png', {
	maxZoom: 18,
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);
console.log("map.js succesfully executed");
var marker = L.marker([51.5, -0.09]).addTo(mymap);
var temperature = $('#temperature').data();
var humidity = $('#humidity').data();
console.log(temperature);
console.log(humidity);
marker.bindPopup("Temperature is "+ temperature +" and humidity is "+ humidity).openPopup();