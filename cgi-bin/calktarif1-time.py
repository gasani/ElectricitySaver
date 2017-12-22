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
energy_and_hours = list()
	
if tarifform.getfirst("tvtime") != None:
	tvtime = float(tarifform.getfirst("tvtime"))
	tvsr = float(tarifform.getfirst("tv"))*4
	energy_and_hours.append((tvsr,(tvtime,)))
else:
	tvtime = 0 
	tvsr = 0		
if tarifform.getfirst("soundtime") != None:
	soundtime = float(tarifform.getfirst("soundtime"))
	soundsr = float(tarifform.getfirst("sound"))*4
	energy_and_hours.append((soundsr,(soundtime,)))
else:
	soundtime = 0 
	soundsr = 0
if tarifform.getfirst("comptime") != None:
	comptime = float(tarifform.getfirst("comptime"))
	compsr = float(tarifform.getfirst("comp"))*4
	energy_and_hours.append((compsr,(comptime,)))
else:
	comptime = 0 
	compsr = 0
if tarifform.getfirst("pyltime") != None:
	pyltime = float(tarifform.getfirst("pyltime"))
	pylsr = float(tarifform.getfirst("pyl"))*4
	energy_and_hours.append((pylsr,(pyltime,)))
else:
	pyltime = 0 
	pylsr = 0
if tarifform.getfirst("coffee") != None:
	coffeetime = float(tarifform.getfirst("coffeetime"))
	coffeesr = float(tarifform.getfirst("coffee"))*4
	energy_and_hours.append((coffeesr,(coffeetime,)))
else:
	coffeetime = 0 
	coffeesr = 0
if tarifform.getfirst("stirtime") != None:
	stirtime = float(tarifform.getfirst("stirtime"))
	stirsr = float(tarifform.getfirst("stir"))*4
	energy_and_hours.append((stirsr,(stirtime,)))
else:
	stirtime = 0 
	stirsr = 0
if tarifform.getfirst("uttime") != None:
	uttime = float(tarifform.getfirst("uttime"))
	utsr = float(tarifform.getfirst("ut"))*4
	energy_and_hours.append((utsr,(uttime,)))
else:
	uttime = 0 
	utsr = 0
if tarifform.getfirst("kondtime") != None:
	kondtime = float(tarifform.getfirst("kondtime"))
	kondsr = float(tarifform.getfirst("kond"))*4
	energy_and_hours.append((kondsr,(kondtime,)))
else:
	kondtime = 0 
	kondsr = 0
if tarifform.getfirst("venttime") != None:
	venttime = float(tarifform.getfirst("venttime"))
	ventsr = float(tarifform.getfirst("vent"))*4
	energy_and_hours.append((ventsr,(venttime,)))
else:
	venttime = 0 
	ventsr = 0
if tarifform.getfirst("teatime") != None:
	teatime = float(tarifform.getfirst("teatime"))
	teasr = float(tarifform.getfirst("tea"))*4
	energy_and_hours.append((teasr,(teatime,)))
else:
	teatime = 0 
	teasr = 0
if tarifform.getfirst("fridge") != None:
	fridgetime = float(tarifform.getfirst("fridgetime"))
	fridgesr = float(tarifform.getfirst("fridge"))*4
	energy_and_hours.append((fridgesr,(fridgetime,)))
else:
	fridgetime = 0 
	fridgesr = 0
if tarifform.getfirst("moroztime") != None:
	moroztime = float(tarifform.getfirst("moroztime"))
	morozsr = float(tarifform.getfirst("moroz"))*4
	energy_and_hours.append((morozsr,(moroztime,)))
else:
	moroztime = 0 
	morozsr = 0
if tarifform.getfirst("elpltime") != None:
	elpltime = float(tarifform.getfirst("elpltime"))
	elplsr = float(tarifform.getfirst("elpl"))*4
	energy_and_hours.append((elplsr,(elpltime,)))
else:
	elpltime = 0 
	elplsr = 0
if tarifform.getfirst("mwvtime") != None:
	mwvtime = float(tarifform.getfirst("mwvtime"))
	mwvsr = float(tarifform.getfirst("mwv"))*4
	energy_and_hours.append((mwvsr,(mwvtime,)))
else:
	mwvtime = 0 
	mwvsr = 0
if tarifform.getfirst("warmtime") != None:
	warmtime = float(tarifform.getfirst("warmtime"))
	warmsr = float(tarifform.getfirst("warm"))*4
	energy_and_hours.append((warmsr,(warmtime,)))
else:
	warmtime = 0 
	warmsr = 0
if tarifform.getfirst("posmtime") != None:
	posmtime = float(tarifform.getfirst("posmtime"))
	posmsr = float(tarifform.getfirst("posm"))*4
	energy_and_hours.append((posmsr,(posmtime,)))
else:
	posmtime = 0 
	posmsr = 0
if tarifform.getfirst("mixtime") != None:
	mixtime = float(tarifform.getfirst("mixtime"))
	mixsr = float(tarifform.getfirst("mix"))*4
	energy_and_hours.append((mixsr,(mixtime,)))
else:
	mixtime = 0 
	mixsr = 0
if tarifform.getfirst("tosttime") != None:
	tosttime = float(tarifform.getfirst("tosttime"))
	tostsr = float(tarifform.getfirst("tost"))*4
	energy_and_hours.append((tostsr,(tosttime,)))
else:
	tosttime = 0 
	tostsr = 0
if tarifform.getfirst("vyttime") != None:
	vyttime = float(tarifform.getfirst("vyttime"))
	vytsr = float(tarifform.getfirst("vyt"))*4
	energy_and_hours.append((vytsr,(vyttime,)))
else:
	vyttime = 0 
	vytsr = 0
if tarifform.getfirst("fentime") != None:
	fentime = float(tarifform.getfirst("fentime"))
	fensr = float(tarifform.getfirst("fen"))*4
	energy_and_hours.append((fensr,(fentime,)))
else:
	fentime = 0 
	fensr = 0
if tarifform.getfirst("varptime") != None:
	varptime = float(tarifform.getfirst("varptime"))
	varpsr = float(tarifform.getfirst("varp"))*4
	energy_and_hours.append((varpsr,(varptime,)))
else:
	varptime = 0 
	varpsr = 0
if tarifform.getfirst("duhshtime") != None:
	duhshtime = float(tarifform.getfirst("duhshtime"))
	duhshsr = float(tarifform.getfirst("duhsh"))*4
	energy_and_hours.append((duhshsr,(duhshtime,)))
else:
	duhshtime = 0 
	duhshsr = 0
if tarifform.getfirst("vposm") != None:
	vposmtime = float(tarifform.getfirst("vposmtime"))
	vposmsr = float(tarifform.getfirst("vposm"))*4
	energy_and_hours.append((vposmsr,(vposmtime,)))
else:
	vposmtime = 0 
	vposmsr = 0
if tarifform.getfirst("multtime") != None:
	multtime = float(tarifform.getfirst("multtime"))
	multsr = float(tarifform.getfirst("mult"))*4
	energy_and_hours.append((multsr,(multtime,)))
else:
	multtime = 0 
	multsr = 0
if tarifform.getfirst("drltime") != None:
	drltime = float(tarifform.getfirst("drltime"))
	drlsr = float(tarifform.getfirst("drl"))*4
	energy_and_hours.append((drlsr,(drltime,)))
else:
	drltime = 0 
	drlsr = 0
if tarifform.getfirst("lntime") != None:
	lntime = float(tarifform.getfirst("lntime"))
	lnq = float(tarifform.getfirst("lnq"))
	lnsr = float(tarifform.getfirst("ln"))*4*lnq
	energy_and_hours.append((lnsr,(lntime,)))
else:
	lntime = 0 
	lnsr = 0
if tarifform.getfirst("lltime") != None:
	lltime = float(tarifform.getfirst("lltime"))
	llq = float(tarifform.getfirst("llq"))
	llsr = float(tarifform.getfirst("ll"))*4*llq
	energy_and_hours.append((llsr,(lltime,)))
else:
	lltime = 0 
	llsr = 0
if tarifform.getfirst("lstime") != None:
	lstime = float(tarifform.getfirst("lstime"))
	lsq = float(tarifform.getfirst("lsq"))
	lssr = float(tarifform.getfirst("ls"))*4*lsq
	energy_and_hours.append((lssr,(lstime,)))
else:
	lstime = 0 
	lssr = 0
if tarifform.getfirst("lgtime") != None:
	lgtime = float(tarifform.getfirst("lgtime"))
	lgq = float(tarifform.getfirst("lgq"))
	lgsr = float(tarifform.getfirst("lg"))*4*lgq
	energy_and_hours.append((lgsr,(lgtime,)))
else:
	lgtime = 0 
	lgsr = 0	
q = sum([tup[0] * tup[1][0] for tup in energy_and_hours])
if q > n:
	total = str(round(n*r[0][0] + (q-n)*r[0][1],2))
else:
	total = str(round(q*r[0][0],2))
	
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
	<div class="wide-block"><table><tr><fieldset><p class="header">ИТОГ</p>""")
print ("<p>При таком использовании в месяц вы потратите: {} р</p>".format(total))
print("""</fieldset>
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
