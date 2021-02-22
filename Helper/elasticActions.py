import elasticsearch

errorMsg = "Error creating index: {0}. return status {1}. Massage {2}"


def create_index(es: elasticsearch.Elasticsearch, index: str, mapping):
    if not es.indices.exists(index=index):
        status_msg = es.indices.create(index=index, body=mapping, ignore=400)
        if "status" in status_msg and status_msg["status"] > 399:
            print(errorMsg.format(index, status_msg["status"], status_msg))
        else:
            print(index + " Successfully created!")
    else:
        print("Index exist! Find other Index!")


def insert_info(es: elasticsearch.Elasticsearch, index: str, body, in_index_id: str):
    try:
        status_msg = es.index(index=index, doc_type="_doc", body=body, id=in_index_id)
        print("Successfully inserted!")
        print(status_msg)
    except Exception as e:
        pass
        print("Error insert data")
        print("Exception raised: {}".format(e))


def get_info_by_query(es: elasticsearch.Elasticsearch, index: str, body):
    res = es.search(index=index, doc_type="_doc", body=body)
    return res["hits"]["hits"]


def delete_index(es: elasticsearch.Elasticsearch, index: str):
    es.indices.delete(index=index, ignore=[400, 404])


def delete_from_index_by_id(es: elasticsearch.Elasticsearch, index: str, id: str):
    try:
        status_msg = es.delete(index=index, id=id, doc_type="_doc")
        print("Successfully deleting!")
        print(status_msg)
    except Exception as e:
        pass
        print("Error deleting data")
        print("Exception raised: {}".format(e))
