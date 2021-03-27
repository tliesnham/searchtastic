import json

class Searchtastic:
    def search(keyword):
        with open("test_keyword_data.json", "r") as file:
            search_data = json.loads(file.read())
        keyword = keyword.lower()  # prevents case sensitivity
        results = []
        
        for k, v in search_data.items():
            if keyword in k:
                v.append(k)
            for term in v:
                if keyword in term:
                    results.append(k)

        return json.dumps(results)