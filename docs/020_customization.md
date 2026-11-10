Customizing sitemetrics
=======================

Here we'll talk on how you can customize **sitemetrics** to your needs.


Customizing metric counters
---------------------------

Some metrics providers allows you to adjust metrics settings, thus changing counters code.

In **sitemetrics** counters are described in classes, so you can adjust counters 
functionality by customizing class attributes values.

Let' try and customize the built-in `Yandex Metrics` counter:

1. First, we define our new customized class somewhere within your project,
   (let's say, `my_counters.py` inside `my_app` application):

   .. code-block:: python
     
        from sitemetrics.providers import Yandex

        # We inherit from the built-in Yandex Metrics counter class.
        class MyYandexProvider(Yandex):

            title = 'My Yandex Metrika'  # This is to differentiate from parent.
       
            def __init__(self):
                # Parent class has `webvisor` counter param set to True,
                # bu we don't want that functionality and disable it.
                self.params['webvisor'] = False

           
2. Second, we introduce our class to Django, putting `SITEMETRICS_PROVIDERS` tuple 
   into projects' `settings.py`:

   .. code-block:: python
        
       # Below is a tuple with classes paths to your metrics counters classes.
       # We have just one.
       SITEMETRICS_PROVIDERS = ('my_app.my_counters.MyYandexProvider',)


Implementing new metrics providers
----------------------------------

1. Implement a class describing counter aspects, somewhere within your project,
   (let's say, `my_metrics.py` inside `my_app` application):

   .. code-block:: python
     
        from sitemetrics.providers import MetricsProvider

        # We inherit from the built-in MetricsProvider counter class.
        class MyMetrics(MetricsProvider):

            title = 'My Metrics'  # Human-friendly title.
            alias = 'my_metrics'  # Alias to address counter from templates.
       
            # And here are counter params, which are passed into counter template.
            params = {
                'my_param_1': True,
                'my_param_2': 30,
            }

2. Create a counter template (**sitemetrics** will search for it in`{your_app}/templates/sitemetrics/{provider_alias}.html`).
   
   `keycode` variable will be available within this template. `keycode.keycode` will contain counter identifier:

   .. code-block:: html

        keycode: {{ keycode.keycode }} 

        {% if keycode.my_param_1 %} 
            my_param_1 set to True, 
            my_param_2 is {{ keycode.my_param_2 }}
        {% endif %}


   The code above is of course not a real counter code, yet it can give you an idea on how to create a real one.

3. Now if you want to see your counter built into the **sitemetrics** fire an issue or a pull request at https://github.com/idlesign/django-sitemetrics/ or if you want to keep it private use `SITEMETRICS_PROVIDERS` definition approach (described in the previous section) to introduce your class to your Django project.


