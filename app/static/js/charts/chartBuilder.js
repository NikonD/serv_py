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
        radius: 10,
        pointRadius: 10,
        pointBorderWidth: 3,
        pointBackgroundColor: "red",
        pointBorderColor: "rgba(200,0,0,0.6)",
        pointHoverRadius: 20,
        data: [65, 75, 70, 80, 60, 80]
    }, {
        label: "Student B",
        backgroundColor: "transparent",
        borderColor: "rgba(0,0,200,0.6)",
        fill: false,
        radius: 6,
        pointRadius: 6,
        pointBorderWidth: 3,
        pointBackgroundColor: "cornflowerblue",
        pointBorderColor: "rgba(0,0,200,0.6)",
        pointHoverRadius: 10,
        data: [54, 65, 60, 70, 70, 75]
    }]
    };

    var chartOptions = {
    scale: {
        gridLines: {
        color: "black",
        lineWidth: 3
        },
        angleLines: {
        display: false
        },
        ticks: {
        beginAtZero: true,
        min: 0,
        max: 100,
        stepSize: 20
        },
        pointLabels: {
        fontSize: 18,
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
