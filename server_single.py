from socket import * # for socket
import sys
import random 
import secrets

suite=["Hearts","Spades","Diamonds","Clubs"]
crd_num=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    
class play:
  def __init__(self):
       #self.name = name
       self.points = 0
       self.cardtype = ""
       self.cardnum = ""

  def deal_card(self):
    self.cardnum=secrets.choice(crd_num)
    self.cardtype= secrets.choice(suite)
    if(self.cardnum=="Ace"):
          num = 1
    elif(self.cardnum=="Jack" or self.cardnum=="Queen" or self.cardnum=="King"):
          num =10
    else:
          num = int(self.cardnum)
    return num
       
       

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("127.0.0.1", 12000))
 
serverSocket.listen(1)
print("Server started.\n\n")
while True:
 print("Waiting for player... \n")

 connSocket, addr = serverSocket.accept()
 print("Player Connected.\n")

 while True:
         dealer=play()
         player=play()
         
         while True:
                 dealer.points = dealer.points + dealer.deal_card()
                 player.points = player.points + player.deal_card()
                 connSocket.send(str(player.cardnum).encode())
                 connSocket.send(str(player.cardtype).encode())
                 data = connSocket.recv(1024).decode()
                 if(data=='STAND'):
                     connSocket.send(str(player.points).encode())
                     connSocket.send(str(dealer.points).encode())
                     break
                 elif(data=="HIT"):
                       continue
                 else:
                       continue
         data = connSocket.recv(1024).decode()
         if(data=="Y" or data =="y"):
              continue 
         else:
              break 
         
 connSocket.close()

             
                       
                       
        

