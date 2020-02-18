import requests
import pprint
import sys
import json
import time
l=[]
#for card_no in sys.argv[1:]:

#    r=requests.get('https://lookup.binlist.net/'+card_no, headers={'Accept-Version': "3"})

#    if 200<=r.status_code<=299:
#        pprint.pprint(r.json())



with open('card1.json') as f:
    cards=json.load(f)
    for card in cards:
        card_no=str(card['CreditCard']['CardNumber'])[0:8]
#        print(card_no)
        c = requests.get('https://lookup.binlist.net/' + card_no, headers={'Accept-Version': "3"})
#        print(c.status_code)
#        print(c.text)
        if 200<=c.status_code<=299:
#           pprint.pprint(c.json())
            l.append(c.json()['bank']['name'])
            time.sleep(0.3)

for y in sorted(sorted(set(l))):
    print(y)





