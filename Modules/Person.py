import json
from Helper.Helper import object_to_dict


class Name:
    first: str
    middle: str
    last: str


class PersonInfo:
    id: str
    name = Name()


class WorkInfo:
    company_name: str
    work_experience: str


class Communication:
    phones: [str]
    mails: [str]


def get_person():
    return Person(dict())


class Person:
    some_number2: float
    some_number1: float
    person_info = PersonInfo()
    work_info = WorkInfo()
    communication = Communication()

    def __init__(self, entries):
        vars(self).update(entries)

    def set_person(self, **entries):
        self.person_info.id = entries.pop("id")
        self.person_info.name.first = entries.pop("first")
        self.person_info.name.middle = entries.pop("middle")
        self.person_info.name.last = entries.pop("last")
        self.work_info.company_name = entries.pop("company_name")
        self.work_info.work_experience = entries.pop("work_experience")
        self.communication.phones = entries.pop("phones")
        self.communication.mails = entries.pop("mails")
        self.some_number1 = entries.pop("some_number1")
        self.some_number2 = entries.pop("some_number2")

    def get_id(self) -> str:
        return self.person_info.id

    def get_person_info(self) -> PersonInfo:
        return self.person_info

    def get_json(self) -> str:
        obj_dict = object_to_dict(self)
        return json.dumps(obj_dict)
