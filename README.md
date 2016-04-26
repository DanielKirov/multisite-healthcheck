# multisite-healthcheck
A multisite healthcheck app for Django.

Installation
------------

Dependencies:
This app requires django>=1.4.0 and requests>=2.3.0

1. Run ``` pip install multisite-healthcheck ```
2. Add ``` multi_health ``` to INSTALLED_APPS
3. Include urls in your ``` urls.py ``` file, e.g.:
```
from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    ...
    url(r'^multihealth/', include('multi_health.urls')),
    ...
    )
```
4. Run ``` python manage.py syncdb --migrate ``` if Django<1.7 or ```python manage.py migrate``` if Django>=1.7.


Configuration
-------------

There are two settings that you need to add in your settings.py:

1. **SITES_TO_CHECK** - a list of site IDs that you want to be checked by the app, e.g.:
```
SITES_TO_CHECK = [1, 2, 3, 5, 6, 8]
```
2. **TIME_PER_SITE** - How often should the app check a site, in seconds.
For example, if you have ``` TIME_PER_SITE = 5 ``` and you have 6 sites in your **SITES_TO_CHECK**
the app will take at least 30 seconds to go through all sites.


Running the app
---------------

The checking of sites happens with a management command. To run the command type
```
python manage.py multisite_healthcheck
```

This command will run infinitely. You will need to manually stop it for the process to end.

The command will read the list of sites defined in settings, get a Site object for each site id, and send a request
to the domain of that Site object. It will then store in the **URLStatusLog** table whether the status of the response
from the site was a 200 or not (**site_is_up**) and when the check was performed (**latest_update**).

The app has a view which renders all the rows in **URLStatusLog**.
If any of the rows have a **site_is_up** that is False, the view will render the page with a status code of 500.
In addition, the view checks if any of the rows in the **URLStatusLog** table are stale.
A row is stale if it hasn't been updated for a certain amount of time, which is calculated in the following way:
``` (len(SITES_TO_CHECK) * TIME_PER_SITE) + TIME_PER_SITE ```
In this case the view will render the page with a 500 status code.
