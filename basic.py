import json
import requests

endpoint="http://127.0.0.1:8000/products/1/"


get_response=requests.get(endpoint,json={"Title":"Good Idea"})
print(get_response.json())