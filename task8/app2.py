mydata= {
"maharashtra":{"mumbai":{"city":"metro city","metro":"yes"},
"population":"20 cr"},
"gujarat": ["AHMEDABAD","SURAT","RAJKOT"],
"rajasthan":["AJMER","JAISALMER",{"capital":"jaipur"},["MEWAD","RJ","INR"]]
}

# Question A : print all keys
# Question B : print count (number of ) keys
# Question 1 : print metro city
# Question 2 : print jaipur
# Question 3 : print Rajkot
# Question 4 : print RJ


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
print(mydata["maharashtra"]["mumbai"]["city"])
print(mydata["rajasthan"][2]["capital"])
print(mydata["gujarat"][2])
print(mydata["rajasthan"][3][1])