query_search_by_first_name = {"query": {"match_phrase": {"person_info.first.keyword": "Lidor"}}}
query_search_by_range = {"query": {"range": {"some_number1": {"gte": 5, "lt": None}}}}
