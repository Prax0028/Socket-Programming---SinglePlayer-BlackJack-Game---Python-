from socket import *
import sys

serverName = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
#try:
clientSocket.connect((serverName, serverPort))
#except error:
 #   clientSocket.connect((serverName, serverPort+1))


while True:
    while True:
        cnum = clientSocket.recv(1024).decode()
        ctype = clientSocket.recv(1024).decode()
        print(f"You recieved {cnum} of {ctype}. HIT or STAND?")
        inp = input(">").upper()
        clientSocket.send(inp.encode())

        if(inp=='STAND'):
            pp = int(clientSocket.recv(1024).decode())
            dp = int(clientSocket.recv(1024).decode())
            print(f"You earned {pp} points, Dealer earned {dp} points.\n")
            
            
            
            if(dp>21 and pp<21):
                print("VICTORY!\n")
            elif(pp>dp and pp<21 ):
                print("VICTORY!\n")
            else:
                print("Loss\n")
            break
        
            
        elif(inp=="HIT"):
            continue
        else:
            print("Error. Try Again. Please Respond Only HIT or STAND.\n")
            continue

    print("Would you like to continue? Y or N?")
    inp = input(">").upper()
    clientSocket.send(inp.encode())
    if(inp=="Y"):
        continue
    else:
        break 

clientSocket.close()