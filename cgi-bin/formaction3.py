#!/usr/bin/env python3
import cgi, os
import numpy
tarifform = cgi.FieldStorage()
plate = int(tarifform.getfirst("plate"))
water = int(tarifform.getfirst("water"))
people = int(tarifform.getfirst("people"))
rooms = int(tarifform.getfirst("rooms"))
counter = int(tarifform.getfirst("counter"))
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
		<li><a href="login.py">ВХОД</a></li>
		<li><a href="register.py">РЕГИСТРАЦИЯ</a></li>
            </ul></div>
    </div>	
	<section id="hello">
	</section>
	<div class="wide-block"><table><tr>
	<fieldset><img src="../img/4.png" width="100%"></fieldset>""")		

if counter == 1:
	tarnorm = str(r[0][0])
	tarup = str(r[0][1])
	print("""		<fieldset> 
			<legend><p class="header">ВАШ ТАРИФ</p></legend>""")
	print ("<p>При энергопотреблении ниже социальной нормы: {} р/кВт*ч</p>".format(tarnorm))
	print ("<p>При энергопотреблении выше социальной нормы: {} р/кВт*ч</p>".format(tarup))
	print ("""</fieldset>""")
	print("""		<fieldset> 
			<legend><p class="header">ХОТИТЕ ПРОДОЛЖИТЬ?</p></legend>
				<form id="tarifform2" action="formaction5.py" method="post">
				<p class="header"><b>Выберите дальнейшие действия</b></p>
				<p class="textform"><label><input type="radio" name="action" value=1>Ввести показания счетчика и рассчитать сумму к оплате</label>
				<label><input type="radio" name="action" value=2>Рассчитать расход электроприборов</label></p>""")
				
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
if counter == 2:
	tarnorm_day = str(r[1][0])
	tarnorm_night = str(r[2][0])
	tarup_day = str(r[1][1])
	tarup_night = str(r[2][1])
	print("""		<fieldset> 
			<legend><p class="header">ВАШ ТАРИФ</p></legend>""")
	print("""<p class="header"><b>ДНЕВНАЯ ЗОНА (7:00-23:00)</b></p>""")
	print ("<p>При энергопотреблении ниже социальной нормы: {} р/кВт*ч</p>".format(tarnorm_day))
	print ("<p>При энергопотреблении выше социальной нормы: {} р/кВт*ч</p>".format(tarup_day))
	print("""<p class="header"><b>НОЧНАЯ ЗОНА (23:00-7:00)</b></p>""")
	print ("<p>При энергопотреблении ниже социальной нормы: {} р/кВт*ч</p>".format(tarnorm_night))
	print ("<p>При энергопотреблении выше социальной нормы: {} р/кВт*ч</p>".format(tarup_night))
	print ("""</fieldset>""")	
	print("""		<fieldset> 
			<legend><p class="header">ХОТИТЕ ПРОДОЛЖИТЬ?</p></legend>
				<form id="tarifform2" action="formaction5.py" method="post">
				<p class="header"><b>Выберите дальнейшие действия</b></p>
				<p class="textform"><label><input type="radio" name="action" value=1>Ввести показания счетчика и рассчитать сумму к оплате</label>
				<label><input type="radio" name="action" value=2>Рассчитать расход электроприборов</label></p>""")
				
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
if counter == 3:
	tarnorm_peak = str(r[3][0])
	tarnorm_semipeak = str(r[4][0])
	tarnorm_night = str(r[5][0])
	tarup_peak = str(r[3][1])
	tarup_semipeak = str(r[4][1])
	tarup_night = str(r[5][1])
	print("""		<fieldset> 
			<legend><p class="header">ВАШ ТАРИФ</p></legend>""")
	print("""<p class="header"><b>ПИКОВАЯ ЗОНА (7:00-10:00 / 17:00-21:00)</b></p>""")
	print ("<p>При энергопотреблении ниже социальной нормы: {} р/кВт*ч</p>".format(tarnorm_peak))
	print ("<p>При энергопотреблении выше социальной нормы: {} р/кВт*ч</p>".format(tarup_peak))
	print("""<p class="header"><b>ПОЛУПИКОВАЯ ЗОНА (10:00-17:00 / 21:00-23:00)</b></p>""")
	print ("<p>При энергопотреблении ниже социальной нормы: {} р/кВт*ч</p>".format(tarnorm_semipeak))
	print ("<p>При энергопотреблении выше социальной нормы: {} р/кВт*ч</p>".format(tarup_semipeak))
	print("""<p class="header"><b>НОЧНАЯ ЗОНА (23:00-7:00)</b></p>""")
	print ("<p>При энергопотреблении ниже социальной нормы: {} р/кВт*ч</p>".format(tarnorm_night))
	print ("<p>При энергопотреблении выше социальной нормы: {} р/кВт*ч</p>".format(tarup_night))
	print ("""</fieldset>""")
	print("""		<fieldset> 
			<legend><p class="header">ХОТИТЕ ПРОДОЛЖИТЬ?</p></legend>
				<form id="tarifform2" action="formaction5.py" method="post">
				<p class="header"><b>Выберите дальнейшие действия</b></p>
				<p class="textform"><label><input type="radio" name="action" value=1>Ввести показания счетчика и рассчитать сумму к оплате</label>
				<label><input type="radio" name="action" value=2>Рассчитать расход электроприборов</label></p>""")
				
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
		
if counter == 4:
	print("""		<fieldset> 
			<legend><p class="header">ВАШ НОРМАТИВ</p></legend>""")
	print ("<p>Ваш текущий норматив: {} кВт</p>".format(nr))
	print ("""</fieldset>""")
	print("""		<fieldset> 
			<legend><p class="header">ХОТИТЕ ПРОДОЛЖИТЬ?</p></legend>
				<form id="tarifform2" action="formaction5.py" method="post">
				<p class="header"><b>Выберите дальнейшие действия</b></p>
				<p class="textform"><label><input type="radio" name="action" value=1>Рассчитать сумму к оплате</label>
				<label><input type="radio" name="action" value=2>Ввести сумму и составить план энергопотребления</label></p>""")
				
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
   
print("""				<p><button type="submit" />Далее</button></p>
				</form>
		</fieldset>
		</tr></table></div>
	<div class="description"><p class="big header">ГРАФИК ПЛАНОВЫХ ОТКЛЮЧЕНИЙ</p>
	<p class = "text narrow">Ура! Теперь можно изучить график плановых отключений электроэнергии, найти в нем свой дом и<br> заранее подготовиться к неизбежному</p>
	<br><a href="../information.html#plans"><div class="btt red middle">ПОСМОТРЕТЬ ГРАФИК</div></a></div>

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