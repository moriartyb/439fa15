$(document).ready(function() {
    var chart;
    var data_points = ['RSSI'];
    var index_counter = 1;

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

    function update_chart() {
        var latest_index = index_counter;
        var data_request = $.ajax({ url: '/point' });
        data_request.done(function(response) {
            update_data(response['data'], latest_index);
        });
        index_counter += 1;
    }

    function update_data(new_data_point, target_index) {
        var length_diff = target_index - data_points.length;
        data_points.extend(length_diff);
        data_points[target_index] = new_data_point;
        chart.load({ columns: [data_points] });
    }

    setInterval(function() {
        update_chart();
    }, 1000);
});

Array.prototype.extend = function(extend_amount) {
    if (extend_amount < 0)
        return;

    var old_length = this.length;
    var new_length = old_length + extend_amount;

    this.length = new_length;
    for (var i = old_length; i < new_length; i++) {
        this[i] = 0;
    }
}