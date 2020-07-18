import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
def get_resource(id):
    resp=requests.get(BASE_URL+ENDPOINT+id+'/')
    print(resp.status_code)
    print(resp.json())
#id=input("enter the  id of employee to get  the  data:")
#get_resource(id)
def get_all():
    resp=requests.get(BASE_URL+ENDPOINT)
    print(resp.status_code)
    print(resp.json())
#get_all()
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
    'esal':700,
    'eaddr':'lko',
    }
    resp=requests.put(BASE_URL+ENDPOINT+str(id)+'/',data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
#update_resource(2)
def delete_resource(id):
    resp=requests.delete(BASE_URL+ENDPOINT+str(id)+'/')
    print(resp.status_code)
    print(resp.json())
while True:
 print("Welcome TO This Application \npress 1 to enter employee details\npress 2 to update employee details\npress 3 to delete employee details\npress 4 to get employee details\npress 5 to exit")
 ch=int(input("enter choice:"))
 if ch==1:
  create_resource()
 elif ch==2:
  id=int(input("enter id:"))
  update_resource(id)
 elif ch==3:
  id=int(input("enter id:"))
  delete_resource(id)
 elif ch==4:
  get_all()
 elif ch==5:
  break
 else:
  print("invalid choice")
print("Thanks for using my API")