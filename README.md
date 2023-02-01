# wascraper
## Python functions for using inUtil Labs' whatsapp scraper

### Overview
wa-scraper-py is a set python functions for using inUtil Labs' whatsapp-scraper service from your python code, in a very simple way.
You can test its funcionality for free before using the libraries [here](https://rapidapi.com/inutil-inutil-default/api/whatsapp-scraper/). For production use, you must become a subscriber (supporter) of the service and obtain a valid apikey.

You are encouraged to test the service before moving to a paid subscription, use the [playground](https://rapidapi.com/inutil-inutil-default/api/whatsapp-scraper/) to discover the features behind the free endpoints (do not forget to ask for a temporary token).


### Installing and iporting wascraper

1.- Clone this repository locally:

    ```
    git clone https://github.com/inUtil-info/wascraper.git
    ```
    
2.- Install the package with pip or pip3

    ```
    pip3 install -e path/to/wascraper
    ```
    
3.- Import wascraper in your python code

   ```
   from  wascraper import *
   ```
   
  


### About phone numbers
Please make sure you use the right format, as Whatsapp is expecting you include the country code without the + sign before it (e.g, 34605797764)
Remove hyphens, dashes and trim spaces before feeding phone numbers.

**these are some examples of NOT valid phone formats**
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

**wa_profilepic(phone, apikey,pictype="url", quality="high")**

This function will take phone number and apikey as input, together with two optional parameters:
 - pictype choices are; "url", "png" and "base64". This will determine the data type the function will return.
 - quality choices are "high" and "low", where high is the image the owner uploaded and low is the icon size format of the image.

Caling examples:

  wa_profilepic(34605797764,<yourapikey>,"url","low") will return a response object
  wa_profilepic(34605797764,<yourapikey>,"url","high").text will be the url in string format 
  wa_profilepic(34605797764,<yourapikey>,"base64","high") will return a response object
  wa_profilepic(34605797764,<yourapikey>,"base64","high").text will be the base64 coded image in string format.
  wa_profilepic(34605797764,<yourapikey>,"png","high") will return a response object that contains an image buffer on the payload

**wa_picobj(phone, apikey)**

This function recieves the phone to scrap and your apikey and returs a json object listing the objects found in the profile picture of the whatsapp number
The output will be a json object with the list of objects found with the following format:

[{object:"dog", confidence:99.56}, {object:"person", confidence:98.34}]




