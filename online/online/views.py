from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def textRes (request):
    return Response({"text": "collected"})