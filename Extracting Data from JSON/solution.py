import urllib.request, urllib.parse
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
# serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

url = "http://py4e-data.dr-chuck.net/comments_42.json" # sample url
url = "http://py4e-data.dr-chuck.net/comments_2003853.json" # actual url

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

# print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

try:
    js = json.loads(data)
except:
    js = None

# print(json.dumps(js, indent=4))

sum = 0

for item in js['comments']:
    # print('Name:', item['name'])
    # print('Count:', item['count'])
    sum += int(item['count'])

print('\t',len(js['comments']), 'users commented with a total number of',sum, 'comments.')