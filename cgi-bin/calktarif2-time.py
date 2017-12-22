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
	
if tarifform.getfirst("tvtime_day") != None:
	tvtime_day = float(tarifform.getfirst("tvtime_day"))
	tvtime_night = float(tarifform.getfirst("tvtime_night"))
	tvsr = float(tarifform.getfirst("tv"))*4
	energy_and_hours.append((tvsr,(tvtime_day,tvtime_night,)))
		
if tarifform.getfirst("soundtime_day") != None:
	soundtime_day = float(tarifform.getfirst("soundtime_day"))
	soundtime_night = float(tarifform.getfirst("soundtime_night"))
	soundsr = float(tarifform.getfirst("sound"))*4
	energy_and_hours.append((soundsr,(soundtime_day,soundtime_night,)))

if tarifform.getfirst("comptime_day") != None:
	comptime_day = float(tarifform.getfirst("comptime_day"))
	comptime_night = float(tarifform.getfirst("comptime_night"))
	compsr = float(tarifform.getfirst("comp"))*4
	energy_and_hours.append((compsr,(comptime_day,comptime_night,)))

if tarifform.getfirst("pyltime_day") != None:
	pyltime_day = float(tarifform.getfirst("pyltime_day"))
	pyltime_night = float(tarifform.getfirst("pyltime_night"))
	pylsr = float(tarifform.getfirst("pyl"))*4
	energy_and_hours.append((pylsr,(pyltime_day,pyltime_night,)))

if tarifform.getfirst("coffee_day") != None:
	coffeetime_day = float(tarifform.getfirst("coffeetime_day"))
	coffeetime_night = float(tarifform.getfirst("coffeetime_night"))
	coffeesr = float(tarifform.getfirst("coffee"))*4
	energy_and_hours.append((coffeesr,(coffeetime_day,coffeetime_night,)))

if tarifform.getfirst("stirtime_day") != None:
	stirtime_day = float(tarifform.getfirst("stirtime_day"))
	stirtime_night = float(tarifform.getfirst("stirtime_night"))
	stirsr = float(tarifform.getfirst("stir"))*4
	energy_and_hours.append((stirsr,(stirtime_day,stirtime_night,)))

if tarifform.getfirst("uttime_day") != None:
	uttime_day = float(tarifform.getfirst("uttime_day"))
	uttime_night = float(tarifform.getfirst("uttime_night"))
	utsr = float(tarifform.getfirst("ut"))*4
	energy_and_hours.append((utsr,(uttime_day,uttime_night,)))

if tarifform.getfirst("kondtime_day") != None:
	kondtime_day = float(tarifform.getfirst("kondtime_day"))
	kondtime_night = float(tarifform.getfirst("kondtime_night"))
	kondsr = float(tarifform.getfirst("kond"))*4
	energy_and_hours.append((kondsr,(kondtime_day,kondtime_night,)))

if tarifform.getfirst("venttime_day") != None:
	venttime_day = float(tarifform.getfirst("venttime_day"))
	venttime_night = float(tarifform.getfirst("venttime_night"))
	ventsr = float(tarifform.getfirst("vent"))*4
	energy_and_hours.append((ventsr,(venttime_day,venttime_night,)))

if tarifform.getfirst("teatime_day") != None:
	teatime_day = float(tarifform.getfirst("teatime_day"))
	teatime_night = float(tarifform.getfirst("teatime_night"))
	teasr = float(tarifform.getfirst("tea"))*4
	energy_and_hours.append((teasr,(teatime_day,teatime_night,)))

if tarifform.getfirst("fridge_day") != None:
	fridgetime_day = float(tarifform.getfirst("fridgetime_day"))
	fridgetime_night = float(tarifform.getfirst("fridgetime_night"))
	fridgesr = float(tarifform.getfirst("fridge"))*4
	energy_and_hours.append((fridgesr,(fridgetime_day,fridgetime_night,)))

if tarifform.getfirst("moroztime_day") != None:
	moroztime_day = float(tarifform.getfirst("moroztime_day"))
	moroztime_night = float(tarifform.getfirst("moroztime_night"))
	morozsr = float(tarifform.getfirst("moroz"))*4
	energy_and_hours.append((morozsr,(moroztime_day,moroztime_night,)))

if tarifform.getfirst("elpltime_day") != None:
	elpltime_day = float(tarifform.getfirst("elpltime_day"))
	elpltime_night = float(tarifform.getfirst("elpltime_night"))
	elplsr = float(tarifform.getfirst("elpl"))*4
	energy_and_hours.append((elplsr,(elpltime_day,elpltime_night,)))

if tarifform.getfirst("mwvtime_day") != None:
	mwvtime_day = float(tarifform.getfirst("mwvtime_day"))
	mwvtime_night = float(tarifform.getfirst("mwvtime_night"))
	mwvsr = float(tarifform.getfirst("mwv"))*4
	energy_and_hours.append((mwvsr,(mwvtime_day,mwvtime_night,)))

if tarifform.getfirst("warmtime_day") != None:
	warmtime_day = float(tarifform.getfirst("warmtime_day"))
	warmtime_night = float(tarifform.getfirst("warmtime_night"))
	warmsr = float(tarifform.getfirst("warm"))*4
	energy_and_hours.append((warmsr,(warmtime_day,warmtime_night,)))

if tarifform.getfirst("posmtime_day") != None:
	posmtime_day = float(tarifform.getfirst("posmtime_day"))
	posmtime_night = float(tarifform.getfirst("posmtime_night"))
	posmsr = float(tarifform.getfirst("posm"))*4
	energy_and_hours.append((posmsr,(posmtime_day,posmtime_night,)))

if tarifform.getfirst("mixtime_day") != None:
	mixtime_day = float(tarifform.getfirst("mixtime_day"))
	mixtime_night = float(tarifform.getfirst("mixtime_night"))
	mixsr = float(tarifform.getfirst("mix"))*4
	energy_and_hours.append((mixsr,(mixtime_day,mixtime_night,)))

if tarifform.getfirst("tosttime_day") != None:
	tosttime_day = float(tarifform.getfirst("tosttime_day"))
	tosttime_night = float(tarifform.getfirst("tosttime_night"))
	tostsr = float(tarifform.getfirst("tost"))*4
	energy_and_hours.append((tostsr,(tosttime_day,tosttime_night,)))

if tarifform.getfirst("vyttime_day") != None:
	vyttime_day = float(tarifform.getfirst("vyttime_day"))
	vyttime_night = float(tarifform.getfirst("vyttime_night"))
	vytsr = float(tarifform.getfirst("vyt"))*4
	energy_and_hours.append((vytsr,(vyttime_day,vyttime_night,)))

if tarifform.getfirst("fentime_day") != None:
	fentime_day = float(tarifform.getfirst("fentime_day"))
	fentime_night = float(tarifform.getfirst("fentime_night"))
	fensr = float(tarifform.getfirst("fen"))*4
	energy_and_hours.append((fensr,(fentime_day,fentime_night,)))

if tarifform.getfirst("varptime_day") != None:
	varptime_day = float(tarifform.getfirst("varptime_day"))
	varptime_night = float(tarifform.getfirst("varptime_night"))
	varpsr = float(tarifform.getfirst("varp"))*4
	energy_and_hours.append((varpsr,(varptime_day,varptime_night,)))

if tarifform.getfirst("duhshtime_day") != None:
	duhshtime_day = float(tarifform.getfirst("duhshtime_day"))
	duhshtime_night = float(tarifform.getfirst("duhshtime_night"))
	duhshsr = float(tarifform.getfirst("duhsh"))*4
	energy_and_hours.append((duhshsr,(duhshtime_day,duhshtime_night,)))

if tarifform.getfirst("vposm_day") != None:
	vposmtime_day = float(tarifform.getfirst("vposmtime_day"))
	vposmtime_night = float(tarifform.getfirst("vposmtime_night"))
	vposmsr = float(tarifform.getfirst("vposm"))*4
	energy_and_hours.append((vposmsr,(vposmtime_day,vposmtime_night,)))

if tarifform.getfirst("multtime_day") != None:
	multtime_day = float(tarifform.getfirst("multtime_day"))
	multtime_night = float(tarifform.getfirst("multtime_night"))
	multsr = float(tarifform.getfirst("mult"))*4
	energy_and_hours.append((multsr,(multtime_day,multtime_night,)))

if tarifform.getfirst("drltime_day") != None:
	drltime_day = float(tarifform.getfirst("drltime_day"))
	drltime_night = float(tarifform.getfirst("drltime_night"))
	drlsr = float(tarifform.getfirst("drl"))*4
	energy_and_hours.append((drlsr,(drltime_day,drltime_night,)))

if tarifform.getfirst("lntime_day") != None:
	lntime_day = float(tarifform.getfirst("lntime_day"))
	lntime_night = float(tarifform.getfirst("lntime_night"))
	lnq = float(tarifform.getfirst("lnq"))
	lnsr = float(tarifform.getfirst("ln"))*4*lnq
	energy_and_hours.append((lnsr,(lntime_day,lntime_night,)))

if tarifform.getfirst("lltime_day") != None:
	lltime_day = float(tarifform.getfirst("lltime_day"))
	lltime_night = float(tarifform.getfirst("lltime_night"))
	llq = float(tarifform.getfirst("llq"))
	llsr = float(tarifform.getfirst("ll"))*4*llq
	energy_and_hours.append((llsr,(lltime_day,lltime_night,)))

if tarifform.getfirst("lstime_day") != None:
	lstime_day = float(tarifform.getfirst("lstime_day"))
	lstime_night = float(tarifform.getfirst("lstime_night"))
	lsq = float(tarifform.getfirst("lsq"))
	lssr = float(tarifform.getfirst("ls"))*4*lsq
	energy_and_hours.append((lssr,(lstime_day,lstime_night,)))

if tarifform.getfirst("lgtime_day") != None:
	lgtime_day = float(tarifform.getfirst("lgtime_day"))
	lgtime_night = float(tarifform.getfirst("lgtime_night"))
	lgq = float(tarifform.getfirst("lgq"))
	lgsr = float(tarifform.getfirst("lg"))*4*lgq
	energy_and_hours.append((lgsr,(lgtime_day,lgtime_night,)))
	
q_day = sum([tup[0] * tup[1][0] for tup in energy_and_hours])
q_night = sum([tup[0] * tup[1][1] for tup in energy_and_hours])

if (q_day + q_night) > n:
    M1, v1 = numpy.array([[1., 1.], [q_day, -q_night]]), numpy.array([n,0.])
    counts = numpy.linalg.solve(M1, v1)
    total = str(round(counts[0]*r[1][0] + counts[1]*r[2][0] + (q_day-counts[0])*r[1][1] + (q_night-counts[1])*r[2][1],2))
else:
	total = str(round(q_day*r[1][0] + q_night*r[2][0],2))
	
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