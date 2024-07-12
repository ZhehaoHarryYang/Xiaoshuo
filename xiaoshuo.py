# how to send request
# pip install requests
import requests
# pip install lxml
from lxml import etree

# send to which url
url = 'https://dl.131437.xyz/book/douluodalu2/611.html'

while True:
    # camouflage
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    # send request
    resp = requests.get(url, headers = headers)
    # code
    resp.encoding = 'utf-8'

    # respond
    e = etree.HTML(resp.text)
    info = '\n'.join(e.xpath('//div[@class="m-post"]/p/text()'))
    title = e.xpath('//h1/text()')[0]
    url = f'https://dl.131437.xyz/{e.xpath("//tr/td[2]/a/@href")[0]}'
    #print(info)
    print(title)
    # save data
    #with open('Douluo.txt', 'a', encoding='utf-8') as f:
    #    f.write(title + '\n\n' + info + '\n\n')
    # end of list
    #if url == "https://dl.131437.xyz/book/douluodalu2/":
    #   break