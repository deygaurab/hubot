import requests
import json

def search(uri, term):
    """Simple Elasticsearch Query"""
    query = json.dumps({
        "query": {
            "match": {
                "Log snippet": term
            }
        }
    })
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.get(uri, data=query, headers=headers)
    results = json.loads(response.text)
    return results

# LOG_SNIPPET = "java.lang.RuntimeException: Cannot reserve additional contiguous " \
#               "bytes in the vectorized reader"


LOG_SNIPPET = "bytes in the vectorized reader"
es_base_url = 'http://localhost:9200/'
index = "runbook_index"
doc_type = 'r3d3_type'
uri = es_base_url+index+"/"+doc_type+"/_search"
print(uri)
res = search(uri, term=LOG_SNIPPET)
print(json.dumps(res))
# print(res['hits']['total'])
total_results = res['hits']['total']['value']
# print("Total results found: %d" % total_results)
if total_results > 0:
    print("search results:")
    # Print all log snippets and action to do
    # items = res['hits']['hits']
    # print(json.dumps(items))
    # for item in items:
    #     source = item['_source']
    #     print("full log snippet:")
    #     print(source['Log snippet'])
    #     print("Action TO DO:")
    #     print(source['Action To Do'])
    #     print("-".center(30, '-'))
else:
    print("No results found")