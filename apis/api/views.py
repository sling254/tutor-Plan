from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


@api_view(['GET'])
def getRouter(request):
    routes =  [
        '/api/token',
        '/api/token/refresh',
    ]


    return Response(routes)

