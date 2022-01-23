from django.views.generic.edit import CreateView
from .models import Address
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AddressSerializer

# Create your views here.
@api_view(['GET'])
def addressList(request):
  address =Address.objects.all()
  serializer = AddressSerializer(address, many=True)
  return Response(serializer.data)
