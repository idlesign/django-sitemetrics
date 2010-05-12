import urllib, hashlib
from django import template
from django.db import models
from django.contrib.sites.models import Site

register = template.Library()
keycode = models.get_model('sitemetrics', 'Keycode')

@register.tag
def sitemetrics(parser, token):
    """
    Parses sitemetrics tag.
    
    Two notation types are possible:
        1. No arguments:
           {% sitemetrics %} 
           Used to render all metric counters registered and active for current site.
           This requires 'Admin site' and 'Sites' from Django contrib.
            
        2. Four arguments:
           {% sitemetrics by yandex for "138500" %}
           Used to render custom metric counter with custom counter-id.
           This is a simple template tag with no special requirements.
    
    """
    tokens = token.split_contents()
    tokensNum = len(tokens)
    
    if tokensNum == 1:
        # Notation Type 1
        currentSite = Site.objects.get_current()
        keycodes = currentSite.keycode_set.filter(active=True)
    elif tokensNum == 5:
        # Notation Type 2
        if tokens[1] == 'by' and tokens[3] == 'for':
            keycodes = [{ 'provider':tokens[2], 'keycode':tokens[4][1:-1] },]
        else:
            raise template.TemplateSyntaxError, "A five argument notation of %r tag should look like {%% sitemetrics by yandex for \"138500\" %%}." % tokens[0]    
    else:
        raise template.TemplateSyntaxError, "%r tag requires four or no arguments. E.g. {%% sitemetrics by yandex for \"138500\" %%} or {%% sitemetrics %%}." % tokens[0]
    
    return sitemetricsNode(keycodes)

class sitemetricsNode(template.Node):
    """Renders specified site metric counter from template."""
    
    def __init__(self, keycodes):
        self.keycodes = keycodes
        self.template = template.loader.get_template('sitemetrics/sitemetrics.tpl') 
        
    def render(self, context): 
        myContext =  template.Context({'keycodes': self.keycodes,})
        return self.template.render(myContext)
