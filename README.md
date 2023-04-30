# Socket-Programming---SinglePlayer-BlackJack-Game---Python-
SinglePlayer BlackJack Game using Python  to demonstrate Socket Programming.

--------------------------------------------------------------------
Steps to run:                                                                                     
Save the client file in the client computer, and server file in the server.                                                                   
Change the Server ip address present in the code from the loopback address to the server ip address.                                                                                                                      
command to run - python filename                                    
                 python3 filename                                
                 
--------------------------------------------------------------------
Demonstrating of Socket Programming by making of a blackjack game involving a dealer (server) and a player (client), connected through a TCP connection.
The server is responsible for handling the game logic and the client is responsible for communicating with the server and displaying the game state to the user.

The game involves the player and dealer drawing a card until the player wishes to stop, with the points of all the cards being totalled. The player’s goal is to have their points as close to 21 as possible without going over 21 points or having less points than the dealer.

The server side code, deals with the drawing of cards and keeping track of the points, and then sending to the client, through a TCP connection, necessary encoded data such as the card drawn and the points earned, so that they can be displayed on the client at the appropriate time. 
The client side code, deals with printing the necessary instructions to the player, decoding information sent by server, and also taking the player’s input and sending it encoded to the server.
This encoding is necessary to send string information through variables.
The code includes while loops to deal with starting a new game, different rounds in a game, and the outermost one in the server-side code deals with keeping the server forever active.

----------------------------------------------------------------------

PES University - 4th Sem Computer Networks Project
Made By - 
Pragnya Vempati
Pratham Prabal R
Ranjitha S K

