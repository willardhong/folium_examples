// static/js/script.js
var API_URL = 'http://localhost:5000/api';

var displayJSON = function() {

    d3.json(API_URL, function(error, data) {

        // log any error to the console as a warning
        if(error){
            return console.warn(error);
        }

        d3.select('#query pre').html("test"); 1
        d3.select('#data pre').html(JSON.stringify(data, null, 4));
        console.log(data);
    });
};

displayJSON();