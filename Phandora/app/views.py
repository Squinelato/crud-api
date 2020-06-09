from django.shortcuts import render


from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from app.models import App
from app.serializers import AppSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def app_list(request):
    if request.method == 'GET':
        app = App.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            app = app.filter(name__icontains=name)
        
        app_serializer = AppSerializer(app, many=True)
        return JsonResponse(app_serializer.data, safe=False)
    elif request.method == 'POST':
        app_data = JSONParser().parse(request)
        app_serializer = AppSerializer(data=app_data)
        if app_serializer.is_valid():
            app_serializer.save()
            return JsonResponse(app_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(app_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = App.objects.all().delete()
        return JsonResponse({'message': '{} Records were deleted successfully!'.format(count[0])}, 
                            status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def app_detail(request, pk):
    try:
        app = App.objects.get(pk=pk)

        if request.method == 'GET':
            app_serializer = AppSerializer(app)
            return JsonResponse(app_serializer.data)
        elif request.method == 'POST':
            app_data = JSONParser().parse(request)
            app_serializer = AppSerializer(app, data=app_data)
            if app_serializer.is_valid():
                app_serializer.save()
                return JsonResponse(app_serializer.data)
            return JsonResponse(app_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'PUT':
            app_data = JSONParser().parse(request)
            app_serializer = AppSerializer(app, data=app_data)
            if app_serializer.is_valid():
                app_serializer.save()
                return JsonResponse(app_serializer.data)
            return JsonResponse(app_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            app.delete()
            return JsonResponse({'message': 'Record was deleted sucessfully!'}, 
                                status=status.HTTP_204_NO_CONTENT)

    except App.DoesNotExist:
        return JsonResponse({'message': 'The record does not exist'}, 
                             status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def app_list_supers(request):
    app = App.objects.filter(permission='super')

    if request.method == 'GET':
        app_serializer = AppSerializer(app, many=True)
        return JsonResponse(app_serializer.data, safe=False)
