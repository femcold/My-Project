import requests
from bs4 import BeautifulSoup

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
    
for url in urls:
    page = requests.get( url )
    soup = BeautifulSoup(page.text, 'html.parser')
    html = soup.findAll("div", class_='storyfull__container')
    print html
    print "=" * 50
#     t = (id,GSID,cell.text,cell['href'])