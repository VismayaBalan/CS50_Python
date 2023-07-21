import sys
import requests

if len(sys.argv) < 2:
    sys.exit('Missing command-line argument')

n = sys.argv[1]

try:
    bitcoin = float(n)

except ValueError:
    sys.exit('Command-line argument is not a number')



try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = r.json()
except requests.RequestException:
    print('error')
else:
    price = data['bpi']['USD']['rate_float']
    print(f"${price *float(n):,.4f}")
