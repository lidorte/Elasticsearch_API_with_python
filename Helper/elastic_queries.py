query_search_by_first_name = {"query": {"match_phrase": {"person_info.first.keyword": "Lidor"}}}
query_search_by_range = {"query": {"range": {"some_number1": {"gte": 5, "lt": None}}}}
query_search_by_id = {"query": {"match_phrase": {"person_info.id": "123456"}}}


def query_query_search_by_range(get_id: str):
    query = {"query": {"match_phrase": {"person_info.id": get_id}}}

    return query
