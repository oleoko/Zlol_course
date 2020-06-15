import socket
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 1234))
s.listen(1)

while True:
    clientsocket, address = s.accept()
    print("Connection from address {} has been established".format(address))
    cfile = clientsocket.makefile('rw', 1024)
    line = cfile.readline().strip().split()[1]
    print(line)
    cfile.write('HTTP/1.0 200 OK\n\n')
    cfile.write('<html><head><title>Welcome %s!</title></head>' % (str(address)))
    cfile.write('<body><h1>Directories walk</h1>')

    # directory change block
    if (line != "/" and line != "/favicon.ico"):
        os.chdir(str(line[1:]))

    # Generating page block
    cfile.write('<p><a href = http://localhost:1234/>'+'..'+'</a></p>')
    for root, dirs, files in os.walk(".", topdown=True):
        cfile.write("FOLDER(S):")
        for dir in dirs:
            cfile.write('<p><a href = http://localhost:1234/{}>'.format(dir)+str(dir)+'</a>')
        cfile.write("<p>FILE(S):")
        for file in files:
            cfile.write('<p>'+file+'</p>')
        break
    cfile.write('</body></html>')


