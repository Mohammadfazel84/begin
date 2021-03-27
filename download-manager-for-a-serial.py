import os
import sys
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
se = int(input("sesion :"))
ep1 = int(input("of episod :"))
ep2 = int(input("to episod :"))
def download(s,e):
    if s<10:
        s = "0"+str(s)
    if e<10:
        e = "0"+str(e)
    link = f"https://s1.irdanlod.ir/files/Serial/T/100/S{s}/720p/The.100.S{s}E{e}.720p.Censored.Farsi.Dubbed.mp4"
    file_name = urlparse(link)
    file_name = file_name.path.rsplit('/', 1)[-1]
    with open(file_name, "wb") as f:
            print("Downloading %s"% file_name)
            response = requests.get(link, stream=True)
            if repr(response) == "<Response [404]>" :
                print("404 Error")
            total_length = response.headers.get('content-length')

            if total_length is None:
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('▬' * done, '▭' * (50-done)) )
                    sys.stdout.flush()

    print("\n\n\n\tDownload was compelet...")
mainContent = requests.get(f"https://s1.irdanlod.ir/files/Serial/T/100/S{se}/720p/")
soup = BeautifulSoup(mainContent.text,'lxml')
try:
    for ep in range(ep1,ep2+1):
        download(se,ep)
except OSError:
    print("No space left on Device")
