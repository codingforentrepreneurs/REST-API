import json


from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from cfeapi.mixins import JsonResponseMixin

from .models import Update
#def detial_view(request):
    #return render(request, template, {}) # return JSON data  --> JS Object Notion
    #return HttpResponse(get_template().render({}))

# obj = Update.objects.get(id=1)

def json_example_view(request):
    '''
    URI -- for a REST API
    GET -- Retrieve
    '''
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    json_data = json.dumps(data)
    #return JsonResponse(data)
    return HttpResponse(json_data, content_type='application/json')



class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
     def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return self.render_to_json_response(data)



