#!/usr/bin/env python3
import cgi, os
import numpy
import csv
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
	<div class="wide-block"><table><tr>""")
print("""		<fieldset> 
			<legend><b>Укажите средние недельные часы использования электроприборов</b></legend>
				<form id="tarifform2" action="calktarif2-time.py" method="post">""")
if tarifform.getfirst("tv") != None:
	print("""<p>Телевизор</p>
				<p><label>День:   <input type="text" name="tvtime_day"></label><label>
				Ночь:   <input type="text" name="tvtime_night"></label></p><input type="hidden" name="tv" value=0.18>""")
if tarifform.getfirst("sound") != None:
	print("""<p>Акустическая система</p>
				<p><label>День:   <input type="text" name="soundtime_day"></label><label>
				Ночь:   <input type="text" name="soundtime_night"></label><input type="hidden" name="sound" value=0.1></p>""")				
if tarifform.getfirst("comp") != None:
	print("""<p>Компьютер</p>
				<p><label>День:   <input type="text" name="comptime_day"></label><label>
				Ночь:   <input type="text" name="comptime_night"></label><input type="hidden" name="comp" value=0.6></p>""")				
if tarifform.getfirst("pyl") != None:
	print("""<p>Пылесос</p>
				<p><label>День:   <input type="text" name="pyltime_day"></label><label>
				Ночь:   <input type="text" name="pyltime_night"></label><input type="hidden" name="pyl" value=1></p>""")
if tarifform.getfirst("coffee") != None:
	print("""<p>Кофемашина</p>
				<p><label>День:   <input type="text" name="coffeetime_day"></label><label>
				Ночь:   <input type="text" name="coffeetime_night"></label><input type="hidden" name="coffee" value=0.8></p>""")
if tarifform.getfirst("stir") != None:
	print("""<p>Стиральная машина</b></p>
				<p><label>День:   <input type="text" name="stirtime_day"></label><label>
				Ночь:   <input type="text" name="stirtime_night"></label><input type="hidden" name="stir" value=3.3></p>""")
if tarifform.getfirst("ut") != None:
	print("""<p>Утюг</p>
				<p><label>День:   <input type="text" name="uttime_day"></label><label>
				Ночь:   <input type="text" name="uttime_night"></label><input type="hidden" name="ut" value=1></p>""")
if tarifform.getfirst("kond") != None:
	print("""<p>Кондиционер</p>
				<p><label>День:   <input type="text" name="kondtime_day"></label><label>
				Ночь:   <input type="text" name="kondtime_night"></label><input type="hidden" name="kond" value=1.5></p>""")
if tarifform.getfirst("vent") != None:
	print("""<p>Тепловентилятор</p>
				<p><label>День:   <input type="text" name="venttime_day"></label><label>
				Ночь:   <input type="text" name="venttime_night"></label><input type="hidden" name="vent" value=2></p>""")
if tarifform.getfirst("tea") != None:
	print("""<p>Чайник</p>
				<p><label>День:   <input type="text" name="teatime_day"></label><label>
				Ночь:   <input type="text" name="teatime_night"></label><input type="hidden" name="tea" value=1></p>""")
if tarifform.getfirst("fridge") != None:
	print("""<p>Холодильник</p>
				<p><label>День:   <input type="text" name="fridgetime_day"></label><label>
				Ночь:   <input type="text" name="fridgetime_night"></label><input type="hidden" name="fridge" value=0.2></p>""")
if tarifform.getfirst("moroz") != None:
	print("""<p>Морозильная камера</p>
				<p><label>День:   <input type="text" name="moroztime_day"></label><label>
				Ночь:   <input type="text" name="moroztime_night"></label><input type="hidden" name="moroz" value=0.2></p>""")
if tarifform.getfirst("elpl") != None:
	print("""<p>Электрическая плита</p>
				<p><label>День:   <input type="text" name="elpltime_day"></label><label>
				Ночь:   <input type="text" name="elpltime_night"></label><input type="hidden" name="elpl" value=2.5></p>""")
if tarifform.getfirst("mwv") != None:
	print("""<p>Микроволновая печь</p>
				<p><label>День:   <input type="text" name="mwvtime_day"></label><label>
				Ночь:   <input type="text" name="mwvtime_night"></label><input type="hidden" name="mwv" value=1></p>""")
if tarifform.getfirst("warm") != None:
	print("""<p>Обогреватель</p>
				<p><label>День:   <input type="text" name="warmtime_day"></label><label>
				Ночь:   <input type="text" name="warmtime_night"></label><input type="hidden" name="warm" value=11></p>""")
if tarifform.getfirst("posm") != None:
	print("""<p>Посудомоечная машина</p>
				<p><label>День:   <input type="text" name="posmtime_day"></label><label>
				Ночь:   <input type="text" name="posmtime_night"></label><input type="hidden" name="posm" value=2></p>""")
if tarifform.getfirst("mix") != None:
	print("""<p>Миксер</p>
				<p><label>День:   <input type="text" name="mixtime_day"></label><label>
				Ночь:   <input type="text" name="mixtime_night"></label><input type="hidden" name="mix" value=0.2></p>""")
if tarifform.getfirst("tost") != None:
	print("""<p>Тостер</p>
				<p><label>День:   <input type="text" name="tosttime_day"></label><label>
				Ночь:   <input type="text" name="tosttime_night"></label><input type="hidden" name="tost" value=1.3></p>""")
if tarifform.getfirst("vyt") != None:
	print("""<p>Вытяжка</p>
				<p><label>День:   <input type="text" name="vyttime_day"></label><label>
				Ночь:   <input type="text" name="vyttime_night"></label><input type="hidden" name="vyt" value=0.21></p>""")
if tarifform.getfirst("fen") != None:
	print("""<p>Фен</p>
				<p><label>День:   <input type="text" name="fentime_day"></label><label>
				Ночь:   <input type="text" name="fentime_night"></label><input type="hidden" name="fen" value=0.8></p>""")
if tarifform.getfirst("varp") != None:
	print("""<p>Варочная панель</p>
				<p><label>День:   <input type="text" name="varptime_day"></label><label>
				Ночь:   <input type="text" name="varptime_night"></label><input type="hidden" name="varp" value=1.5></p>""")
if tarifform.getfirst("duhsh") != None:
	print("""<p>Духовой шкаф</p>
				<p><label>День:   <input type="text" name="duhshtime_day"></label><label>
				Ночь:   <input type="text" name="duhshtime_night"></label><input type="hidden" name="duhsh" value=3.5></p>""")
if tarifform.getfirst("vposm") != None:
	print("""<p>Встроенная посудомойка</p>
				<p><label>День:   <input type="text" name="vposmtime_day"></label><label>
				Ночь:   <input type="text" name="vposmtime_night"></label><input type="hidden" name="vposm" value=3.5></p>""")
if tarifform.getfirst("drl") != None:
	print("""<p>Дрель</p>
				<p><label>День:   <input type="text" name="drltime_day"></label><label>
				Ночь:   <input type="text" name="drltime_night"></label><input type="hidden" name="drl" value=0.25></p>""")
print ("""</fieldset><fieldset><legend><b>Количество лампочек и среднее время их использования</b></legend>""")				
if tarifform.getfirst("ln") != None:
	print("""<p><b>Сколько ламп накаливания задействованы в освещении и какое среднее время их использования в неделю:</b></p>
				<p><label>Количество:   <input type="text" name="lnq"></label>
				<label>   Время днем:   <input type="text" name="lntime_day"></label>
				<label>   Время ночью:   <input type="text" name="lntime_night"></label><input type="hidden" name="ln" value=0.1></p>""")
if tarifform.getfirst("ll") != None:
	print("""<p><b>Сколько люминисцентных ламп задействованы в освещении и какое среднее время их использования в неделю:</b></p>
				<p><label>Количество:   <input type="text" name="llq"></label>
				<label>   Время днем:   <input type="text" name="lltime_day"></label>
				<label>   Время ночью:   <input type="text" name="lltime_night"></label><input type="hidden" name="ll" value=0.078></p>""")
if tarifform.getfirst("ls") != None:
	print("""<p><b>Сколько энергосберегающих ламп задействованы в освещении и какое среднее время их использования в неделю:</b></p>
				<p><label>Количество:   <input type="text" name="lsq"></label>
				<label>   Время днем:   <input type="text" name="lstime_day"></label>
				<label>   Время ночью:   <input type="text" name="lstime_night"></label><input type="hidden" name="ls" value=0.042></p>""")
if tarifform.getfirst("lg") != None:
	print("""<p><b>Сколько галогенных ламп задействованы в освещении и какое среднее время их использования в неделю:</b></p>
				<p><label>Количество:   <input type="text" name="lgq"></label>
				<label>   Время днем:   <input type="text" name="lgtime_day"></label>
				<label>   Время ночью:   <input type="text" name="lgtime_night"></label><input type="hidden" name="lg" value=0.22></p>""")
print ("""</fieldset>""")				
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
   
print("""<input type="hidden" name="counter" value=1>""")				
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