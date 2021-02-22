from Modules.Person import *
from Helper.elasticActions import *
from Helper.Helper import *
from Helper.elastic_queries import *

es = elasticsearch.Elasticsearch([{"host": "localhost", "port": 9200}])
index = "test_number"
mapping = {
    "mappings": {
        "properties": {
            "person_info": {
                "properties": {
                    "name": {
                        "properties": {
                            "first": {"type": "keyword"},
                            "middle": {"type": "keyword"},
                            "last": {"type": "keyword"}
                        }

                    },
                    "id": {"type": "keyword"},
                }
            },
            "work_info": {
                "properties": {
                    "company_name": {"type": "keyword"},
                    "work_experience": {"type": "keyword"},
                }
            },
            "communication": {
                "properties": {
                    "phones": {"type": "keyword"},
                    "mails": {"type": "keyword"},
                }
            },
            "some_number1": {"type": "long"},
            "some_number2": {"type": "long"}
        }
    }
}

# create_index(es=es, index=index, mapping=mapping)

person = get_person()
person.set_person(first="Simon", middle=None, last="Chuko", id="123456", company_name="Intel", work_experience="3",
                  phones=["225", "111"], mails=["rres@mail.com"], some_number1=15, some_number2=7)

# insert_info(es=es, index=index, body=person.get_json(), in_index_id=person.get_id())

# hits = get_info_by_query(es=es, index=index, body=query_search_by_range)
# data = hits[0]["_source"]
# res_person = convert_hit_to_class(data, Person)
# print(res_person.get_id())

# delete_from_index_by_id(es=es, id="123456", index=index)

print(person.get_json())
