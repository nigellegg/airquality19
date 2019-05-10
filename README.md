# airquality19
Dynamic map of Bristol Airquality

Using the data and APIs on the Bristol Open Data website, it is theoretically possible to gather data regarding NO and NOx concentrations from a number of sites across the city every 15 minutes.  
I intend to collect this data and display it in a dynamic Leaflet.js map, for community use. 
This will be a Serverless web app, running on Amazon Web Services: 
- a Lambda function calls the api, parses the json and saves it to S3.  
- this function is triggered by a CloudWatch Schedule - TODO. 
- index.html is the single page static site, using javascript to convert the json to geojson, and leaflet.js to display the data on the map - TO FIX


    
