from datetime import datetime

# http://www.eurosport.com/_ajax_/story_v8_5/storylist_latest_v8_5.zone?O2=1&langueid=0&dropletid=146&domainid=135&sportid=22&AdPageName=home-sport&RefreshInterval=900&mime=text%2fxml&DeviceType=desktop&datemax=2017-09-20T07:52:40


# http://www.eurosport.com/_ajax_/story_v8_5/storylist_latest_v8_5.zone?O2=1&langueid=0&dropletid=146&domainid=135&sportid=22&AdPageName=home-sport&RefreshInterval=900&mime=text%2fxml&DeviceType=desktop&datemax=2017-09-19T17:44:30


# http://www.eurosport.com/_ajax_/story_v8_5/storylist_latest_v8_5.zone?O2=1&langueid=0&dropletid=146&domainid=135&sportid=22&AdPageName=home-sport&RefreshInterval=900&mime=text%2fxml&DeviceType=desktop&datemin=2017-09-21T19:49:56


# http://www.eurosport.com/_ajax_/story_v8_5/storylist_latest_v8_5.zone?O2=1&langueid=0&dropletid=146&domainid=135&sportid=22&AdPageName=home-sport&RefreshInterval=900&mime=text%2fxml&DeviceType=desktop&datemin=2017-09-20T21:49:56

def constructYFURL(datemax):
    dropletid = 146
    
    domainid = 135
    
    sportid = 22
    
    AdPageName = "home-sport"
    
    RefreshInterval = 900
    
    mime="text%2fxml"
    
    DeviceType="desktop"
    
    datemax = datemax
    yfURL = "http://www.eurosport.com/_ajax_/story_v8_5/storylist_latest_v8_5.zone?O2=1&langueid=0&dropletid="+\
    str(dropletid) + "&domainid="+str(domainid)+"&sportid="+str(sportid)+"&AdPageName="+str(AdPageName)+\
    "&RefreshInterval="+str(RefreshInterval) +"&mime="+str(mime)+"&DeviceType="+str(DeviceType)+\
    "&datemax="+datemax

    return yfURL

def download(filePath,urlOfFile):
    import urllib2

    # We can just use a function from urllib2 to download a url, and save its contents to a
    # local path
    hdr = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Language':'en-US,en;q=0.8',
           'Accept-Encoding':'none',
           'Connection':'keep-alive'}


    webRequest  = urllib2.Request(urlOfFile,headers=hdr)
    #  We'll pass in a header attribute to the webRequest

    # The rest of our code will be enclosed within a try:/except: pair
    # This will act as a safety net in case we encounter some errors when
    # accessing the web urls or working with the files

    try:
        page=urllib2.urlopen(webRequest)
        # save the contents of the web request in a variable called 'content'
        # These are literally the file form the URL (i.e. what you'd get if you
        # downloaded the URL manually

        content=page.read()

        with open(filePath,"wb") as output:
            output.write(bytearray(content))

    # We are simply reading the bytes in content and writing them to our local file.
    # This way we are agnostic to what kind of file we are trying to download ie zip files , csvs,
    # excel etc

    except urllib2.HTTPError, e:
        # Let's print out the error , if any resulted
        print e.fp.read()
        
sometime = "page1"
nseURL = constructYFURL( sometime )
print nseURL

fileName=sometime + ".xml"

import os
localFilePath = os.getcwd()

# localFilePath = "/Users/swethakolalapudi/pytest/"
download(localFilePath+fileName,nseURL)

