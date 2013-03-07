import socket
import hashlib
 
class Server:
    """Server object for handling communications with the server"""
    def __init__(self, ip, port, password):
        self.socket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port
        self.password = password
 
    def connect(self):
        self.socket.connect ( (self.ip, self.port) ) #connect
        self.socket.recv(128) #welcome by mm
        hash1 = self.socket.recv(128) #this will contain your digest
        hash1 = hash1[17:33] #digest always at this pos
        hash1 = hash1.decode() #decode bytes to str
        key = hash1 + self.password #add pass to digest
        key = md5(key) #create a hash of this
        login = 'login {0}\n'.format(key) #send the login command with our hash
        login = login.encode() #encode this to bytes
        self.socket.send(login) #send it to the server
        tmp = self.socket.recv(128)
        tmp = tmp.decode()
        return tmp.replace("\\n", "\n") #characters such as these are escaped
     
def md5(k):
    """creates an MD5 hash of a particular given string
    k:str"""
    md5 = hashlib.md5() #make a new md5 object
    k = k.encode() #coverting string to bytes
    key= md5.update(k) #md5'ing it all
    key = md5.hexdigest()
    return key

if __name__ == "__main__":
    myServer = Server(ip, int(port), password)
    print(myServer.connect())
