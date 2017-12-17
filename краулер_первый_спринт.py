import re
from urllib import request
from urllib import parse

def get_new_url(left_part_url, **kwargs):
    inputs  = ['%s=%s' % (k, parse.quote(v.encode('cp1251'))) for k, v in kwargs.items()]
    return request.urlopen(left_part_url.format('&'.join(inputs)))

def get_content(resp):
    return resp.read().decode(search_url.headers.get_content_charset()).replace('\n', ' ')

query = input('Запрос: ')

search_url = get_new_url('https://www.eldorado.ru/search/catalog.php?{}', q = query, PAGEN_SEARCH = '1')

url_html = get_content(search_url)

try:
    
    pages = int(re.findall("<a class=[\"']page[\"'][^>]*>(\d+)", url_html)[-1])
    
except IndexError: #1 page or 0 results

    pages = 1

res = re.findall("<div class=[\"']itemTitle[\"']><a href=[\"']([^\"']*)[\"']>(.*?)</a", url_html)

for page in range(2, pages + 1):
    
    search_url = get_new_url('https://www.eldorado.ru/search/catalog.php?{}', q = query, PAGEN_SEARCH = str(page) )

    url_html = get_content(search_url)
    
    res += re.findall("<div class=[\"']itemTitle[\"']><a href=[\"']([^\"']*)[\"']>(.*?)</a", url_html)

#retrieve information from product page

total_chars = []

for iteration, item in enumerate(res):

    curr_url = get_new_url('https://www.eldorado.ru/' + item[0])

    url_html = get_content(curr_url)

    table_of_chars = re.findall('<table>.*?</table>', url_html)[0]

    chars = re.findall('td>([^<]*)</td><td>([^>]*)<', table_of_chars)

    total_chars.append(chars)


for i in range(len(res)):

    print( '{} : {}'.format(res[i][1], total_chars[i]) )


