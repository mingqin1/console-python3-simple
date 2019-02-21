from datetime import timedelta, date, datetime
import random
import string
import requests
import json

start_date = datetime(2019, 2, 20)

for x in range(60*1):
    print (x, ", ",)
    single_date = start_date + timedelta(minutes=x)
    dt = single_date.strftime("%Y-%m-%d")
    doc = { "user" : "patriotism.com", 
            "post_date" : single_date.isoformat(),  
            "message" : ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12)) , 
            "x": x,
            "cpu": random.randint(0,100),
            "io": random.randint(0,100)
            
    }
    
    print ( json.dumps(doc))

#r = requests.get('https://api.github.com/events')
#print(r.content)
print("Hello, world!")
