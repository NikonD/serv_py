

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
function build_chart_by_query(data) {
    var diag;
    var marksCanvas = document.getElementById("testdiag");
    diag = new Chart(marksCanvas, {
        type: 'pie',
        data: {
            labels: Object.keys(data),
            backgroundColor: "red",
            datasets: [
                {
                    label: Object.keys(data),
                    fillColor: "rgb(220,220,220)",
                    data: Object.keys(data).map(function(key) {
                        return data[key];
                    }),
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
//           JSON.parse(response , function() {
//               console.log(response);
////               return v;
//           });
//            JSON.parse(response , function( k , v) {
//                console.log(k);
//                return v
//            });

//        true code)    JSON.parse("[{'val': 15.0, 'ind': 'Наличие категории'}, {'val': 15.0, 'ind': 'Наличие категории'}, {'val': 15.0, 'ind': 'Наличие категории'}, {'val': 15.0, 'ind': 'Наличие категории'}, {'val': 15.0, 'ind': 'Наличие категории'}]".replace(/[']/g,'"'));
            console.log(Object.keys(response[0]));
//            makeDiagram(response);
            build_chart_by_query(response)
        }
    });
}

function makeDiagram(data) {
    var marksCanvas = document.getElementById("testdiag");

}