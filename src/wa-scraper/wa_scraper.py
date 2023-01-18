import requests

# refustered function returns a boolean value
def wa_registered(phone, apikey):
    url = "https://whatsapp-scraper.p.rapidapi.com/wchk"        
    querystring = {"phone":phone}
    headers = {
	    "X-RapidAPI-Key": apikey,
	    "X-RapidAPI-Host": "whatsapp-scraper.p.rapidapi.com"
    }
    return bool(requests.request("GET", url, headers=headers, params=querystring).json())

# about function returns a json object
def wa_about(phone, apikey):
    url = "https://whatsapp-scraper.p.rapidapi.com/about"        
    querystring = {"phone":phone}
    headers = {
	    "X-RapidAPI-Key": apikey,
	    "X-RapidAPI-Host": "whatsapp-scraper.p.rapidapi.com"
    }
    return requests.request("GET", url, headers=headers, params=querystring).json()

# Isbiz returns a boolean value
def wa_isbiz(phone, apikey):
    url = "https://whatsapp-scraper.p.rapidapi.com/isbiz"        
    querystring = {"phone":phone}
    headers = {
	    "X-RapidAPI-Key": apikey,
	    "X-RapidAPI-Host": "whatsapp-scraper.p.rapidapi.com"
    }
    return bool(requests.request("GET", url, headers=headers, params=querystring).json())

# Bizinfo returns a json object
def wa_bizinfo(phone, apikey):
    url = "https://whatsapp-scraper.p.rapidapi.com/bizinfo"        
    querystring = {"phone":phone}
    headers = {
	    "X-RapidAPI-Key": apikey,
	    "X-RapidAPI-Host": "whatsapp-scraper.p.rapidapi.com"
    }
    return requests.request("GET", url, headers=headers, params=querystring).json()

# Valid values for pictype are 'url', 'base64' and 'png'.
# Valid values for quality are 'high' and 'low'
def wa_profilepic(phone, apikey,pictype="url", quality="high"):
    url = "https://whatsapp-scraper.p.rapidapi.com/wspicture"        
    querystring = {"phone":phone,"pictype":pictype,"quality":quality}
    headers = {
	    "X-RapidAPI-Key": apikey,
	    "X-RapidAPI-Host": "whatsapp-scraper.p.rapidapi.com"
    }
    return requests.request("GET", url, headers=headers, params=querystring)
