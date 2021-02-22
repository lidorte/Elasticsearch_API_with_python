import json
import types

primitive = (int, str, bool, float, list)


def convert_hit_to_class(data_get, class_appear):
    # class_appear.__dict__ = data_get
    # return class_appear
    data_as_str = json.dumps(data_get)
    res = json.loads(data_as_str, object_hook=class_appear)
    return res


def object_to_dict(obj):
    res = {}

    for member in dir(obj):
        inner_object = getattr(obj, member)
        if relevant_attribute_for_json(member, inner_object):
            if isinstance(inner_object, primitive) and inner_object is not None:
                res[member] = inner_object
            elif inner_object is not None:
                res[member] = object_to_dict(inner_object)
    return res


def relevant_attribute_for_json(member_name: str, obj):
    return not member_name.startswith('__') \
           and not isinstance(obj, types.MethodType) \
           and not isinstance(obj, types.BuiltinFunctionType)


def dict2obj(d):
    # checking whether object d is a
    # instance of class list
    if isinstance(d, list):
        d = [dict2obj(x) for x in d]

        # if d is not a instance of dict then
    # directly object is returned
    if not isinstance(d, dict):
        return d

        # declaring a class

    class C:
        pass

    # constructor of the class passed to obj
    obj = C()

    for k in d:
        obj.__dict__[k] = dict2obj(d[k])

    return obj
