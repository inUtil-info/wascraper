# wa-scraper-py
## Python functions for using rapidapi's whatsapp scraper

### Overview
wa-scraper-py is a simple implementation for calling rapidapi's wa-scraper service from your python code in a very simple way.
You must be subscribed to the service before at https://rapidapi.com/inutil-inutil-default/api/whatsapp-scraper/ and obtain your apikey.
If you want to test the API before subscribing, use rapidAPI's frontend to discover the free endpoints and to get your temporary token.

This library will work only against the endpoints for subscribed users. Feel free to amend the code to include the token parameter if you need to run free tests from your code.

### About phone numbers
Please ensure you use the right format, that is, including country code but without the + sign before it (e.g, 34605797764)
Remove hyphens, dashes and trim spaces before feeding phone numbers.

**Not valid phone formats**
+34605797764
(34) 34605797764
34-605 797 764

### Library functions & Endpoints

**wa_registered(phone, apikey)**

This function will take phone number and apikey as input and shall return a true/flase boolean response depending on whether the number is registered in the whatsapp network.

**wa_about(phone, apikey)**

This function will take phone number and apikey as input and shall return a json object with the information the phone owner entered as 'status' or 'about' and when was this information added to owner's profile.


**wa_isbiz(phone, apikey)**

This function will take phone number and apikey as input and shall return a true/flase boolean response depending on whether the number is registered as a business account.

**wa_bizinfo(phone, apikey)**

This function will take phone number and apikey as input and shall return a json object with the information the phone owner entered as business informatino details for the account like, e.g., opening times.

** wa_profilepic(phone, apikey,pictype="url", quality="high")**

This function will take phone number and apikey as input, together with two optional parameters:
 - pictype choices are; "url", "png" and "base64". This will determine the data type the function will return.
 - quality choices are "high" and "low", where high is the image the owner uploaded and low is the icon size format of the image.





