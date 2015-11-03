$(document).ready(function() {
    var chart;
    var data_points = ['RSSI', 0];

    (function init_chart() {
        chart = c3.generate({
            bindto: '#chart',
            data: {
                columns: [
                    data_points,
                ]
            },
            axis: {
                y: {
                    label: {
                        text: 'Signal strength',
                        position: 'middle-left'
                    }
                },
                x: {
                    label: 'Time in seconds',
                    tick: {
                        format: function(x) {
                            return Math.floor(x * 100) / 100;
                        },
                        count: 10
                    }
                }
            }
        });
    })();


    function update_chart(new_data_point) {
        data_points.push(new_data_point);
        chart.load({
            columns: [
                data_points
            ]
        });
    }

    setInterval(function() {
        var new_value = parseInt(Math.random() * 50);
        update_chart(new_value);
    }, 1000);
});
