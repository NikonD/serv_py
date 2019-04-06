
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

function build_chart_by_query() {
    var marksCanvas = document.getElementById("marksChart");

    Chart.defaults.global.defaultFontFamily = "Lato";
    Chart.defaults.global.defaultFontSize = 18;

    var marksData = {
    labels: ["English", "Maths", "Physics", "Chemistry", "Biology", "History"],
    datasets: [{
        label: "Student A",
        backgroundColor: "rgba(200,200,0,0.2)",
        borderColor: "rgba(200,200,0,0.6)",
        fill: true,
        radius: 3,
        pointRadius: 2,
        pointBorderWidth: 3,
        pointBackgroundColor: "red",
        pointBorderColor: "rgba(200,0,0,0.6)",
        pointHoverRadius: 4,
        data: [65, 75, 70, 80, 60, 80]
    }, {
        label: "Student B",
        backgroundColor: "transparent",
        borderColor: "rgba(0,0,200,0.6)",
        fill: false,
        radius: 3,
        pointRadius: 2,
        pointBorderWidth: 3,
        pointBackgroundColor: "cornflowerblue",
        pointBorderColor: "rgba(0,0,200,0.6)",
        pointHoverRadius: 4,
        data: [54, 65, 60, 70, 70, 75]
    }]
    };

    var chartOptions = {
    scale: {
        gridLines: {
        color: "black",
        lineWidth: 2
        },
        angleLines: {
        display: false
        },
        ticks: {
        beginAtZero: true,
        min: 0,
        max: 100,
        stepSize: 50,
        fontColor: "#89FF66",
        // backdropColor: "rgba(109,109,108,0,4)"
        },
        pointLabels: {
        fontSize: 9,
        fontColor: "green"
        }
    },
    legend: {
        position: 'left'
    }
    };

    var radarChart = new Chart(marksCanvas, {
        type: 'radar',
        data: marksData,
        options: chartOptions
    });    
}
