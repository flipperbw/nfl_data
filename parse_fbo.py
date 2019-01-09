import requests
from bs4 import BeautifulSoup
from time import sleep

print 'Player|Team|Position|Started|Total Snaps|Off Snaps|Off Snap Pct|Def Snaps|Def Snap Pct|ST Snaps|ST Snap Pct|Week|Year'

for y in ('2016', '2015', '2014', '2013', '2012'):
    for w in range(1,17):
        data = {'team': 'ALL', 'week': str(w), 'pos': 'ALL', 'year': str(y), 'Submit': 'Submit'}
        headers = {'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36', 'Referer': 'http://www.footballoutsiders.com/stats/snapcounts'}
        q = requests.post('http://www.footballoutsiders.com/stats/snapcounts', data=data, headers=headers)
        
        qt = q.text
        b = BeautifulSoup(qt, "lxml")
        bt = b.find(id='dataTable')
        
        trs = bt.find_all('tr')
        for t in trs[1:]:
            tds = t.find_all('td')
            td_list = [td.text for td in tds]
            td_list.append(str(w))
            td_list.append(str(y))
            
            td_str = '|'.join(td_list)
            
            print(td_str)

        sleep(1.5)
