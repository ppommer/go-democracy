#!/usr/bin/python3

import sys
import requests

aliases = {}
party = sys.argv[1]

def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://graphql2.staging.br24.beta.br24.de/graphql', json={'query': query}, headers=None)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

        
# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.       
query = """{
  filterTags(searchTerm: \"""" + party + """\") {
                        nodes {
                                    id
                                            text
                                                  }
                }
  }
  """

result = run_query(query) # Execute the query

result = result["data"]["filterTags"]["nodes"]
for r, _ in zip(result, range(10000)):
    print("\"{}\", ".format(r["text"]), end="")
    #print(r["publicationDate"])
    #print(r["teaserText"])
