function getIndsAndRate() {
    JQuery.ajax({
        type: "POST",
        url: "/get_data_for_diag",
        success: function(response) {
            var data = response;
            console.log(data);
            return data;
        },
        error: function(error) {
            console.log(error);
        }
     });

}

//var marksCanvas = document.getElementById("testdiag");
//var radarChart = new Chart(marksCanvas, {
//    type: 'line',
//    data: {
//        labels: labels,
//        datasets: [{
//            label: 'This week',
//            data: Object.values(data)
//        }]
//    });
//}
function build_chart_by_query(data , arr_indicators , arr_value) {
    var diag;
    var marksCanvas = document.getElementById("testdiag");
    diag = new Chart(marksCanvas, {
        type: 'pie',
        data: {
            labels: arr_indicators,
            backgroundColor: "red",
            datasets: [
                {
                    label: "рейтинг по критериям",
                    fillColor: "rgb(220,220,220)",
                    data: arr_value,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.4)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 0.6)',
                        'rgba(255, 99, 132, 0.6)',
                        'rgba(54, 162, 235, 0.6)',
                        'rgba(255, 206, 86, 0.6)',
                        'rgba(75, 192, 192, 0.6)',
                        'rgba(153, 102, 255, 0.6)'
                    ]
                }
            ]
        }
    });
}
// TODO: Write diagram builder




function load_diagrams() {
    jQuery.ajax({
        type: 'POST',
        url:  '/load_diagrams',
        dataType: 'json',
        success: function(response){
          // JSON.parse(response.toString().replace(/[']/g,'"'));
//            JSON.parse(response , function( k , v) {
//                console.log(k);
//                return v
//            });


//        true code)    JSON.parse("[{'val': 15.0, 'ind': 'Наличие категории'}, {'val': 15.0, 'ind': 'Наличие категории'}, {'val': 15.0, 'ind': 'Наличие категории'}, {'val': 15.0, 'ind': 'Наличие категории'}, {'val': 15.0, 'ind': 'Наличие категории'}]".replace(/[']/g,'"'));

            // JSON.parse("[{'val': 15.0, 'ind': 'Наличие категории'}, {'val': 15.0, 'ind': 'Наличие категории'}, {'val': 15.0, 'ind': 'Наличие категории'}, {'val': 15.0, 'ind': 'Наличие категории'}, {'val': 15.0, 'ind': 'Наличие категории'}]".replace(/[']/g,'"'));
            // console.log(JSON.parse(response.toString().replace(/[']/g,'"')));
            // console.log(response);
            var arr_indicators = [];
            var arr_value = [];
            for (var i = 0; i < response.length; i++) {
                arr_indicators[i] = response[i][0];
                arr_value[i] = response[i][1];
            }
            console.log(arr_indicators);
            console.log(arr_value);
//            makeDiagram(response);
            build_chart_by_query(response , arr_indicators , arr_value)
        }
    });
}

function makeDiagram(data) {
    var marksCanvas = document.getElementById("testdiag");

}