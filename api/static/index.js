$(document).ready(function() {
    var rssi_chart;
    var distance_chart;

    var data_dict = {}
    var socket = io();

    (function init_rssi_chart() {
        rssi_chart = c3.generate({
            bindto: '#rssi_chart',
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

    (function init_distance_chart() {
        distance_chart = c3.generate({
            bindto: '#distance_chart',
            data: {
                columns: []
            },
            axis: {
                y: {
                    label: {
                        text: 'Estimated distance (m)',
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
        })
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

        var column_rssi_data = flatten_points_dict(data_dict);
        rssi_chart.load({ columns: column_rssi_data });

        var distance_dict = generate_range_data(data_dict);
        var column_distance_data = flatten_points_dict(distance_dict);
        distance_chart.load({columns: column_distance_data});
    }

    function generate_range_data(rssi_dict) {
        var ret = {}
        for (var key in rssi_dict) {
            var rssi_data = rssi_dict[key];
            var mac_addr = rssi_data[0];
            var rssi_vals = rssi_data.splice(1);

            ret[mac_addr] = [mac_addr];

            for (var i in rssi_vals.length) {
                ret[mac_addr].push(compute_range(rssi_vals[i]));
            }
        }

        return ret;
    }

    function flatten_points_dict(dict) {
        var ret = [];
        for (var key in dict) {
            ret.push(dict[key]);
        }

        return ret;
    }

    function compute_range(rssi_value) {
        var A = parseFloat($('#one_meter').value())
        var n = parseFloat($('#n_value').value())

        var div = -((rssi_value - A) / (10 * n));
        var d = Math.pow(10, div);

        return d;
    }
});