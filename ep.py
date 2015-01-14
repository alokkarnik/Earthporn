import urllib2
import json

url = 'http://www.reddit.com/r/earthporn.json'

obj = urllib2.urlopen(url)

data = json.load(obj)

#print json.dumps(data, sort_keys = True, indent = 4)
count = 0

for i in data["data"]["children"]:

  imurl = i["data"]["url"]
  try:
    
    #if "jpg" not in str(imurl) or "jpeg" not in str(imurl):
      #imurl = imurl + ".jpg"
    
    print imurl
    
    req = urllib2.Request(imurl+".jpg")

    imgdata = urllib2.urlopen(req).read()
   
    fp = open(("%s"+".jpg") %(i["data"]["title"]) ,"wb")
    fp.write(imgdata)
    fp.close()
    
  except:
    pass
  count = count + 1
  print count

