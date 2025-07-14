mydata= {"category":[{"A":"FIRST","package":{"data":"2lacs"}},
{"B":"Second","data":{"new":[100]}},{"C":"Third","Tests":[45,75,25]}]};


# Question A : print all keys
# Question B : print count (number of ) keys
# Question 1 : print 2lacs
# Question 2 : print 25
# Question 3 : print 100


all_keys = []

def extract_keys(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            all_keys.append(key)
            extract_keys(value)
    elif isinstance(obj, list):
        for item in obj:
            extract_keys(item)

extract_keys(mydata)

print("All keys:", all_keys)
print("Total number of keys:", len(all_keys))
print(mydata["category"][0]["package"]["data"])
print(mydata["category"][2]["Tests"][2])
print(mydata["category"][1]["data"]["new"][0])
