import cgi, ckks, csv

log = ckks.set_cookies()

if log:
	print("""Content-type: text/html\n
<!DOCTYPE html>
<html lang="ru">
	<head>
		<meta charset="windows-1251"><meta http-equiv="refresh" content="0; url=formaction3.py" />\r\n""")
else:
	print("Content-type: text/html\n")
	with open("calculator.html", 'r', encoding = 'utf-8') as f:
		print( f.read().format( log.upper() if log else 'ВХОД', '<li><a href="register.py">РЕГИСТРАЦИЯ</a></li>' if not log else '' ) )