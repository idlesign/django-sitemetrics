{% for keycode in keycodes %}
	{% ifequal keycode.provider "yandex" %}
		<script src="//mc.yandex.ru/metrika/watch.js" type="text/javascript"></script>
		<div style="display:none;"><script type="text/javascript">try { var yaCounter{{ keycode.keycode }} = new Ya.Metrika({{ keycode.keycode }}); } catch(e){}</script></div>
		<noscript><div style="position:absolute"><img src="//mc.yandex.ru/watch/{{ keycode.keycode }}" alt="" /></div></noscript>
	{% endifequal %}
	{% ifequal keycode.provider "google" %}
		<script type="text/javascript">var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));</script>
		<script type="text/javascript">try{var pageTracker = _gat._getTracker("{{ keycode.keycode }}");pageTracker._trackPageview();} catch(err) {}</script>
	{% endifequal %}
{% endfor %}