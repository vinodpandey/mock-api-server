from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Api
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request, path):
    method = 'GET'
    if request.method == 'POST':
        method = 'POST'
    response_obj = get_object_or_404(Api, path='/'+path, is_enabled=True, method=method)
    if int(response_obj.status) == 503 or int(response_obj.status) == 401:
        response = HttpResponse()
        response.status_code = int(response_obj.status)
    else:
        response = HttpResponse(content_type='application/json')
        response.status_code = int(response_obj.status)
        response.content = response_obj.response
    return response
