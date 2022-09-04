import requests
import lxml
import time
from bs4 import BeautifulSoup
from xlwt import *

# menyiapkan excel worksheet untuk menyimpan hasil crawling
workbook = Workbook(encoding = 'utf-8')
table = workbook.add_sheet('data')
table.write(0, 0, 'url')
table.write(0, 1, 'meta_judul')
table.write(0, 2, 'meta_content')
line=1

page = 1
while page<=12:
    url = "https://cookpad.com/id/cari/masakan%20nusantara?page="+str(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }   

    f = requests.get(url, headers=headers)
    soup = BeautifulSoup(f.content, 'lxml')

    # setiap halaman=====
    resep_list = soup.find_all('li',{'class':'block-link card border-cookpad-gray-400 border-t-0 border-l-0 border-r-0 border-b flex m-0 rounded-none overflow-hidden ranked-list__item xs:border-b-none xs:mb-sm xs:rounded'})
    # setiap resep=====
    for resep in resep_list:
        # mendapat link
        link = resep.find('a')['href']
        table.write(line,0, url+link)

        # mendapat judul
        judul = resep.find('a').get_text()
        table.write(line,1,judul)

        # mendapat content
        content = resep.find('div',{'class':'flex flex-col h-full'})['data-ingredients-highlighter-ingredients-value']
        table.write(line,2, content)
        print('total resep ditambahkan:'+str(line))
        line+=1
    page+=1
    time.sleep(3)

workbook.save('resep_nusantara.xls')
print('selesai')



