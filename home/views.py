
# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')




# views.py
from django.http import JsonResponse
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from .models import ExchangeData
from .serializers import ExchangeDataSerializer

@csrf_exempt
def get_all_exchange_data(request):
    if request.method == 'GET':
        exchange_data = ExchangeData.objects.all()
        serializer = ExchangeDataSerializer(exchange_data, many=True)
        return JsonResponse(serializer.data, safe=False)