import csv	
def set_cookies(lgn = None):
	"""Для разработчицы сайта: 
Загружает и сохраняет куки (логин пользователя). В form передавать переменную только в том случае,
если пользователь находился на странице входа или регистрации, отправил данные и они прошли валидацию
(т.е. когда нужно создать новые куки). В form передается переменная с формой типа tarifform из tariffunction.py,
только в нашем случае это будут формы логина или регистрации.
Результат работы сохранить в новую переменную - это будет логин пользователя (строка) или None.
Запускать во всех скриптах перед print content-type.
Файл сохранить в директорию со всеми скриптами (cgi-bin), перед тем как вызывать, функцию нужно импортировать: from ckks import set_cookies"""
	import http.cookies
	from os import environ
	cookie = http.cookies.SimpleCookie(environ.get("HTTP_COOKIE"))
	login = cookie.get("login")
	if login:
		return login.value
	else:
		if lgn:
			print("Set-cookie: login={}; expires=Wed May 18 03:33:20 2033; path=/cgi-bin/ ".format(lgn))
		return

def validation(login, pswd):
	with open('userdb.csv', 'r', encoding = 'utf-8') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			if row and row[0] == login and row[1] == pswd:
				return True
	return False