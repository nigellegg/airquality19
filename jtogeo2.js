var geojson = {
  type: "FeatureCollection",
  features: [],
};

for (i = 0; i < json.stationBeanList.length; i++) {
  if (window.CP.shouldStopExecution(1)) {
    break;
  }
  geojson.features.push({
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [json.stationBeanList[i].longitude, json.stationBeanList[i].latitude]
    },
    "properties": {
      "id": json.stationBeanList[i].id,
      "stationName": json.stationBeanList[i].stationName,
      "totalDocks": json.stationBeanList[i].totalDocks,
      "station": json.stationBeanList[i].stationName,
      "stAddress1": json.stationBeanList[i].stAddress1,
      "stAddress2": json.stationBeanList[i].stAddress2,
      "city": json.stationBeanList[i].city,
      "postalCode": json.stationBeanList[i].postalCode,
      "testStation": json.stationBeanList[i].testStation
    }
  });
}

window.CP.exitedLoop(1);

document.getElementById('json').innerHTML = JSON.stringify(json, null, 2);
document.getElementById('geojson').innerHTML = JSON.stringify(geojson, null, 2);

var geojson = {
  type: "FeatureCollection", 
  features: [],
};

for (i = 0; i < json.length; i++) {
  if (window.CP.shouldStopExecution(1)) {
    break;
  }
  geojson.features.push({
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [json[i].longitude, json[i].latitude]
    }, 
    "properties": {
      "id": json[i].recordid,
      "time": json[i].time,
      "no": json[i].no,
      "nox": json[i].nox,
      "no2": json[i].no2
    }
  });
}