var map,
    currentPositionMarker,
    mapCenter = new google.maps.LatLng(40.700683, -73.925972),
    map;

function initializeMap()
{
    map = new google.maps.Map(document.getElementById('mapa'), {
       zoom: 17,
       center: mapCenter,
       mapTypeId: google.maps.MapTypeId.ROADMAP
     });
}

function locError(error) {
    alert("La posición actual no se ha encontrado :(");
}

function setCurrentPosition(pos) {
    mapCenter = new google.maps.LatLng(pos.coords.latitude, pos.coords.longitude);
    currentPositionMarker = new google.maps.Marker({
        map: map,
        position: new google.maps.LatLng(
            pos.coords.latitude,
            pos.coords.longitude
        ),
        title: "Posición actual"
    });
    map.panTo(new google.maps.LatLng(pos.coords.latitude,pos.coords.longitude));

    
}
function displayAndWatch(position) {
    // establecer la posición actual
    setCurrentPosition(position);
    // obervamos la posición
    watchCurrentPosition();
    var text = "position.coords.latitude: "  + position.coords.latitude  + "<br/>" +
               "position.coords.longitude: " + position.coords.longitude + "<br/>" +
               "position.coords.altitude: " + position.coords.altitude + "<br/>" +
               "position.coords.accuracy(meters): "  + position.coords.accuracy  + "<br/>" +
               "position.coords.altitudeAccuracy(meters): "  + position.coords.altitudeAccuracy  + "<br/>" +
               "position.coords.heading: "  + position.coords.heading  + "<br/>" +
               "position.coords.speed: "  + position.coords.speed  + "<br/>" +
               "position.timestamp: " + new Date(position.timestamp);
    jQuery("#APIReturnValues").html(text);
}

function watchCurrentPosition() {
    var positionTimer = navigator.geolocation.watchPosition(
        function (position) {
            setMarkerPosition(
                currentPositionMarker,
                position
            );
        });
}

function setMarkerPosition(marker, position) {
    marker.setPosition(
        new google.maps.LatLng(
            position.coords.latitude,
            position.coords.longitude)
    );
}

function initLocationProcedure() {
    initializeMap();
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(displayAndWatch, locError);
    } else {
        alert("Su navegador no es compatible con la API de Geolocalización :(");
    }
}

$(document).ready(function() {
    initLocationProcedure();
    $(".center-marker").click(initializeMap);
});