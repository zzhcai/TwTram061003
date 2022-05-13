"""
@author Team 31, Melborune, 2022

Bingzhe Jin (1080774), Hongwei Chen (891632), Tian Hui (1054513),
Zhen Cai (1049487), Ziqi Zhang (1241157)

"""

import couchdb
from couchdb import design

SERVER = "http://admin:admin@localhost:5984"
server = couchdb.Server(SERVER)

try:
    hist = server["historic_melb"]
except couchdb.http.ResourceNotFound:
    hist = server.create("historic_melb")
try:
    melb = server["melb_db"]
except couchdb.http.ResourceNotFound:
    melb = server.create("melb_db")


senti = ["polarity", "introspection", "temper", "attitude", "sensitivity"]

for s in senti:

    map_sa = """
    function (doc) {
        emit([doc.sa4, doc.sa3, doc.sa2], doc.%s_score);
    }
    """ % s

    map_id = """
    function (doc) {
        emit([id], doc.%s_score);
    }
    """ % s

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

    reduce_max_id = """
    function (keys, values, rereduce) {
        results = {"max": -1, "id": null};
        if (rereduce) {
            for (var i = 0; i < values.length; i++) {
                if (values[i].max >= results.max) {
                    results.max = values[i].max;
                    results.id = values[i].id;
                }
            }
        } else {
            for (var j = 0; j < values.length; j++) {
                if (values[j] >= results.max) {
                    results.max = values[j];
                    results.id = keys[i];
                }
            }
        }
        return results;
    }
    """

    reduce_min_id = """
    function (keys, values, rereduce) {
        results = {"min": 1, "id": null};
        if (rereduce) {
            for (var i = 0; i < values.length; i++) {
                if (values[i].min <= results.min) {
                    results.min = values[i].min;
                    results.id = values[i].id;
                }
            }
        } else {
            for (var j = 0; j < values.length; j++) {
                if (values[j] <= results.min) {
                    results.min = values[j];
                    results.id = keys[i];
                }
            }
        }
        return results;
    }
    """

    sa_sum_count = design.ViewDefinition(
        s, "sa_sum_count", map_sa, reduce_sum_count
    )
    sa_sum_count.sync(hist)

    sum_count = design.ViewDefinition(
        s, "sum_count", map_id, reduce_sum_count
    )
    sum_count.sync(melb)

    max_id = design.ViewDefinition(
        s, "max_id", map_id, reduce_max_id
    )
    max_id.sync(hist)
    max_id.sync(melb)

    min_id = design.ViewDefinition(
        s, "min_id", map_id, reduce_min_id
    )
    min_id.sync(hist)
    min_id.sync(melb)
