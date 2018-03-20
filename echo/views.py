from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


# Create your views here.
def echo(request):
    msg = request.GET.get('msg', None)

    # Empty string is not considered as error.
    if msg is None:
        error_message = {'error': "Query parameter 'msg' required."}
        return JsonResponse(error_message, status=400)
    
    return JsonResponse({'msg': msg})