import couchdb

SERVER = "http://admin:admin@localhost:5984"
server = couchdb.Server(SERVER)

hist = server["historic_melb"]

map_sa3_polarity = """
function (doc) {
    emit([doc.sa3], doc.polarity_score);
}
"""

reduce_sum_count = """
function (keys, values, rereduce) {
    var results = {};
    if (rereduce) {
        for (var i = 0; i < values.length; i++) {
            for (var key in values[i]) {
                if (key in results) {
                    results[key]["sum"] += values[i][key]["sum"];
                    results[key]["count"] += values[i][key]["count"];
                } else {
                    results[key] = values[i][key];
                }
            }
        }
    }
    else {
        for (var j = 0; j < values.length; j++) {
            if (keys[j] in results) {
                results[keys[j]]["sum"] += values[j];
                results[keys[j]]["count"] += 1;
            } else {
                results[keys[j]] = {"sum": values[j], "count": 1};
            }
        }
    }
}
"""

mean_sa3_polarity = couchdb.design.ViewDefinition(
    "geo", "mean_sa3_polarity", map_sa3_polarity, reduce_sum_count
)
mean_sa3_polarity.sync(hist)
