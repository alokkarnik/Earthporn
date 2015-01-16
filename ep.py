import urllib2
import json
import os

url = 'http://www.reddit.com/r/earthporn.json'

obj = urllib2.urlopen(url)

data = json.load(obj)

count = 0

directory = os.getcwd()+"/Images"
if not os.path.exists(directory):
  os.makedirs(directory)
  
for i in data["data"]["children"]:

  imurl = i["data"]["url"]
  try:
  
    print imurl
    
    req = urllib2.Request(imurl+".jpg")

    imgdata = urllib2.urlopen(req).read()
   
    fp = open(("Images/%s"+".jpg") %(i["data"]["title"]) ,"wb")
    fp.write(imgdata)
    fp.close()
    
  except:
    pass
  count = count + 1
  print count

