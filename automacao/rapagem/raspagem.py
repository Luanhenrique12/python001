import requests, bs4, os 
url= "https://www.playstation.com/pt-br/"
os.makedirs("playstation", exist_ok=True)
while not url.endswith("#"):
    print("Downloading page %s..." % url)
    res=requests.get(url)
    res.raise_for_status()
    soup= bs4.BeautifulSoup(res.text)
    print(soup)