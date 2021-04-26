
import json
import urllib.request
import pprint
import requests


#keys
primary_key = "TyDvr4YhkRER5AyJlIBT12EF6laHBvBJ"
secondary_key = "" 



#something


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    a = urllib.request.urlopen(url)
    response_text = a.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint.pprint(response_data)
    # return response_data


def main():
    """
    You can test all the functions here
    """
    url = f"https://services-qa.walgreens.com/api/products/inventory/v2"
    get_json(url)
    # latitude, longitude = get_lat_long("Babson College")
    # print(latitude, longitude)
    # print(get_nearest_station(latitude, longitude))
    

if __name__ == '__main__':
    main()

