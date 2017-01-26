#!/usr/bin/env python
import random, socket, sys
from time import sleep
import quotes

server = "irc.freenode.net"
chan = "#chicago"
nick = "TronaldDump"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Time to make IRC great again..connecting to: "+server

irc.connect((server, 6667))
irc.send("USER "+ nick +" "+ nick +" "+ nick +" :This is a fun bot!\n")
irc.send("NICK "+ nick +"\n")         
irc.send("PRIVMSG nickserv :iNOOPE\r\n")
irc.send("JOIN "+ chan +"\n")

while 1:    
    text=irc.recv(2040)  
    print text   

    if text.find('PING') != -1:                          
       irc.send('PONG ' + text.split() [1] + '\r\n')

    if text.find(':trump') !=-1: 
        t = text.split(':trump') 
        to = t[1].strip() 
        reply = random.choice(quotes.qdb)
        sleep(1)
        irc.send('PRIVMSG '+chan+' :'+reply+' \r\n')
