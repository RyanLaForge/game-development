		var pos  //The starting position when the website as accessed.
		var map;	//The google map
		var geocoder;	//The google geocoder
		var markers = [];	//An array of markers to keep track of the markers currently on the scren.
		var startPosition;	//The start position for the entered values.
		var currentPosition;	//The current position of the user.
		var endPosition;	//The end position of the user.
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
	latitude.innerHTML = 'Latitude:' + pos.lat().toFixed(14);
	var longitude = document.getElementById('longitude');
	longitude.innerHTML = 'Longitude:' + pos.lng().toFixed(14);
	
	
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

	var latitude = position.coords.latitude.toFixed(14);
	var longitude = position.coords.longitude.toFixed(14);
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
	document.getElementById('currentLatitude').innerHTML = 'Latitude: ' + latitude 
	document.getElementById('currentLongitude').innerHTML ='Longitude: ' + longitude;
	updateCoords();
  }

  var oldLocation = 0;
  function currentPositionHasChanged()
  {
	  if (oldLocation != currentPosition)
	  {
		  oldLocation = currentPosition;
		  return true;
	  }
	  return false;
  }
var watchID = navigator.geolocation.watchPosition(updateLocation);


 
    }, handleError)}
 else {
    // Browser doesn't support Geolocation
    handleNoGeolocation(false);
  }
  
    directionsDisplay = new google.maps.DirectionsRenderer({ suppressMarkers: true});

  directionsDisplay.setMap(map);
  
}

function handleError()
{
	switch(error.code) {
        case error.PERMISSION_DENIED:
            alert("Geolocation failed. User denied the request for Geolocation.");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("Location information is unavailable.");
            break;
        case error.TIMEOUT:
            alert("The request to get user location timed out.");
            break;
        case error.UNKNOWN_ERROR:
			alert("An unknown error occurred.");
            break;
    }
}


/* Handles any error associated with geocoding.*/
function handleNoGeolocation(errorFlag) {
  if (errorFlag) {
    var content = 'Error: The Geolocation service failed at finding your location. For the following reason' + errorFlag.value;
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

/* Displays the direction from the entered start address to the destination address.*/
function displayTheWay() 
{
	var start = document.getElementById('startBox');
	var end = document.getElementById('destinationBox');
	
	var startAddress = start.value;
	var endAddress = end.value;
	
	clearMarkers();
	setMarker(startAddress, 'Start Position.');
	setMarker(endAddress, 'Destination Position.');
  
	displayDirection(startAddress, endAddress);

	parseAddress(startAddress,0);
	parseAddress(endAddress,1);
	

	
}

/*Puts the direction on the map*/
function displayDirection(startAddress, endAddress)
{
	var methodOfTravel = document.getElementById('mode').value;
	var request = {
      origin:startAddress,
      destination:endAddress,
      travelMode: methodOfTravel,
	  waypoints:[
    {
      location:currentPosition,
      stopover:true
    }]
  };
  
	
  directionsService.route(request, function(response, status) {
    if (status == google.maps.DirectionsStatus.OK) {
      directionsDisplay.setDirections(response);
    }
  });


}

/**Parses the address to obtain a LatLng*/
function parseAddress(address, number)
{
    geocoder.geocode( { 'address': address}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
		  if (number == 0)
		  {
			  startPosition = results[0].geometry.location;
		  }
		  else if (number == 1)
		  {
			   endPosition = results[0].geometry.location;
		  }
      } else {
        alert("Geocode was not successful for the following reason: " + status);
      }
    });

 }
 
 /*update the coordinates of the starting position, current position, and end position.*/
 function updateCoords()
 {
	if (currentPosition != null)
	{
		document.getElementById('currentLatitude').innerHTML = 'Latitude:' + currentPosition.lat().toFixed(14);
		document.getElementById('currentLongitude').innerHTML = 'Longitude:' + currentPosition.lng().toFixed(14);
		}
	  if (startPosition != null && currentPosition != null)
		 {
				document.getElementById('currentToStart').innerHTML = (google.maps.geometry.spherical.computeDistanceBetween(currentPosition,startPosition)/1000).toFixed(2) + ' Km';

		 }
		 
		if(endPosition != null && currentPosition != null)
		 {
			 		document.getElementById('currentToEnd').innerHTML = (google.maps.geometry.spherical.computeDistanceBetween(currentPosition,endPosition)/1000).toFixed(2) + ' Km';
		 }
		 if (startPosition != null && endPosition != null)
		 {
			 document.getElementById('distance').innerHTML = (google.maps.geometry.spherical.computeDistanceBetween(startPosition,endPosition)/1000).toFixed(2) + ' Km';
		 }
 }
 
 /*Sets a marker on the map with the given address and message */
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

/* Clears all markers from the map.*/
function clearMarkers()
{
	while(markers.length)
	{
		markers.pop().setMap(null);
	}
}

/*Uses the coordinates to set down markers for the path.*/
function trackPath()
{
	var startLatitude = document.getElementById('startLocationLatitude').value;
	var startLongitude = document.getElementById('startLocationLongitude').value;
	var endLatitude = document.getElementById('destinationLocationLatitude').value;
	var endLongitude = document.getElementById('destinationLocationLongitude').value;
	
	startPosition = new google.maps.LatLng(startLatitude, startLongitude);
	endPosition = new google.maps.LatLng(endLatitude,endLongitude);
	
	
	


	
	displayDirection(startPosition,endPosition);
	clearMarkers();
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
	
	updateCoords();
}

