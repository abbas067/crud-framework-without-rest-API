import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
def get_resource(id=None):
   data={}
   if id is not None:
    data={
	  'id':id
	  }
   resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
   print(resp.status_code)
   print(resp.json())
def create_resource():
    new_emp={
    'eno':110,
    'ename':'ausaf',
    'esal':30000,
    'eaddr':'chennai'
    }
    resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
def update_resource(id):
    new_emp={
    'id':id,
    'esal':7000,
    'eaddr':'hyd',
    }
    resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
#update_resource(1)
def delete_resource(id):
    new_emp={
    'id':id,
    }
    resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
delete_resource(50)