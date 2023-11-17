#Imports
from webserver import WebServer
from files.file_tools import FileTools



serverIP = "127.0.0.1"
serverPort = 11000
num_clients=5
FileTools()
web_server=WebServer(serverIP,serverPort,num_clients)
web_server.open_webserver()