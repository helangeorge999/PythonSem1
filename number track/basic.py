import requests

def reverse_phone_lookup(9746530848):
    api_key = 'your_api_key'
    url = f'https://api.twilio.com/2010-04-01/Accounts/{api_key}/Lookups/PhoneNumbers/{phone_number}.json'
    response = requests.get(url)
    data = response.json()
    return data

phone_number_info = reverse_phone_lookup('1234567890')
print(phone_number_info)
