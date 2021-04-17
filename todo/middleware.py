from django.http import JsonResponse
from rest_framework import status
from .utils import sys_type
from django.conf import settings

class AllowOriginMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self,request, view_func, view_args, view_kwargs):

        envs = request.environ
        req_dev_type = sys_type(request)
        print(req_dev_type)
        if req_dev_type == None:
            return JsonResponse({'msg':'Unknown Origin'},status=status.HTTP_403_FORBIDDEN)
        elif req_dev_type == 'WEB':
            path = request.get_full_path()
            print(path)
            if 'admin' in path:
                print('hi')
                return None
            elif envs.get("HTTP_ORIGIN") not in settings.ALLOWED_ORIGIN:
                return JsonResponse({'msg':'Unknown Origin'},status=status.HTTP_403_FORBIDDEN)
        elif not (req_dev_type == 'POSTMAN' and settings.ALLOW_POSTMAN):
            return JsonResponse({'msg':'Unknown Origin'},status=status.HTTP_403_FORBIDDEN)
        return None