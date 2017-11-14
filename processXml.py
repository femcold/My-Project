import requests
from bs4 import BeautifulSoup
import random as random
import time

infile = open("srcpage1.xml","r")
contents = infile.read()
soup = BeautifulSoup(contents,'xml')

storylist_latest = cells=soup.findAll("div", class_='storylist-latest__main-title None')

print len( storylist_latest )
print ( storylist_latest )

urls = []
for story in storylist_latest:
    # print story.a.get_text()
    urls.append("http://www.eurosport.com" + story.a['href'])
print urls
# 

record_i = 0

for url in urls:
    page = requests.get( url )
    soup = BeautifulSoup(page.text, 'html.parser')
    html = soup.findAll("div", class_='storyfull__container')
    print html
    print "=" * 50
    if record_i % 50 == 0:
        ticker = random.randrange(300, 400, 2)
        print "sleeping for %s" % (ticker)
        time.sleep(ticker)
    elif record_i % 20 == 0:
        ticker = random.randrange(180, 300, 2)
        print "sleeping for %s" % (ticker)
        time.sleep(ticker)
    elif record_i % 4 == 0:
        ticker = random.randrange(60, 121, 2)
        print "sleeping for %s" % (ticker)
        time.sleep(ticker)
    else:
        ticker = random.randrange(25, 50, 2)
        print "sleeping for %s" % (ticker)
        time.sleep(ticker)
        
#     t = (id,GSID,cell.text,cell['href'])