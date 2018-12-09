import requests
import xml.etree.ElementTree as ET
import xmltodict, json
from collections import OrderedDict


headers = {
    'Authorization': 'Bearer 1a0894b4-fa7e-48ff-8d1c-87d60cb64f6b',
    'Content-Type': 'application/xml'
}

xml_file = "AirShopping.xml"

with open(xml_file) as xml:
    r = requests.post('https://18.130.255.52:9002/ndc171webservices/v171/airshopping?site=airline',
                      headers=headers,
                      verify=False, data=xml)



print(r.status_code)

print(r.content)

r = xmltodict.parse(r.content)
# print(r)
json.dumps(r)
# print(r)

r = r.get('AirShoppingRS')
print(r)

r = dict(r)
print(r)

# arr = []

try:
    for i, k in enumerate(r.items()):
        print(i, k)
        if i == 4 and k[0] == 'Errors':
            k = k[1]['Error']['@ShortText']
            print(k)
            break
        elif i == 5 and k[0] == 'Success':
            print(k[0])

        if i == 7:
            tmp_k = k[1]['AllOffersSnapshot']
            print(str(tmp_k))

            tmp_k = k[1]['AirlineOffers']['Offer']

            arr = [dict() for _ in range(len(tmp_k))]
            print(arr)

            for n in range(len(tmp_k)):
                print(tmp_k[n])

        if i == 8:
            tmp_k = k[1]['FlightSegmentList']['FlightSegment']

            print(tmp_k)

            for n in range(len(tmp_k)):
                print(tmp_k[n])
except:
    print('Something went wrong.')

