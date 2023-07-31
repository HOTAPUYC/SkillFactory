import requests

status = 'available'

# GET

res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})
print(res.status_code)
print(res.text)

# POST

res1 = requests.post( f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                      json={"id": 9379992, "category": {"id": 0,"name": "string"},"name": "TOBY","photoUrls": ["string"],
        "tags": [{"id": 0,"name": "string"}],"status": "available"})
print(res1.status_code)
print(res1.json())

# PUT

headers1 = {'accept': 'application/json', 'Content-Type': 'application/json'}
data1 = {"id": 9379992,"category": {"id": 0,"name": "string"},"name": "DOBY","photoUrls": ["string"],
        "tags": [{"id": 0,"name": "string"}],"status": "available"}
res2 = requests.put( f"https://petstore.swagger.io/v2/pet", headers=headers1, json=data1)
print(res2.status_code)
print(res2.json(), '\n\n', '-' * 100)

# DELETE

headers2 = {'accept': 'application/json'}
res3 = requests.delete(f"https://petstore.swagger.io/v2/pet/{9379992}", headers=headers2)
print(res3.status_code)
print(res3.json())





