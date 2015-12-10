$(document).ready(function() {
    var chart;
    var data_dict = {}
    var socket = io();

    (function init_chart() {
        chart = c3.generate({
            bindto: '#chart',
            data: {
                columns: []
            },
            axis: {
                y: {
                    label: {
                        text: 'Signal strength (RSSI)',
                        position: 'middle-left'
                    }
                },
                x: {
                    label: 'Timestamp',
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

    socket.on('new_data', function(data) {
        update_data(data);
    });

    function update_data(new_data_point) {
        var signal_strength = new_data_point[0];
        var mac_addr = new_data_point[1];

        if (mac_addr in data_dict) {
            data_dict[mac_addr].push(signal_strength);
        } else {
            data_dict[mac_addr] = [mac_addr, signal_strength];
        }

        var column_data = flatten_points_dict(data_dict);
        chart.load({ columns: column_data });
    }

    function flatten_points_dict(dict) {
        var ret = [];
        for (var key in dict) {
            ret.push(dict[key]);
        }

        return ret;
    }
});