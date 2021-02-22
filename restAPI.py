from flask import Flask, request
from flask_restful import Api, Resource
from Helper.elasticActions import *
from Helper.Helper import convert_hit_to_class
from Modules.Person import *
from Helper.elastic_queries import query_query_search_by_range

app = Flask(__name__)
api = Api(app)

es = elasticsearch.Elasticsearch([{"host": "localhost", "port": 9200}])
index = "test_number"


@app.route("/<string:id>")
def get_object_by_id(id: str):
    hits = get_info_by_query(es=es, index=index, body=query_query_search_by_range(id))
    data = hits[0]["_source"]
    return data


@app.route("/<string:id>", methods=['DELETE'])
def delete_object_by_id(id: str):
    delete_from_index_by_id(es=es, id=id, index=index)
    return {}


@app.route("/<string:id>", methods=['POST'])
def create_object(id: str):
    body = request.data
    insert_info(es=es, index=index, body=body, in_index_id=id)
    return {}


if __name__ == "__main__":
    app.run(debug=True)  # Not run with debug=True in product ENV
