import cgi, ckks, csv

loginform = cgi.FieldStorage()

log = ckks.set_cookies()
				
if log:
	print("Content-type: text/html\n")	
	print("""<!DOCTYPE HTML>
			<html>
			<head>
				<meta charset="windows-1251"><meta http-equiv="refresh" content="5; url=/../index.html" /><title>Вход</title>
				</head>
				<body>""")
	print("""Вы уже вошли в систему</body></html>""")
	
	
else:

	log, pswd = loginform.getvalue("login"), loginform.getvalue("pswd")
		

	if log and ckks.validation(log, pswd):
	
		ckks.set_cookies(log)
		print("Content-type: text/html\n")	
		print("""<!DOCTYPE HTML>
			<html>
			<head>
				<meta charset="windows-1251">
				<meta http-equiv="refresh" content="5; url=/../index.html" /><title>Вход</title></head>""")

	else:
		print("Content-type: text/html\n")	
		print("""<!DOCTYPE HTML>
			<html>
			<head>
				<meta charset="windows-1251">""")
	
		print("""<title>Вход</title>
				</head>
				<body>""")
		print("""<form action="" method="post">
					<p><b>Введите логин и пароль:</b></p>
					<p>Логин:<label><input type="text" name="login" required></label></p>
					<p>Пароль:<label><input type="text" name="pswd" required></label></p>
					<input id="submitinput" class="submit" value="Далее" type="submit" />
					</form></body></html>""")