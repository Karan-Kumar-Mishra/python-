import requests
import urllib.request
r=requests.get("https://www.google.com")
print(r.text)
r=urllib.request.urlopen("https://www.google.com")
timeout = 1
try:
    requests.head("http://www.google.com/", timeout=timeout)
    # Do something
    print('The internet connection is active')
except requests.ConnectionError:
    # Do something
    print("The internet connection is down")
