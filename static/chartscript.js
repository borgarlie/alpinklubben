/**
 * Created by Borgar on 22.04.2016.
 */

var ctx = document.getElementById("userchart").getContext("2d");
var ctx2 = document.getElementById("saleschart").getContext("2d");

$.ajax({
    type: "GET",
    url: '/api/user-chart-data',
    dataType: 'json',
    success: function (data) {
        var item = data.item;
        var dataset = {
            labels: ["0-20", "21-30", "31-40", "41+"],
            datasets: [
                {
                    label: "Medlemmer - aldersgrupper",
                    fillColor: "rgba(220,220,220,0.5)",
                    strokeColor: "rgba(220,220,220,0.8)",
                    highlightFill: "rgba(220,220,220,0.75)",
                    highlightStroke: "rgba(220,220,220,1)",
                    data: [item.first, item.second, item.third, item.forth]
                }
            ]
        };
        var BarChartUsers = Chart.Bar(ctx, {
            data: dataset,
            options: {}
        });
    }
});

$.ajax({
    type: "GET",
    url: '/api/sales-chart-data',
    dataType: 'json',
    success: function (data) {
        var item = data.item;
        var dataset2 = {
            labels: ["Dagskort", "Ukeskort", "Sesongkort"],
            datasets: [
                {
                    label: "Salg av heiskort",
                    fillColor: "rgba(220,220,220,0.5)",
                    strokeColor: "rgba(220,220,220,0.8)",
                    highlightFill: "rgba(220,220,220,0.75)",
                    highlightStroke: "rgba(220,220,220,1)",
                    data: [item.first, item.second, item.third]
                }
            ]
        };

        var BarChartSales = Chart.Bar(ctx2, {
            data: dataset2,
            options: {}
        });
    }
});
