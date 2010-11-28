{% for keycode in keycodes %}
	{% ifequal keycode.provider "yandex" %}
		<div style="display:none;"><script type="text/javascript">
		(function(w, c) {
		    (w[c] = w[c] || []).push(function() {
			try {
			    w.yaCounter{{ keycode.keycode }} = new Ya.Metrika({{ keycode.keycode }});
			     yaCounter{{ keycode.keycode }}.clickmap(true);
			     yaCounter{{ keycode.keycode }}.trackLinks(true);
		
			} catch(e) {}
		    });
		})(window, 'yandex_metrika_callbacks');
		</script></div>
		<script src="//mc.yandex.ru/metrika/watch.js" type="text/javascript" defer="defer"></script>
		<noscript><div style="position:absolute"><img src="//mc.yandex.ru/watch/{{ keycode.keycode }}" alt="" /></div></noscript>
	{% endifequal %}
	{% ifequal keycode.provider "google" %}
		<script type="text/javascript">var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));</script>
		<script type="text/javascript">try{var pageTracker = _gat._getTracker("{{ keycode.keycode }}");pageTracker._trackPageview();} catch(err) {}</script>
	{% endifequal %}
{% endfor %}
