from email import message
from django.http import request
from django.shortcuts import redirect, render

from frontend.filters import AddressFilter
from .forms import AddressForm
import pandas as pd
from address.models import Address
# Create your views here.
def home(request):
  address = Address.objects.filter(date__month=1, date__year='2022').distinct()
  print(address)
  return render(request, 'frontend/home.html')

def upload(request):
  if request.method == 'POST':
    data = request.FILES['document']
    # form = UploadFileForm(request.POST, request.FILES)
    if not data.name.endswith('xlsx'):
      print('Bad data')
    extract_data = pd.read_excel(data)
    try:
      for NAME, ADDRESS, LONG, LAT, DATE in zip(extract_data.name,extract_data.address, extract_data.long, extract_data.lat, extract_data.date):
        address = Address(name=NAME,address=ADDRESS, long=LONG, lat=LAT, date=DATE)
        address.save()
        return redirect('home')
    except:
      message = {'bad data'}
      print(message)
  return render(request, 'frontend/home.html')


def list_data(request):
  addresses = Address.objects.all()
  my_filter = AddressFilter(request.GET, queryset=addresses)
  addresses = my_filter.qs
  context = {'addresses':addresses, 'my_filter':my_filter}
  return render(request, 'frontend/list_data.html', context)


def delete(request, pk):
	address = Address.objects.get(id=pk)
	if request.method == "POST":
		address.delete()
		return redirect('list_data')

	return redirect('list_data')

def update(request, pk):

	order = Address.objects.get(id=pk)
	form = AddressForm(instance=order)

	if request.method == 'POST':
		form = AddressForm(request.POST, instance=order)
    
		if form.is_valid():
			form.save()
			return redirect('list_data')
    
	context = {'form':form}
	return render(request, 'frontend/update.html', context)