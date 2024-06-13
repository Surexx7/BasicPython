#dict_name = {key, value}
#Dictonary is ordered
#Dictanary is mutuable(Only value can be changed)
#Key should be unique
#Value can be of any data types

phone_no={"Ram ": 9843,
          "Shyam" :98567,
          "Mohan":946473
          }
print(phone_no["Shyam"])

phone_no=dict([("Ram", 1234), ("Shyam",3457),("Mohan",89342)])
print(phone_no)


#Updating Dictionary

phone_no["Ram"]=7765
print(phone_no)
phone_no["Shyam"]={"Shyam_home": 9999},{"Office_phone":96758}
print(phone_no)
print(phone_no["Shyam"])
print(phone_no["Shyam"],["Office_phone"])


#Get Method

print(phone_no.get("Ram"))

#Deleting
del phone_no["Ram"]
print(phone_no)
print(phone_no.keys())
print(phone_no.values())
print(phone_no.items())

for i in phone_no.items():
    print(i)

phone_no2=phone_no.copy()
print(phone_no2)