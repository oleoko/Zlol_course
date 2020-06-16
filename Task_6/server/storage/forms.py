from django import forms

class KeyForm(forms.Form):
	key_text = forms.CharField(label = 'key', max_length = 200)
	key_ip = forms.CharField(label = 'ip', max_length = 20)
class IpForm(forms.Form):
	ip_to_decrypt = forms.CharField(label = 'ip_to_decrypt', max_length = 20)