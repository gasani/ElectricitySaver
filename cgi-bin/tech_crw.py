import re, csv
from urllib import request
from urllib import parse
from functns import *

def get_new_url(left_part_url, **kwargs):
	inputs  = ['%s=%s' % (k, parse.quote(v)) for k, v in kwargs.items()]
	return request.urlopen(left_part_url.format('&'.join(inputs)))

def get_content(resp):
	return resp.read().decode(resp.headers.get_content_charset()).replace('\n', ' ')

def reformat(string):
	digits = re.search('\d+.?\d+', string)
	return float(digits.group(0)) if digits else string.replace("&nbsp;", "")

def do_search(query):
	
	query = eval(str( query.encode('unicode_escape')).replace('\\\\', '\\')) #неудачная попытка решить проблему с кодировками

	#query = input('Запрос: ') только для теста - здесь будет запрос, взятый из поисковой формы

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

	total_chars, category = [], []

	res_copy = res[:]

	for iteration, item in enumerate(res):

		curr_url = get_new_url('https://www.eldorado.ru/' + item[0])

		url_html = get_content(curr_url)

		sections = ''.join(re.findall("class=['\"]sectionLink['\"]>(.*?)</a", url_html))

		params = None

		with open('lookup.csv', 'r', encoding = 'utf-8', newline='') as csvfile:

			reader = csv.DictReader(csvfile)

			for row in reader:

				if row['\ufeffОбъект'] in sections:

					params = [j.strip() for j in row['Параметры д/выч энергопотр'].split(';')]
					
					category.append(row['\ufeffОбъект'])
					
		if not params:

			del res_copy[ res_copy.index(res[iteration]) ]

			continue
		
		table_of_chars = re.findall('<table>.*?</table>', url_html)[0]

		chars = {i[0]: reformat(i[1]) for i in re.findall('td>([^<]*)</td><td>([^>]*)<', table_of_chars) if i[0] in params }

		total_chars.append(chars)

	model_and_energy = []

	for i in range(len(res_copy)):

		model_and_energy.append( (res_copy[i][1], count_kvth(category[i], **total_chars[i]) ) )

	return model_and_energy

#test
print( do_search('холодильник атлант') )
