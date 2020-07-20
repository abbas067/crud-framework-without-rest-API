from django.shortcuts import render
from testapp.models import  Employee
from django.views.generic import View
from  django.http import HttpResponse
from  django.views.decorators.csrf  import csrf_exempt
from  django.utils.decorators import method_decorator
import json
from django.core.serializers import serialize
from testapp.mixins import SerializeMixin,HttpResponseMixin
from testapp.util import is_json
from testapp.forms import EmployeeForm
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeDetailsCBV(SerializeMixin,HttpResponseMixin,View):
    def get_object_by_id(self,id):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp=None
        return emp
    def put(self,request,id,*args,**kwargs):
         emp=self.get_object_by_id(id=id)
         if emp is None:
             json_data=json.dumps({'msg':'No  Matched record  found not possible to updation '})
             return self.render_to_http_response(json_data,status=404)
         data=request.body
         valid_json=is_json(data)
         if not valid_json:
             json_data=json.dumps({'msg':'please send valid json data'})
             return self.render_to_http_response(json_data,status=400)
         provided_data=json.loads(data)
         origial_data={
          'eno':emp.eno,
          'ename':emp.ename,
          'esal':emp.esal,
          'eaddr':emp.eaddr,
          }
         origial_data.update(provided_data)
         form=EmployeeForm(origial_data,instance=emp)
         if form.is_valid():
              form.save()
              json_data=json.dumps({'msg':'Resource update successfully'})
              return self.render_to_http_response(json_data)
         if form.errors:
                json_data=json.dumps(form.errors)
                return self.render_to_http_response(json_data,status=400)
    def delete(self,request,id,*args,**kwargs):
         emp=self.get_object_by_id(id=id)
         if emp is None:
             json_data=json.dumps({'msg':'No  Matched record  found not possible to delete '})
             return self.render_to_http_response(json_data,status=404)
         status,deleted_item=emp.delete()
         if status==1:
             json_data=json.dumps({'msg':'resource deleted successfully'})
             return self.render_to_http_response(json_data)
         else:
             json_data=json.dumps({'msg':'unale to delete'})
             return self.render_to_http_response(json_data)
    def get(self,request,id,*args,**kwargs):
        #emp=Employee.objects.get(id=id)
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data=json.dumps({'msg':'The requested resource not availale'})
            return self.render_to_http_response(json_data,status=404)
        else:
          json_data=self.serialize([emp,])
          return self.render_to_http_response(json_data)
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeListCBV(SerializeMixin,HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        json_data=self.serialize(qs)
        return HttpResponse(json_data,content_type='application/json')
    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'please send valid json data'})
            return self.render_to_http_response(json_data,status=400)
        empdata=json.loads(data)
        form=EmployeeForm(empdata)
        if form.is_valid():
            form.save()
            json_data=json.dumps({'msg':'resource created successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)
@method_decorator(csrf_exempt,name='dispatch')          
class EmployeeCRUDCBV(HttpResponseMixin,SerializeMixin,View):
   def get_object_by_id(self,id):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp=None
        return emp
   def get(self,request,*args,**kwargs):
      data=request.body
      valid_json=is_json(data)
      if not valid_json:
           json_data=json.dumps({'msg':'please send valid json data'})
           return self.render_to_http_response(json_data,status=400)
      pdata=json.loads(data)
      id=pdata.get('id',None)
      if id is not None:
          emp=self.get_object_by_id(id)
          if emp is None:
              json_data=json.dumps({'msg':'The requested resource not availale with matched id'})
              return self.render_to_http_response(json_data,status=404)
          json_data=self.serialize([emp,])
          return self.render_to_http_response(json_data)
      qs=Employee.objects.all()
      json_data=self.serialize(qs)
      return self.render_to_http_response(json_data)
   def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'please send valid json data'})
            return self.render_to_http_response(json_data,status=400)
        empdata=json.loads(data)
        form=EmployeeForm(empdata)
        if form.is_valid():
            form.save()
            json_data=json.dumps({'msg':'resource created successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)   
   def put(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'please send valid json data'})
            return self.render_to_http_response(json_data,status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is None:
             json_data=json.dumps({'msg':'to perform updation id is manadatory please provide'})
             return self.render_to_http_response(json_data,status=400)
        emp=self.get_object_by_id(id)
        if emp is None:
              json_data=json.dumps({'msg':'No resource with matched id, not possible to perform updation'})
              return self.render_to_http_response(json_data,status=404)
        provided_data=json.loads(data)
        origial_data={
          'eno':emp.eno,
          'ename':emp.ename,
          'esal':emp.esal,
          'eaddr':emp.eaddr,
          }
        origial_data.update(provided_data)
        form=EmployeeForm(origial_data,instance=emp)
        if form.is_valid():
              form.save()
              json_data=json.dumps({'msg':'Resource update successfully'})
              return self.render_to_http_response(json_data)
        if form.errors:
                json_data=json.dumps(form.errors)
                return self.render_to_http_response(json_data,status=400)     
   def delete(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'please send valid json data'})
            return self.render_to_http_response(json_data,status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            emp=self.get_object_by_id(id)
            if emp is None:
              json_data=json.dumps({'msg':'No resource with matched id, not possible to delete'})
              return self.render_to_http_response(json_data,status=404)
            status,deleted_item=emp.delete()
            if status==1:
             json_data=json.dumps({'msg':'resource deleted successfully'})
             return self.render_to_http_response(json_data)
            json_data=json.dumps({'msg':'unale to delete'})
            return self.render_to_http_response(json_data)
        
         

