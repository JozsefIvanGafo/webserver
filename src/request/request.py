


class Request:

    def __init__(self) -> None:
        pass
    

    def extract_request(self,data:str):

        #We split the data
        data_in_lines=data.split("\r\n")


        #We extract the first line (method,path and )
        first_line=data_in_lines[0].split(" ")


        request_dict={
                "Method":first_line[0],
                "Path":first_line[1],
                "Version":first_line[2]
        }

        parameters=("Host","Connection")
        for line in data_in_lines:
            new_line=line.split(":")

            #We save the host 
            if new_line[0]=="Host":
                request_dict["Host"]=new_line[1]
                continue
            
            #We save if we mantain connection
            if new_line[0]=="Connection":
                request_dict["Connection"]=new_line[1]
                continue

            #We save the browser
            if new_line[0]=="sec-ch-ua":
                request_dict["Browser"]=new_line[1].split(";")[0]
                continue

            #Information about the user browser
            if new_line[0]=="User-Agent":
                request_dict["User-Agent"]=new_line[1]
                continue
            
            #What file types the browser accepts
            if new_line[0]=="Accept":
                request_dict["Accept"]=new_line[1].split(",")
                continue

            if new_line[0]=="Accept-Encoding":
                request_dict["Accept-Encoding"]=new_line[1].split(",")
                continue

        return request_dict

        