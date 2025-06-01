import json

book = {}
book['tom'] = {
    "name" : "tom",
    "address" : "1 red street, NY",
    "phone" : 2548451215
}

book['bob'] = {
    "name" : "bob",
    "address" : "1 blue street, NY",
    "phone" : 124548754
}

s = json.dumps(book)
print(s)