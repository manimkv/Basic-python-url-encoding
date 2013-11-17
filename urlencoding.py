from socket import * 
import re
import sys             
s=socket(AF_INET,SOCK_STREAM)          
host="localhost"

#Port number is taken while running the program

port=int(sys.argv[1])          
s.bind((host,port))        
s.listen(5)               
while True:
   c,addr=s.accept() 
   data=c.recv(1024) 
   
#If response contains file.html in it we extract it and send to browser

   matchh=re.search(r'GET\s/([\w]+).html',data)
   if (matchh): 
        c.send('HTTP/1.0 200 OK \r\n')
        c.send('Content-Type: text/html\r\n\r\n') 
        c.send(open(matchh.group(1)+".html").read()) 

#If response contains username and password we extract it and write to a file

   match=re.search(r'firstname=([\w_.]+)&pwd=([\w.]+)',data) 
   if (match):
        print data,count
        print match.group(1)
        print match.group(2)
        f=open("data.txt","a")
        f.write("\nUsername:")
        f.write(match.group(1))
        f.write("\nPassword:")
        f.write(match.group(2))
        f.close()
        c.send("welcome  "+match.group(1))

