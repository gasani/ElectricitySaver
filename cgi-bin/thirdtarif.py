#!/usr/bin/env python3
import cgi, os, ckks
import numpy
tarifform = cgi.FieldStorage()
plate = int(tarifform.getfirst("plate"))
water = int(tarifform.getfirst("water"))
people = int(tarifform.getfirst("people"))
rooms = int(tarifform.getfirst("rooms"))
counter = int(tarifform.getfirst("counter"))
q_peak = float(tarifform.getfirst("q_peak"))
q_semipeak = float(tarifform.getfirst("q_semipeak"))
q_night = float(tarifform.getfirst("q_night"))
n = 85+(50*(people-1))
dif = 0
normals = [[103,64,49,40,35],[133,82,64,52,45],[150,93,72,59,51],[162,101,78,63,55],[153,95,73,60,52],[180,112,87,70,61],[197,122,95,77,67],[209,130,101,82,71],
           [174,108,84,68,59],[225,139,108,88,76],[255,158,122,99,87],[276,171,132,107,94],[224,139,108,88,76],[265,164,127,103,90],[289,179,139,113,98],[307,191,148,120,105]]
plates = [[3.45,5.98],[3.58,6.88],[1.75,3.59],[3.62,7.18],[3.45,5.98],[1.75,3.59],[2.48,4.31],[2.53,4.96],[1.24,2.59],[2.55,5.17],[2.48,4.31],[1.24,2.59]]

if plate == 1:
    r = plates[:6]
else:
    r = plates[6:]		

if (q_peak + q_semipeak + q_night) > n: #если потреблено > соц.нормы
    M1 = numpy.array([[1., 1., 1.], [q_semipeak, q_night-q_peak, -q_semipeak],[q_night+q_semipeak, -q_peak, -q_peak], [q_night, q_night, -q_peak-q_semipeak]]) 
    v1 = numpy.array([n,0.,0.,0.])
    counts = numpy.linalg.lstsq(M1, v1)
    counts = counts[0]
    total = str(round(counts[0]*r[3][0] + counts[1]*r[4][0] + counts[2]*r[5][0] + (q_peak-counts[0])*r[3][1] + (q_semipeak-counts[1])*r[4][1] + (q_night-counts[2])*r[5][1],2))
    tar_peak = str(r[3][1])
    tar_semipeak = str(r[4][1])
    tar_night = str(r[5][1])
else: #если потреблено < соц.нормы
    total = str(round(q_peak*r[3][0] + q_semipeak*r[4][0] + q_night*r[5][0],2))
    tar_peak = str(r[3][0])
    tar_semipeak = str(r[4][0])
    tar_night = str(r[5][0])
    dif = q_peak + q_semipeak + q_night - n
	
log = ckks.set_cookies()
print("""Content-type: text/html\n
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
	<div class="wide-block"><table><tr>""".format( log.upper() if log else 'ВХОД', '<li><a href="register.py">РЕГИСТРАЦИЯ</a></li>' if not log else '' )) 
print ("""<fieldset> 
			<legend><p class="header">ИТОГ</p></legend>""")
print ("<p>Ваш текущий пиковый тариф: {} р/кВт*ч</p>".format(tar_peak))
print ("<p>Ваш текущий полупиковый тариф: {} р/кВт*ч</p>".format(tar_semipeak))
print ("<p>Ваш текущий ночной тариф: {} р/кВт*ч</p>".format(tar_night)) 		
print ("<p>Сумма к оплате: {} р</p>".format(total))   
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