#! /usr/env python3
import requests

def send():
	h = {
			'Connection':'keep-alive',
			'Content-Length': '60',
			'Cache-Control':'max-age=0',
			'Upgrade-Insecure-Requests':'1',
			'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
			'Origin':'https://www.sas.ulisboa.pt',
			'Content-Type':'application/x-www-form-urlencoded',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
			'Referer':'https://www.sas.ulisboa.pt/index.php?opt=4;03',
			'Accept-Encoding':'gzip, deflate, br',
			'Accept-Language':'en-US,en;q=0.9,pt;q=0.8',
			'Cookie':'_ga=GA1.2.313966427.1550356578; PHPSESSID=67bf2d28daeb44ed8458783749418f06; SimpleSAMLAuthToken=_565f82766ba3849fa26e6b1d8721fd819940a011f1; _gid=GA1.2.1646023247.1557308652; _gat_gtag_UA_47704932_1=1'
		}
	d = {'opt':'4;4H1','chvP':'116;2019-05-08;1','dia':'','other':'','searchbox':''}
	resp = requests.post('http://www.sas.ulisboa.pt/index.php', data = d, headers = h)
	print(resp.status_code)

send()

'''POST /index.php HTTP/1.1
Host: www.sas.ulisboa.pt
Connection: keep-alive
Content-Length: 60
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36
Origin: https://www.sas.ulisboa.pt
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Referer: https://www.sas.ulisboa.pt/index.php?opt=4;03
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,pt;q=0.8
Cookie: _ga=GA1.2.313966427.1550356578; PHPSESSID=67bf2d28daeb44ed8458783749418f06; SimpleSAMLAuthToken=_565f82766ba3849fa26e6b1d8721fd819940a011f1; _gid=GA1.2.1646023247.1557308652; _gat_gtag_UA_47704932_1=1'''