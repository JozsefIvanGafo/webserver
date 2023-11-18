#We define the imports
import threading
from socket import *
from concurrent.futures import ThreadPoolExecutor

#own imports
from request.request import Request
from response.response import Response


class WebServer:

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
        finally:
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
                connection_socket,client_address=self._server_socket.accept()

                self.__handle_client(connection_socket,client_address)
                #We submit on the thread
                thread.submit(self.__handle_client,connection_socket,client_address)




    def __handle_client(self,connection_socket:socket,client_address):
        """
        Method to handle one http client request
        """
        #Extract data
        print(f"Received request from {threading.current_thread}")
        data=connection_socket.recv(2048).decode()
        request=Request().extract_request(data)
        print(request)


        #We process the answer
        with self.__lock:
            print(f"Processing answer from {threading.current_thread}")
            response=Response().generate_response(request)


            print(f"Sending response from {threading.current_thread}")
            connection_socket.sendto(response.encode(),client_address)


            connection_socket.close()

