#!/usr/bin/env python3
import cgi, os
from tech_crw import *
from urllib import parse
import re
from sum_to_pay import sum_to_pay

tarifform = cgi.FieldStorage()
plate = int(tarifform.getfirst("plate"))
water = int(tarifform.getfirst("water"))
people = int(tarifform.getfirst("people"))
rooms = int(tarifform.getfirst("rooms"))
counter = int(tarifform.getfirst("counter"))
action = int(tarifform.getfirst("action"))
n = 85+(50*(people-1))
normals = [[103,64,49,40,35],[133,82,64,52,45],[150,93,72,59,51],[162,101,78,63,55],[153,95,73,60,52],[180,112,87,70,61],[197,122,95,77,67],[209,130,101,82,71],
		   [174,108,84,68,59],[225,139,108,88,76],[255,158,122,99,87],[276,171,132,107,94],[224,139,108,88,76],[265,164,127,103,90],[289,179,139,113,98],[307,191,148,120,105]]
plates = [[3.45,5.98],[3.58,6.88],[1.75,3.59],[3.62,7.18],[3.45,5.98],[1.75,3.59],[2.48,4.31],[2.53,4.96],[1.24,2.59],[2.55,5.17],[2.48,4.31],[1.24,2.59]]


if plate == 1:
	r = plates[:6]
else:
	r = plates[6:]
	

	
if water == 0 and plate == 1: #для квартир с газовыми плитами, без электроводонагревателей
	nr = normals[rooms-1][people-1]
if water == 0 and plate == 0: #для квартир с электроплитами, без электроводонагревателей
	nr = normals[rooms+3][people-1]
if water == 1 and plate == 1: #для квартир с газовыми плитами, с электроводонагревателем
	nr = normals[rooms+7][people-1]
if water == 1 and plate == 0: #для квартир с электроплитами, с электроводонагревателем
	nr = normals[rooms+11][people-1]

#counting expences
energy_and_hours = list()

names = ['tv', 'sound', 'comp', 'pyl', 'coffee', 'stir', 'ut', 'kond', 'vent', 
'tea', 'fridge', 'moroz', 'elpl', 'mwv', 'warm', 'posm', 'mix', 
'tost', 'vyt', 'fen', 'varp', 'dusch', 'vposm', 'mult', 'drl', *[name for name in tarifform.keys() if name.startswith('model')] ]
lamps = ('ln', 'll', 'ls', 'lg')
for fieldname in names:
	tmp = tarifform.getlist(fieldname)
	if tmp:
		energy_and_hours.append( ( float(tmp[0]) * 4, tuple(float(time) for time in tmp[1:]) ) )
for fieldname in lamps:
	tmp = tarifform.getlist(fieldname)
	if tmp:
		energy_and_hours.append( ( float(tmp[0]) * 4 * float(tmp[1]), tuple(float(time) for time in tmp[2:]) ) )


total_sum = None		
if energy_and_hours:
	total_sum = sum_to_pay(energy_and_hours, n, r, nr)
#crw starts
query = tarifform.getfirst("searchfield")
search_res = None
k = 0
if query:
	search_res = do_search(query)
#crw ends

print("Content-type: text/html\n")
print("""<!DOCTYPE html>
<html lang="ru">
	<head>
		<meta charset="windows-1251">
		<title>Калькулятор платы за электроэнергию - Нижний Новгород</title>
		<link rel="stylesheet" href="../css/main.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	<script src="js/jquery.easing.min.js"></script>
	<script src="js/cbpFixedScrollLayout.min.js"></script>
	<script type="text/javascript">
	$(function() {
	$(window).scroll(function() {
	if($(this).scrollTop() != 0) {
	$('#toTop').fadeIn();
	} else {
	$('#toTop').fadeOut();
	}
	});
	$('#toTop').click(function() {
	$('body,html').animate({scrollTop:0},800);
	});
	});
	</script>
	<script>
		$(function() {
			cbpFixedScrollLayout.init();
		});
	</script>	
	</head>
	<body id="top">

	<div class="menu">
	<div class="logo"><a href="index.html"><img height="60px" src="https://pp.userapi.com/c841535/v841535312/4be95/yD1jwSa4X2A.jpg"></a></div>
	
	<div class="nav"><ul>
		<li class="current"><a href="../index.html" >ГЛАВНАЯ</a></li>
		<li><a href="../data.html">ТАРИФЫ И НОРМАТИВЫ</a></li>
        <li><a href="../calculator.html">КАЛЬКУЛЯТОР ЭЛЕКТРОЭНЕРГИИ</a></li>
		<li><a href="../information.html">ПОЛЕЗНАЯ ИНФОРМАЦИЯ</a></li>
            </ul></div>
    </div>	
	<section id="hello">
	</section>
	<div class="wide-block"><table><tr>""")

if action == 1 and counter == 1:
	print("""       <fieldset> 
			<legend><b>УЗНАТЬ ТАРИФ</b></legend>
				<form id="tarifform2" action="firsttarif.py" method="post">
				<p><b>Введите показания счетчика</b></p>
				<p><label><input type="text" name="q"></label></p>""")
				
	if plate == 0 and water == 0:               
		print("""<input type="hidden" name="plate" value=0>
   <input type="hidden" name="water" value=0>""")
	if plate == 0 and water == 1:               
		print("""<input type="hidden" name="plate" value=0>
   <input type="hidden" name="water" value=1>""") 
	if plate == 1 and water == 0:               
		print("""<input type="hidden" name="plate" value=1>
   <input type="hidden" name="water" value=0>""")
	if plate == 1 and water == 1:               
		print("""<input type="hidden" name="plate" value=1>
   <input type="hidden" name="water" value=1>""")
   
	if people == 1:             
		print("""<input type="hidden" name="people" value=1>""")
	if people == 2:             
		print("""<input type="hidden" name="people" value=2>""")
	if people == 3:             
		print("""<input type="hidden" name="people" value=3>""")
	if people == 4:             
		print("""<input type="hidden" name="people" value=4>""")
	if people == 5:             
		print("""<input type="hidden" name="people" value=5>""")

	if rooms == 1:              
		print("""<input type="hidden" name="rooms" value=1>""") 
	if rooms == 2:              
		print("""<input type="hidden" name="rooms" value=2>""")
	if rooms == 3:              
		print("""<input type="hidden" name="rooms" value=3>""")
	if rooms == 4:              
		print("""<input type="hidden" name="rooms" value=4>""")
   
	if counter == 1:                
		print("""<input type="hidden" name="counter" value=1>""") 
	if counter == 2:                
		print("""<input type="hidden" name="counter" value=2>""")
	if counter == 3:                
		print("""<input type="hidden" name="counter" value=3>""")
	if counter == 4:                
		print("""<input type="hidden" name="counter" value=4>""")
   
	print("""               <p><input id="submitinput" class="submit" value="Далее" type="submit" /></p>
				</form>
		</fieldset>""")
		
if action == 1 and counter == 2:
	print("""       <fieldset> 
			<legend><b>УЗНАТЬ ТАРИФ</b></legend>
				<form id="tarifform2" action="secondtarif.py" method="post">
				<p><b>Введите показания счетчика</b></p>
				<p>День:<label><input type="text" name="q_day"></label></p>
				<p>Ночь:<label><input type="text" name="q_night"></label></p>""")
				
	if plate == 0 and water == 0:               
		print("""<input type="hidden" name="plate" value=0>
   <input type="hidden" name="water" value=0>""")
	if plate == 0 and water == 1:               
		print("""<input type="hidden" name="plate" value=0>
   <input type="hidden" name="water" value=1>""") 
	if plate == 1 and water == 0:               
		print("""<input type="hidden" name="plate" value=1>
   <input type="hidden" name="water" value=0>""")
	if plate == 1 and water == 1:               
		print("""<input type="hidden" name="plate" value=1>
   <input type="hidden" name="water" value=1>""")
   
	if people == 1:             
		print("""<input type="hidden" name="people" value=1>""")
	if people == 2:             
		print("""<input type="hidden" name="people" value=2>""")
	if people == 3:             
		print("""<input type="hidden" name="people" value=3>""")
	if people == 4:             
		print("""<input type="hidden" name="people" value=4>""")
	if people == 5:             
		print("""<input type="hidden" name="people" value=5>""")

	if rooms == 1:              
		print("""<input type="hidden" name="rooms" value=1>""") 
	if rooms == 2:              
		print("""<input type="hidden" name="rooms" value=2>""")
	if rooms == 3:              
		print("""<input type="hidden" name="rooms" value=3>""")
	if rooms == 4:              
		print("""<input type="hidden" name="rooms" value=4>""")
   
	if counter == 1:                
		print("""<input type="hidden" name="counter" value=1>""") 
	if counter == 2:                
		print("""<input type="hidden" name="counter" value=2>""")
	if counter == 3:                
		print("""<input type="hidden" name="counter" value=3>""")
	if counter == 4:                
		print("""<input type="hidden" name="conter" value=4>""")
   
	print("""               <p><input id="submitinput" class="submit" value="Далее" type="submit" /></p>
				</form>
		</fieldset>""") 

if action == 1 and counter == 3:
	print("""       <fieldset> 
			<legend><b>УЗНАТЬ ТАРИФ</b></legend>
				<form id="tarifform2" action="thirdtarif.py" method="post">
				<p><b>Введите показания счетчика</b></p>
				<p>Пиковые часы:<label><input type="text" name="q_peak"></label></p>
				<p>Полупиковые часы:<label><input type="text" name="q_semipeak"></label></p>
				<p>Ночь:<label><input type="text" name="q_night"></label></p>""")
				
	if plate == 0 and water == 0:               
		print("""<input type="hidden" name="plate" value=0>
   <input type="hidden" name="water" value=0>""")
	if plate == 0 and water == 1:               
		print("""<input type="hidden" name="plate" value=0>
   <input type="hidden" name="water" value=1>""") 
	if plate == 1 and water == 0:               
		print("""<input type="hidden" name="plate" value=1>
   <input type="hidden" name="water" value=0>""")
	if plate == 1 and water == 1:               
		print("""<input type="hidden" name="plate" value=1>
   <input type="hidden" name="water" value=1>""")
   
	if people == 1:             
		print("""<input type="hidden" name="people" value=1>""")
	if people == 2:             
		print("""<input type="hidden" name="people" value=2>""")
	if people == 3:             
		print("""<input type="hidden" name="people" value=3>""")
	if people == 4:             
		print("""<input type="hidden" name="people" value=4>""")
	if people == 5:             
		print("""<input type="hidden" name="people" value=5>""")

	if rooms == 1:              
		print("""<input type="hidden" name="rooms" value=1>""") 
	if rooms == 2:              
		print("""<input type="hidden" name="rooms" value=2>""")
	if rooms == 3:              
		print("""<input type="hidden" name="rooms" value=3>""")
	if rooms == 4:              
		print("""<input type="hidden" name="rooms" value=4>""")
   
	if counter == 1:                
		print("""<input type="hidden" name="counter" value=1>""") 
	if counter == 2:                
		print("""<input type="hidden" name="counter" value=2>""")
	if counter == 3:                
		print("""<input type="hidden" name="counter" value=3>""")
	if counter == 4:                
		print("""<input type="hidden" name="counter" value=4>""")
   
	print("""               <p><input id="submitinput" class="submit" value="Далее" type="submit" /></p>
				</form>
		</fieldset>""")     
		
if action == 1 and counter == 4:
	total = str(nr*r[0][0]*people)
	print("""<!DOCTYPE HTML>
		<html>
		<head>
			<meta charset="windows-1251">
			<title>Обработка данных форм</title>
		</head>
		<body>
	<p><b>Результаты без счетчика</b></p>""")
	print ("<p>Ваш текущий норматив: {} кВт</p>".format(nr))        
	print ("<p>Сумма к оплате: {} р</p>".format(total))    


if action == 2:

	if counter == 4:
		total = str(nr*r[0][0]*people)
		print("""
	<p><b>Результаты без счетчика</b></p>
	<p><b>У Вас не установлен счетчик. Каждый месяц вы тратите фиксированную сумму</b></p>""")
		print ("<p>Ваш текущий норматив: {} кВт</p>".format(nr))        
		print ("<p>Сумма к оплате: {} р</p>".format(total))    
	else:
		print("""<!DOCTYPE HTML>
			<html>
			<head>
				<meta charset="windows-1251">
				<title>Обработка данных форм</title>
			</head>
			<body>""")
		if total_sum:
			print ("<p>При таком использовании в месяц вы потратите: {} р</p>".format(total_sum))
		print ("""<fieldset> 
				<legend><b>Электроприборы</b></legend>""")
			#crw starts
		print("""<form id="searchform" action="" method="get" enctype="text/plain">
	<input type="text" name="searchfield" value="">""")
		for fieldn in ('plate', 'water', 'people', 'rooms', 'counter', 'action'):
			print("""
	<input type='hidden' name="{}" value="{}">
	""".format(fieldn, tarifform.getfirst(fieldn)) )
		print("""<input type="submit" class="submit" value="Искать"></form>""")
			#crw ends
		
		print("""<form id="tarifform1" action="" method="post">
					<p><b>Отметьте электроприборы, которые вы используете дома, укажите средние часы их использования днем и ночью за недельный период:</b></p>
					<p><label width = "40%"><input type="radio" name="tv" value=0.18>Телевизор:   {}</label>
					<p><label><input type="radio" name="sound" value=0.1>Акустическая система:   {}</label>
					<p><label><input type="radio" name="comp" value=0.6>Компьютер:   {}</label>
					<p><label><input type="radio" name="pyl" value=1>Пылесос:   {}</label>
					<p><label><input type="radio" name="coffee" value=0.8>Кофемашина:   {}<input type="text" name=coffee" value=""></label></p>
									
					<p><label><input type="radio" name="stir" value=3.3>Стиральная машина:   {}</label>
					<p><label><input type="radio" name="ut" value=1>Утюг:   {}</label>
					<p><label><input type="radio" name="kond" value=1.5>Кондиционер:   {}</label>
					<p><label><input type="radio" name="vent" value=2>Тепловентилятор:   {}</label>
					<p><label><input type="radio" name="tea" value=1>Чайник:   {}</label></p>
					
					<p><label><input type="radio" name="fridge" value=0.2>Холодильник:   {}</label>
					<p><label><input type="radio" name="moroz" value=0.2>Морозильная камера:   {}</label>
					<p><label><input type="radio" name="elpl" value=2.5>Электрическая плита:   {}</label>
					<p><label><input type="radio" name="mwv" value=1>Микроволновая печь:   {}</label>
					<p><label><input type="radio" name="warm" value=11>Обогреватель:   {}</label></p>

					<p><label><input type="radio" name="posm" value=2>Посудомоечная машина:   {}</label>
					<p><label><input type="radio" name="mix" value=0.2>Миксер:   {}</label>
					<p><label><input type="radio" name="tost" value=1.3>Тостер:   {}</label>
					<p><label><input type="radio" name="vyt" value=0.21>Вытяжка:   {}</label>
					<p><label><input type="radio" name="fen" value=0.8>Фен:   {}</label></p>

					<p><label><input type="radio" name="varp" value=1.5>Варочная панель:   {}</label>
					<p><label><input type="radio" name="duhsh" value=3.5>Духовой шкаф:   {}</label>
					<p><label><input type="radio" name="vposm" value=3.5>Встроенная посудомойка:   {}</label>
					<p><label><input type="radio" name="mult" value=1>Мультиварка:   {}</label>
					<p><label><input type="radio" name="drl" value=0.25>Дрель:   {}</label></p>
	 """.format( *['<input type="text" value="" name="{}">'.format(mtype) * counter for mtype in names ] ) )
			#crw starts
		if search_res:
			print("<p>")
			for index, item in enumerate(search_res):
						print("""<label><input type="radio" name="model{}" value={}>{}{}</label>""".format(index, *item[::-1], '<input type="text" name="model{}" value="">'.format(index) * counter ))
			print("</p>")
			#crw ends
		print("""</fieldset>
					<fieldset><legend><b>Освещение</b></legend><p><b>Выберите типы лампочек, которые вы используете для освещения, укажите их количество и средние часы их использования днем и ночью за недельный период:</b></p>
					<p><label><input type="radio" name="ln" value=0.1>Лампа накаливания:   <input type="text" name="ln" value="">{}</label>
					<p><label><input type="radio" name="ll" value=0.078>Люминисцентная:   <input type="text" name="ll" value="">{}</label>
					<p><label><input type="radio" name="ls" value=0.042>Энергосберегающая:   <input type="text" name="ls" value="">{}</label>
					<p><label><input type="radio" name="lg" value=0.22>Галогенная:   <input type="text" name="lg" value="">{}</label></p></fieldset>""".format( *['<input type="text" value="" name="{}">'.format(mtype) * counter for mtype in lamps ] ))             
		print("""<input type="hidden" name="plate" value={}>
	   <input type="hidden" name="water" value={}>""".format(plate, water))
		print("""<input type="hidden" name="people" value=1><input type="hidden" name="rooms" value={}>""".format(people, rooms) )           
		print("""<input type="hidden" name="counter" value={}>""".format(counter) )               
					
		print("""       <p><button type="submit" />Рассчитать</button></p>
					</form>
			</fieldset>""")
print ("""</tr></table></div>
	<div class="description"><p class="big header">ГРАФИК ПЛАНОВЫХ ОТКЛЮЧЕНИЙ</p>
	<p class = "text narrow">Ура! Теперь можно изучить график плановых отключений электроэнергии, найти в нем свой дом и<br> заранее подготовиться к неизбежному</p>
	<br><a href="information.html#plans"><div class="btt red middle">ПОСМОТРЕТЬ ГРАФИК</div></a></div>

	<footer class="main-footer">
	<div class="social">
    <a href="https://facebook.com" class="social-btn"><img src="http://ipic.su/img/img7/fs/social_icons_v2_graphicsland(1).1513735484.png" width="25" alt="facebook"></a>   <a href="https://twitter.com" class="social-btn"><img src="http://ipic.su/img/img7/fs/social_icons_v2_graphicsland(2).1513735518.png" width="25" alt="twitter"></a>  <a href="https://vk.com" class="social-btn"><img src="http://ipic.su/img/img7/fs/social_icons_v2_graphicsland.1513735562.png" width="25" alt="вконтакте"></a>  <a href="web.telegram.org" class="social-btn"><img src="http://ipic.su/img/img7/fs/social_icons_v2_graphicsland(3).1513735587.png" width="25" alt="telegram"></a>  <a href="ok.ru" class="social-btn"><img src="http://ipic.su/img/img7/fs/social_icons_v2_graphicsland(4).1513735651.png" width="25" alt="одноклассники">
	</div>
	<a href="https://vk.com/justdfour"><p class="cop">
	pictures by justdfour © 2017
	</p></a>
</footer></div>
<div ID = "toTop"><img height="15px" width="15px" src="https://cdn3.iconfinder.com/data/icons/faticons/32/arrow-up-01-512.png"></div>
 </body>
</html>""")		
