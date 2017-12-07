import json
from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel

from cfeapi.mixins import HttpResponseMixin
from .mixins import CSRFExemptMixin


# Creating, Updating, Deleting, Retrieving (1) -- Update Model

class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    '''
    Retrieve, Update, Delete --> Object
    '''
    is_json = True

    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        json_data = {}
        return self.render_to_response(json_data)

    def put(self, request, *args, **kwargs):
        json_data = {}
        return self.render_to_response(json_data)

    def delete(self, request, *args, **kwargs):
        json_data = {}
        return self.render_to_response(json_data, status=403)



class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    '''
    List View
    Create View
    '''
    is_json = True


    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        data = json.dumps({"message": "Unknown data"})
        return self.render_to_response(data, status=400)

    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message": "You cannot delete an entire list."})
        status_code = 403 #Not Allowed
        return self.render_to_response(data, status=403)






