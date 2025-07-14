mydata = [{"states":["GUJARAT","RAJASTHAN",{"PORTION":"WESTINDIA"},
        {"LANGUAGES":["GUJARATI","MARWADI",["HINDI","ENGLISH"]]}]},
        {"CODES":{"GUJARAT":"GJ","RAJASTHAN":"RJ"}},["7.07 CR","8.5CR"]];


# 1) PRINT TOTAL NUMBER OF MAIN KEYS = 0
# 2) PRINT NAME OF ALL MAIN KEYS = X
# 3) PRINT GJ
# 4) PRINT GUJARAT
# 5) PRINT MARWADI
# 6) PRINT ENGLISH
# 7) PRINT WEST INDIA
# 8) PRINT 7.07 CR

all_key = []
def extract_keys(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            all_key.append(key)
            extract_keys(value)
    elif isinstance(obj, list):
        for item in obj:
            extract_keys(item)

extract_keys(mydata)


X = []
for item in mydata:
    if isinstance(item, dict):
        for key in item.keys():
            X.append(key)



print("All keys:", all_key)
print("Main keys = X:", X)
print(mydata[1]["CODES"]["GUJARAT"])
print(mydata[0]["states"][0])
print(mydata[0]["states"][3]["LANGUAGES"][1])
print(mydata[0]["states"][3]["LANGUAGES"][2][1])
print(mydata[0]["states"][2]["PORTION"])
print(mydata[2][0])
