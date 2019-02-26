from datetime import timedelta, date, datetime
import random
import string
import requests
import json



r = requests.get('https://api.github.com/events')
print r.content
print "Hello, world!"

start_date = datetime(2019, 2, 20)

for x in range(60*1):

    print x, "," ,

    single_date = start_date + timedelta(minutes=x)
    #print ( single_date.isoformat())

    dt = single_date.strftime("%Y-%m-%d")
    
    #print ( dt)
    
    url = "https://elastic:7FPxC9XsiEEotQD7y2JbvvT5@48bc81b663c64e919e8045ccb4bcbd4d.us-west1.gcp.cloud.es.io:9243/{}-fake/fake".format(dt)
    
    #print url
    
    doc = { "user" : "patriotism.com", 
            "post_date" : single_date.isoformat(),  
            "message" : ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12)) , 
            "x": x,
            "cpu": random.randint(0,100),
            "io": random.randint(0,100)
            
    }
    
    print  json.dumps(doc)
    
    resp = requests.post(url, json=doc)
    
    print resp.text
