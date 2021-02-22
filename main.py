from Modules.Person import *
from Helper.elasticActions import *
import requests
from Helper.Helper import *
from Helper.elastic_queries import *

es = elasticsearch.Elasticsearch([{"host": "localhost", "port": 9200}])
index = "test_number"
BASE = "http://127.0.0.1:5000/"
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
person.set_person(first="Lidor", middle=None, last="Tevet", id="123456", company_name="****", work_experience="3",
                  phones=["225", "111"], mails=["rres@mail.com"], some_number1=15, some_number2=7)

# response = requests.get(BASE + person.get_id())
# response = requests.post(BASE + person.get_id(), person.get_json())
# print(response.json())

response = requests.delete(BASE + person.get_id())
res_person = convert_hit_to_class(response.json(), Person)
print(res_person.get_json())


