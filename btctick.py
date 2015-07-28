import urllib2 as ul2
import json
import sys


url = 'https://blockchain.info/ticker'
val = ul2.urlopen (url).read ()
js = json.loads (val)

if len (sys.argv) > 1 and sys.argv[1] in js:
    currency = sys.argv[1]
else:
    currency = 'USD'

print (str (js[currency]['last']) + js[currency]['symbol'] + ' = 1BTC')
