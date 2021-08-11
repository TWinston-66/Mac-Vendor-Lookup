import requests
import argparse
from argparse import RawDescriptionHelpFormatter
import json

def lookup(mac, api):
    url = api_list[int(api) - 1]
    r = requests.get(url % mac)
    
    if int(api) == 1:
        result = r.json()
        print(result["result"]["company"])
    elif int(api) == 2:
        result = r.json()
        print(result[0]["company"])
    elif int(api) == 3:
        print(r.text)

macvendorsco = 'http://macvendors.co/api/%s'
macvendorlookup = 'http://www.macvendorlookup.com/api/v2/%s'
macvendors = 'https://api.macvendors.com/%s'

api_num = ['macvendorsco', 'macvendorlookup', 'macvendors']
api_list = [macvendorsco, macvendorlookup, macvendors]

msg = 'Query a choice of three APIs for Mac Address vendor lookup'

parser = argparse.ArgumentParser(description = msg, formatter_class = argparse.RawTextHelpFormatter)
parser.add_argument("-m", "--Mac", help = 'Mac Address')
parser.add_argument("-a", "--Api", help = 'Api Choice...\n1. macvendors.co\n2. macvendorlookup.com\n3. macvendors.com')
args = parser.parse_args()

if args.Mac:
    mac_address = args.Mac
    print('Mac Address: % s' % args.Mac)
else:
    print("Please provide a Mac Address")

if args.Api:
    if int(args.Api) > 4:
        print('Please enter a valid API option' + '\n')
        print('See help menu (-h) for choices')
    else:
        num = int(args.Api)
        api_choice = api_num[num - 1]
        print('Api Choice: ' + api_choice + '\n')
else:
    print('Please provide an API choice')


if args.Mac and args.Api:
    print('Searching...\n')
    lookup(args.Mac, args.Api)