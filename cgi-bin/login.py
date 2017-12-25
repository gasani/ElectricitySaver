import fileinput, sys, cgi, ckks, csv

loginform = cgi.FieldStorage()

log = ckks.set_cookies()
header = """Content-type: text/html\n
<!DOCTYPE html>
<html lang="ru">
	<head>
		<meta charset="windows-1251">
		<title>Законы и формулы - Электрономия Нижний Новгород</title>
		<link rel="stylesheet" href="../css/main.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	<script src="js/jquery.easing.min.js"></script>
	<script src="js/cbpFixedScrollLayout.min.js"></script>
	<script type="text/javascript">
	$(function() {{
	$(window).scroll(function() {{
	if($(this).scrollTop() != 0) {{
	$('#toTop').fadeIn();
	}} else {{
	$('#toTop').fadeOut();
	}}
	}});
	$('#toTop').click(function() {{
	$('body,html').animate({{scrollTop:0}},800);
	}});
	}});
	</script>
	<script>
		$(function() {{
			cbpFixedScrollLayout.init();
		}});
	</script>	
	</head>
	<body id="top">

	<div class="menu">
	<div class="logo"><a href="index.html"><img height="60px" src="https://pp.userapi.com/c841535/v841535312/4be95/yD1jwSa4X2A.jpg"></a></div>
	
	<div class="nav"><ul>
		<li><a href="data.py?p=index" >ГЛАВНАЯ</a></li>
		<li><a class="current" href="data.py?p=data">ТАРИФЫ И НОРМАТИВЫ</a></li>
        <li><a href="calculator.py">КАЛЬКУЛЯТОР ЭЛЕКТРОЭНЕРГИИ</a></li>
		<li><a href="data.py?p=information">СПРАВОЧНАЯ ИНФОРМАЦИЯ</a></li>
		<li><a href="login.py">{}</a></li>
		{}
            </ul></div>
    </div>
	<section id="hello">
	</section>
	<div class="wide-block"><table><tr>""".format( log.upper() if log else 'ВХОД', '<li><a href="register.py">РЕГИСТРАЦИЯ</a></li>' if not log else '' ) 
	
		
if log:

	if loginform.getvalue("change"):
	
		values = [int(loginform.getvalue(val)) for val in ('plate', 'water', 'people', 'rooms', 'counter')]

		with open('userdb.csv', 'r+', encoding = 'utf-8') as csvfile:
		
			reader = csv.reader(csvfile)
			
			seen = []
			
			for row in reader:
			
				if row and row[0] == log:
					
					pswd = row[1]
				
				elif row:
					
					seen.append(row)
			csvfile.seek(0)
			csvfile.truncate()
					
			writer = csv.writer(csvfile) 
				
			for row in seen:
				
				writer.writerow(row)
				
			writer.writerow([log, pswd, *values ])
			
		plate, water, people, rooms, counter = values
				
				
	else:
	
		with open('userdb.csv', 'r', encoding = 'utf-8') as csvfile:
			
			reader = csv.reader(csvfile)
				
			for row in reader:
				
				if row and row[0] == log:
					
					plate, water, people, rooms, counter = map(int, row[2:])
	print(header)			
	print("""<form action="" method="post">
					<fieldset>
	<p class="header"><b>Ваш тип плиты:</b></p>
						<p class="textform"><label class="labelform"><input type="radio" name="plate" value=0 {}>Электричество</label>
						<label class="labelform"><input type="radio" name="plate" value=1 {}>Газ</label></p>
						<p class="header"><b>У Вас есть электроводонагреватель?</b></p>
						<p class="textform"><label class="labelform"><input type="radio" name="water" value=1 {}>Есть</label>
						<label class="labelform"><input type="radio" name="water" value=0 {}>Нет</label></p>
						<p class="header"><b>Количество зарегистрированных жильцов</b></p>
						<p class="textform"><label class="labelform1"><input type="radio" name="people" value=1 {}>1</label>
						<label class="labelform1"><input type="radio" name="people" value=2 {}>2</label>
						<label class="labelform1"><input type="radio" name="people" value=3 {}>3</label>
						<label class="labelform1"><input type="radio" name="people" value=4 {}>4</label>
						<label class="labelform1"><input type="radio" name="people" value=5 {}>5+</label></p>
						<p class="header"><b>Количество жилых комнат</b></p>
						<p class="textform"><label class="labelform1"><input type="radio" name="rooms" value=1 {}>1</label>
						<label class="labelform1"><input type="radio" name="rooms" value=2 {}>2</label>
						<label class="labelform1"><input type="radio" name="rooms" value=3 {}>3</label>
						<label class="labelform1"><input type="radio" name="rooms" value=4 {}>4</label></p>
						<p class="header"><b>Укажите тип счетчика</b></p>
						<p class="textform"><label class="labelform2"><input type="radio" name="counter" value=1 {}>Одноставочный</label>
						<label class="labelform2"><input type="radio" name="counter" value=2 {}>Двухставочный</label>
						<label class="labelform2"><input type="radio" name="counter" value=3 {}>Трехставочный</label>
						<label class="labelform2"><input type="radio" name="counter" value=4 {}>Нет счетчика</label>
						<input type='hidden' value='change' name='change'>
						<p><input id="submitinput" class="submit" value="Сохранить" type="submit" /></p>
	</fieldset>
					</form></tr></table></div></body></html>""".format( *('checked' if val else '' for val in [*[x == plate for x in range(2)],  *[x != water for x in range(2)], *[x == people for x in range(1,6)],
	*[x == rooms for x in range(1,5)], *[x == counter for x in range(1,5)] ] ) ))
	
	
	
	
else:

	log, pswd = loginform.getvalue("login"), loginform.getvalue("pswd")
		

	if log and ckks.validation(log, pswd):
	
		ckks.set_cookies(log)
		print("""Content-type: text/html\n
<!DOCTYPE html>
<html lang="ru">
	<head>
		<meta charset="windows-1251"><meta http-equiv="refresh" content="0; url=login.py" />\r\n""")

	else:
		print(header)
		print("""<div class="wide-block"><form action="" method="post">
					<p><b>Введите логин и пароль:</b></p>
					<p>Логин:<label><input type="text" name="login" required></label></p>
					<p>Пароль:<label><input type="text" name="pswd" required></label></p>
					<input id="submitinput" class="submit" value="Далее" type="submit" />
					</form></div></body></html>""")