# Customizing sitemetrics

Here we'll talk on how you can customize **sitemetrics** to your needs.

## Customizing metric counters

Some metrics providers allows you to adjust metrics settings, thus changing counters code.

In **sitemetrics** counters are described in classes, so you can adjust counters
functionality by customizing class attributes values.

Let' try and customize the built-in `Yandex Metrics` counter:

1. First, we define our new customized class somewhere within your project
   (let's say, `my_counters.py` inside `my_app` application):

    ```python
    from sitemetrics.providers import Yandex


    # We inherit from the built-in Yandex Metrics counter class.
    class MyYandexProvider(Yandex):

        title = 'My Yandex Metrika'  # This is to differentiate from parent.

        def __init__(self):
            # Parent class has `webvisor` counter param set to True,
            # bu we don't want that functionality and disable it.
            self.params['webvisor'] = False
    ```

2. Second, we introduce our class to Django, putting `SITEMETRICS_PROVIDERS` tuple
   into projects' `settings.py`:

    ```python
    # Below is a tuple with classes paths to your metrics counters classes.
    # We have just one.
    SITEMETRICS_PROVIDERS = ('my_app.my_counters.MyYandexProvider',)
    ```
