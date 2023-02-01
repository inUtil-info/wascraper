from wascraper import *

apikey = "replace_with_your_key"
phone = 34655719560
phone2 = 34645785851


print("Checking if a number is registered")
result = wa_registered(phone, apikey)
print(result)


print("\nFetchig the about information")
result = wa_about(phone, apikey)
print(result)


print("\nChecking if the line correspond to a business account")
result = wa_isbiz(phone, apikey)
print(result)

print("\nGathering the business information from an account")

result = wa_bizinfo(phone, apikey)
print(result)


print("\nGathering the url of some account profile picture")

result = wa_profilepic(phone, apikey).text
print("URL: "+result)

print("\nDetecting objects inside of some account profile picture")

result = wa_picobj(phone2, apikey)
print(result)
