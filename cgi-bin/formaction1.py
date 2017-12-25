#!/usr/bin/env python3
import cgi, os, ckks
log = ckks.set_cookies()
tarifform = cgi.FieldStorage()
plate = int(tarifform.getfirst("plate"))
water = int(tarifform.getfirst("water"))

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
""".format( log.upper() if log else 'ВХОД', '<li><a href="register.py">РЕГИСТРАЦИЯ</a></li>' if not log else '' ) )
print("""<section id="hello">
	</section>
	<div class="wide-block"><table><tr>
	<fieldset><img src="../img/2.png" width="100%"></fieldset>""")
print("""		<fieldset> 
			<legend><p class="header">УЗНАЙТЕ СВОЙ ТАРИФ</p></legend>
				<form action="formaction2.py" method="post">
				<p class="header"><b>Количество зарегистрированных жильцов</b></p>
				<p class="textform"><label class="labelform1"><input type="radio" name="people" value=1>1</label>
				<label class="labelform1"><input type="radio" name="people" value=2>2</label>
				<label class="labelform1"><input type="radio" name="people" value=3>3</label>
				<label class="labelform1"><input type="radio" name="people" value=4>4</label>
				<label class="labelform1"><input type="radio" name="people" value=5>5+</label></p>
				<p class="header"><b>Количество жилых комнат</b></p>
				<p class="textform"><label class="labelform1"><input type="radio" name="rooms" value=1>1</label>
				<label class="labelform1"><input type="radio" name="rooms" value=2>2</label>
				<label class="labelform1"><input type="radio" name="rooms" value=3>3</label>
				<label class="labelform1"><input type="radio" name="rooms" value=4>4</label></p>""")
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
	