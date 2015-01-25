		var pos;
		var map;
		var geocoder;
		var markers = [];
		var startPosition;
		var currentPosition;
		var endPosition;
		var directionsService = new google.maps.DirectionsService();
function initialize() {
 geocoder = new google.maps.Geocoder();
  var mapOptions = {
    zoom: 14,
  }
  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  // Try HTML5 geolocation
  if(navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      pos = new google.maps.LatLng(position.coords.latitude,
                                       position.coords.longitude);
	var latitude = document.getElementById('latitude')
	latitude.innerHTML = 'latitude:' + pos.lat().toFixed(14);
	var longitude = document.getElementById('longitude');
	longitude.innerHTML = 'longitude:' + pos.lng().toFixed(14);
	
	
      var marker = new google.maps.Marker({
        map: map,
        position: pos,
        title: 'You started from here!'
      });

      map.setCenter(pos);
	  
  //Watch the current location
  var currentPositionMarker;
 var updateLocation = function(position)
{
	var latitude = position.coords.latitude;
	var longitude = position.coords.longitude;
	currentPosition = new google.maps.LatLng(latitude,longitude);
	if (currentPositionMarker==null)
	{
		currentPositionMarker = new google.maps.Marker({
		position: currentPosition,
		map:map,
		title: 'Current Location'});
		
	}
	else
	{
		  currentPositionMarker.setPosition(currentPosition);
	}
	document.getElementById('currentPosition').innerHTML = 'latitude: ' + latitude + ' longitude: ' + longitude;
	if (startPosition != null && endPosition != null)
	{
			document.getElementById('currentToStart').innerHTML = google.maps.geometry.spherical.computeDistanceBetween(currentPosition,startPosition)/1000 + ' Km';
			document.getElementById('currentToEnd').innerHTML = google.maps.geometry.spherical.computeDistanceBetween(currentPosition,endPosition)/1000 + ' Km';
	
	}
  }

var watchID = navigator.geolocation.watchPosition(updateLocation);


 
    }, function() {
      handleNoGeolocation(true);
    });
  } else {
    // Browser doesn't support Geolocation
    handleNoGeolocation(false);
  }
  
    directionsDisplay = new google.maps.DirectionsRenderer({ suppressMarkers: true});

  directionsDisplay.setMap(map);
  
  //document.getElementById('latLong').innerHTML= pos;
}

function handleNoGeolocation(errorFlag) {
  if (errorFlag) {
    var content = 'Error: The Geolocation service failed at finding your location.';
  } else {
    var content = 'Error: Your browser doesn\'t support geolocation.';
  }

  var options = {
    map: map,
    position: new google.maps.LatLng(60, 105),
    content: content
  };

  var infowindow = new google.maps.InfoWindow(options);
  map.setCenter(options.position)

}
google.maps.event.addDomListener(window, 'load', initialize);
function displayTheWay() 
{
	var start = document.getElementById('startBox');
	var end = document.getElementById('destinationBox');
	
	var startAddress = start.value;
	var endAddress = end.value;
	
	setMarker(startAddress, 'Start Position.');
	setMarker(endAddress, 'Destination Position.');
  
	displayDirection(startAddress, endAddress);

	startPosition = parseAddress(startAddress);
	endPosition = parseAddress(endAddress);
	document.getElementById('distance').innerHTML = google.maps.geometry.spherical.computeDistanceBetween(startPosition,endPosition)/1000 + ' Km';
	document.getElementById('currentToStart').innerHTML = google.maps.geometry.spherical.computeDistanceBetween(currentPosition,startPosition)/1000 + ' Km';
	document.getElementById('currentToEnd').innerHTML = google.maps.geometry.spherical.computeDistanceBetween(currentPosition,endPosition)/1000 + ' Km';
	
}

function displayDirection(startAddress, endAddress)
{
	var methodOfTravel = document.getElementById('mode').value;
	var request = {
      origin:startAddress,
      destination:endAddress,
      travelMode: methodOfTravel
  };
  
  directionsService.route(request, function(response, status) {
    if (status == google.maps.DirectionsStatus.OK) {
      directionsDisplay.setDirections(response);
    }
  });
	clearMarkers();


}

function parseAddress(address)
{
	var latLng;
    geocoder.geocode( { 'address': address}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
         latLng = results[0].geometry.location.LatLng;
      } else {
        alert("Geocode was not successful for the following reason: " + status);
      }
    });
	return latLng;
 }
function setMarker(address, message)
{
	geocoder.geocode( { 'address': address}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      var marker = new google.maps.Marker({
          map: map,
          position: results[0].geometry.location,
		  title: message,
      });
    } else {
      alert('Geocode was not successful for the following reason: ' + status);
    }
	markers.push(marker);
  });
}

function clearMarkers()
{
	while(markers.length)
	{
		markers.pop().setMap(null);
	}
}

function trackPath()
{
	var startLatitude = document.getElementById('startLocationLatitude').value;
	var startLongitude = document.getElementById('startLocationLongitude').value;
	var endLatitude = document.getElementById('destinationLocationLatitude').value;
	var endLongitude = document.getElementById('destinationLocationLongitude').value;
	
	startPosition = new google.maps.LatLng(startLatitude, startLongitude);
	endPosition = new google.maps.LatLng(endLatitude,endLongitude);
	
	
	


	
	displayDirection(startPosition,endPosition);
		var startMarker = new google.maps.Marker({
	map:map,
	position: startPosition,
	title: 'Start Position'});


	var endMarker = new google.maps.Marker({
	map:map,
	position: endPosition,
	title: 'Destination Position'});
	
	markers.push(startMarker);
	markers.push(endMarker);
	
	document.getElementById('distance').innerHTML = google.maps.geometry.spherical.computeDistanceBetween(startPosition,endPosition)/1000 + ' Km';
	document.getElementById('currentToStart').innerHTML = google.maps.geometry.spherical.computeDistanceBetween(currentPosition,startPosition)/1000 + ' Km';
	document.getElementById('currentToEnd').innerHTML = google.maps.geometry.spherical.computeDistanceBetween(currentPosition,endPosition)/1000 + ' Km';
	
}

