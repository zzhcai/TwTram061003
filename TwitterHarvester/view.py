import couchdb
from couchdb import design

SERVER = "http://admin:admin@localhost:5984"
server = couchdb.Server(SERVER)

hist = server["historic_melb"]

map_sa3_polarity = """
function (doc) {
    emit([doc.sa4, doc.sa3, doc.sa2], doc.polarity_score);
}
"""

reduce_sum_count = """
function (keys, values, rereduce) {
    results = {"sum": 0, "count": 0};
    if (rereduce) {
        for (var i = 0; i < values.length; i++) {
            results.sum += values[i].sum;
            results.count += values[i].count;
        }
    } else {
        for(var j = 0; j < values.length; j++){
            results.sum += values[j];
        }
        results.count = values.length;
    }
    return results;
}
"""

sa_polarity = design.ViewDefinition(
    "geo", "sa_polarity", map_sa3_polarity, reduce_sum_count
)
sa_polarity.sync(hist)
