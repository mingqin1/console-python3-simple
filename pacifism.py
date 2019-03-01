
from datetime import timedelta, date, datetime
import random
import string
import requests
import json



r = requests.get('https://api.github.com/events')
print r.content
print "Hello, world!"

start_date = datetime(2019, 2, 21)

for x in range(60*96):

    print x, "," ,

    single_date = start_date + timedelta(minutes=x)
    #print ( single_date.isoformat())

    dt = single_date.strftime("%Y-%m-%d")
    
    #print ( dt)
    
    url = "https://search-smart-vbwh2ra2j72z3f64p5rbhec6ba.us-east-1.es.amazonaws.com/{}-fake/fake".format(dt)
    
    #print url
    
    doc = { "user" : "pacifism.com", 
            "post_date" : single_date.isoformat(),  
            "message" : ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12)) , 
            "x": x,
            "cpu": random.randint(0,100),
            "io": random.randint(0,100)
            
    }
    
    print  json.dumps(doc)
    
    resp = requests.post(url, json=doc)
    
    print resp.text 
