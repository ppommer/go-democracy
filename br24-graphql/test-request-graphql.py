#!/usr/bin/python3
import sys
import requests
import json

aliases = {}

aliases["CDU"] = ["CDU", "CDU/CSU", " CDU", "CDU-Parteitag", "CDU-Generalsekretär", "CDU-Vorstand", "CDU ", "CDU-Vorsitz", "CDU-Vorsitzende", "CDU-Generalsekretärin", "CDU-Wirtschaftsrat", "CSU/CDU", "CDU-Parteivorstand", "CDU-Parteivorsitzende", "CDU-Vorstandsklausur", "CDU CSU", "CDU-Präsidium", "CDU-Spitzenkandidat", "CDU-Zentrale", " CDU/CSU", "CDU-Generalsekretär Tauber", "CDU-Politiker", "Wirtschaftsrat der CDU", "Wolfgang Bosbach, CDU", "CDU-Vize-Chefin"]
aliases["CSU"] = ["CSU", "CDU/CSU", " CSU", "CSU-Landesgruppe", "CSU-Klausur", "CSU-Parteitag", "CSU-Landtagsfraktion", "CSU-Fraktion", "CSU-Vorstand", "CSU-Chef", "CSU-Generalsekretär", "CSU-Vorsitzender", "CSU ", "Landtags-CSU", "CSU-Vorsitz", "CSU-Landesgruppenchefin", "CSU-Machtkampf", "CSU-Vorstandssitzung", "CSU-Parteivorstand", "CSU-Vize", "CSU/CDU", "CSU-Landtagsabgeordnete", " CDU/CSU", "CSU-Bezirksparteitag", "CSU-Winterklausur"]
aliases["GRUENE"] = ["Grüne", "Die Grünen", "Bündnis 90/Die Grünen", "Grüne Woche", " Grüne", "Grünen", "B90/Die Grünen", "B.90/Grüne", "Landtagsgrüne", "Bündnis90/Grüne", "Grünes Trikot", "Grüne ", "Grünen-Klausur", "Landtags-Grüne",  " Bündnis 90/Die Grünen", "Grünen-Parteitag", "Grünen-Fraktion"]

def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://graphql2.staging.br24.beta.br24.de/graphql', json={'query': query}, headers=None)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

        
# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.       
query = """{{
    filterArticles(
        tagsFilter: {}
        sortBy: PUBLICATION_DATE_DESC
    ) {{
        nodes {{
            title
            teaserText
            publicationDate
        }}
    }}
}}""".format(json.dumps(aliases[sys.argv[1]]))

result = run_query(query) # Execute the query

result = result["data"]["filterArticles"]["nodes"]
for r, _ in zip(result, range(4)):
    print(r["title"])
    #print(r["publicationDate"])
    #print(r["teaserText"])
    print()
