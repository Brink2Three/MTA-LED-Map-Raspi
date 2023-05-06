#import requests

#API_KEY = "API KEY HERE"
#URL = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs"

# Set up the request headers with your API key
#headers = {"x-api-key": API_KEY}

# Make a request to the MTA API
#response = requests.get(URL, headers=headers)

#response_text = response.content.decode('utf-8')
#print(response_text)



## Attempt 2 ##
import requests

#response = requests.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs', headers={'x-api-key': 'API KEY HERE'})
#response_text = response.content.decode('utf-8')
#print(response_text)

### Attempt 3 ###
import requests

feed_url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs"

headers = {
    "x-api-key": "API KEY HERE",
    "Content-Type": "application/json"
}

response = requests.get(feed_url, headers=headers)

if response.status_code == 200:
    data = response.content.decode('ISO-8859-1')
    print(data)
else:
    print("Error occurred: ", response.status_code)