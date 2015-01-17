import urllib2
import json
import os

#URL of the EarthPorn JSON
url = 'http://www.reddit.com/r/earthporn.json' 

#initialize the object of the irl
obj = urllib2.urlopen(url)

#Get the JSON data
data = json.load(obj)

#Counter for counting the number of links
count = 0

#Path for current PWD to save Images
directory = os.getcwd()+"/Images"

#Check if Directory alredy exists, If not then create a NEW dir
if not os.path.exists(directory):
  os.makedirs(directory)
  
#Loop through the JSON URLs
for i in data["data"]["children"]:

  imurl = i["data"]["url"]
  try:
  
    print imurl
    
    #Request the Full URL
    req = urllib2.Request(imurl+".jpg")
    
    #Get the Data in the URL
    imgdata = urllib2.urlopen(req).read()
   
    #Create a new image file and write to it
    fp = open((directory + "/%s"+".jpg") %(i["data"]["title"]) ,"wb")
    fp.write(imgdata)
    fp.close()
    
  except:
    pass
    
  count = count + 1
  
  print count
