#We define the imports
from socket import *
import threading
from concurrent.futures import ThreadPoolExecutor
from files.files import *


class Webserver:

    def __init__(self,serverIP:str,serverPort:int,num_clients:int) -> None:
        #Define the socket variables
        self._server_ip=serverIP
        self._server_port=serverPort

        #We accept ipv4 and we want a reliable connection (TCP)
        self._server_socket=socket(AF_INET, SOCK_STREAM)
        #We bind it to a port and an ip
        self._server_socket.bind((self._server_ip,self._server_port))

        #Number of clients we want the server to listen
        self._number_clients=num_clients
        self._server_socket.listen(num_clients)

        #To avoid writing at the same time on a common variable
        self.__lock=threading.Lock( )

        print("The server is ready to receive")


    def open_webserver(self):
        """
        Method to open the loop of the server to receive incoming http requests
        """
        try:
            print("initializing the server")
            self.__loop()

        except KeyboardInterrupt:
            #When we detect a ctrl C
            print("closing the server...")
            self._server_socket.close()
            print("The server is closed")



    def __loop(self):
        """
        Method where we define the main loop of the server to handle clients
        """
        #We define the thread pool
        with ThreadPoolExecutor(max_workers=self._number_clients) as thread:
            while True:
                #We wait until we receive an answer
                client_socket=self._server_socket.accept()
                #We submit on the thread
                thread.submit(self.__handle_client,client_socket)








    def __handle_client(self,client_socket):
        """
        Method to handle one http client request
        """
        connection_socket, client_address=client_socket
        