
var xData = [];
var yData = [];
                    

$(function() {
        $(".filter").click(function() {
            $.ajax({
                url: "/get_chart_data",
                data: $("form").serialize(),
                type: "POST",
                dataType: "html",
                success: function(response) {
                    console.log(response);
                    var results = JSON.parse(response);

                    $.each(results, function(name, value) {
                        yData.push(Number(value));
                        xData.push(name);
                    });
                    $("#container").highcharts({
                        chart: {
                            type: "column"
                        },
                        title: {
                            text: "SPAM in the cities"
                        },
                        xAxis: {
                            categories: xData
                        },
                        yAxis: {
                            title: {
                                text: "Quantity"
                            }
                        },
                        series: [{
                            name: "SPAM",
                            data: yData
                        }, ],
                    });
                },
                error: function(error) {
                    console.log(error);
                }
            });
        });
    });
