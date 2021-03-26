import json

from flask import Flask


def search(term):
    term = term.lower()  # prevents case sensitivity
    results = []
    for k, v in data.items():
        if term in k or term in v:
            results.append(k)
        elif k in term:
            results.append(k)

    return results


with open("data.json", "r") as data:
    data = json.loads(data.read())

term = input("Search: ")

results = search(term)

print(f"Your search returned {len(results)} results.")

for result in results:
    print(result.title())
