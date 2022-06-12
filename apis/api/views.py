from django.http import JsonResponse


def getRouter(request):
    routes =  [
        '/api/token',
        '/api/token/refresh',
    ]


    return JsonResponse(routes, safe=False)

