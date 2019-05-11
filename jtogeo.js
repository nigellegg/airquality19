var map = L.map('map',{
}).setView([43.526523590087891, -5.6150951385498047], 12);

L.tileLayer('http://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}.{ext}', {
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    subdomains: 'abcd',
    ext: 'png'
}).addTo(map);

var data = [{
"latitud": 43.526523590087891,
"longitud": -5.6150951385498047
}, {
"latitud": 43.511680603027344,
"longitud": -5.6671133041381836
},
{
"latitud": 43.526451110839844,
"longitud": -5.6140098571777344
}]

var jsonFeatures = [];

data.forEach(function(point){
    var lat = point.latitud;
    var lon = point.longitud;

    var feature = {type: 'Feature',
        properties: point,
        geometry: {
            type: 'Point',
            coordinates: [lon,lat]
        }
    };

    jsonFeatures.push(feature);
});

var geoJson = { type: 'FeatureCollection', features: jsonFeatures };

L.geoJson(geoJson).addTo(map);

