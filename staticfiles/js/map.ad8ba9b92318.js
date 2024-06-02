function initMap() {
    var mapCenter = {lat: 53.2828, lng: -4.3100};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: mapCenter
    });

    var locations = [
        {lat: 53.333, lng: -4.477, title: 'Llyn Alaw'},
        {lat: 53.389, lng: -4.343, title: 'Parys Mountain'},
        {lat: 53.257, lng: -4.309, title: 'The Dingle'},
        {lat: 53.210, lng: -4.230, title: 'Moel-y-don'},
        {lat: 53.320, lng: -4.227, title: 'Benllech'},
        {lat: 53.407, lng: -4.580, title: 'Hen Borth'},
        {lat: 53.416, lng: -4.346, title: 'Point Lynas'},
        {lat: 53.390, lng: -4.480, title: 'Traeth Penial'},
        {lat: 53.306, lng: -4.700, title: 'South Stack'},
        {lat: 53.275, lng: -4.624, title: 'Trearddur Bay'},
        {lat: 53.236, lng: -4.520, title: 'Rhosneiger'},
        {lat: 53.283, lng: -4.343, title: 'Maltreath'},
        {lat: 53.304, lng: -4.217, title: 'Red Wharf Bay'},
        {lat: 53.146, lng: -4.361, title: 'Newborough Forest'},
        {lat: 53.263, lng: -4.090, title: 'Beaumaris'},
        {lat: 53.203, lng: -4.484, title: 'Aberffraw'}, 
        {lat: 53.373, lng: -4.267, title: 'Ligwy Beach'},
        {lat: 53.297, lng: -4.073, title: 'Llanddona'},
        {lat: 53.223, lng: -4.543, title: 'Church in the Sea'} 
    ];

    locations.forEach(function(location) {
        new google.maps.Marker({
            position: {lat: location.lat, lng: location.lng},
            map: map,
            title: location.title
        });
    });
}

window.onload = initMap;