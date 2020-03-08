from elasticsearch import Elasticsearch
import json

INDEX = "runbook_index"
DOC_TYPE = "r3d3_type"
LOG_SNIPPET = "java.lang.RuntimeException: Cannot reserve additional contiguous bytes in the vectorized reader"
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# GET document id
# r = es.get(index=INDEX, doc_type=DOC_TYPE, id=1)
# print(r)
res = es.search(index=INDEX, body={"query": {"match": {"Log snippet": LOG_SNIPPET}}})
print(json.dumps(res, indent=2, sort_keys=True))
# print(res['hits']['total'])
# total_results = res['hits']['total']['value']
# print("Total results found: %d" % total_results)
# if total_results > 0:
#     print("search results:")
#     # Print all log snippets and action to do
#     items = res['hits']['hits']
#     for item in items:
#         source = item['_source']
#         print("full log snippet:")
#         print(source['Log snippet'])
#         print("Action TO DO:")
#         print(source['Action To Do'])
#         print("-".center(30, '-'))
# else:
#     print("No results found")