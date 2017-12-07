from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


from .models import Update
#def detial_view(request):
    #return render(request, template, {}) # return JSON data  --> JS Object Notion
    #return HttpResponse(get_template().render({}))


def update_model_detail_view(request):
    '''
    URI -- for a REST API
    '''
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    return JsonResponse(data)