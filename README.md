Bink Coding Exercise
====================

Preliminary
-----------
I used Django framework for it's convenience of creating database tables and
other tools I frequently use.
However I am not using any of the web features itself but instead use the 
build-in command features. Generally I use Django in a way that all apps are
created in their own app container so that the app is better separated from the
Django server parts itself and I have the option to create later on a portable
app from it.

In the folder `_project\environment.txt` you find the environment I have created
this project in. However it should be reasonably portable (though not tested)
and just creating an environment where the `requirements.txt` are installed
should be enough to use this project.

Commands
========
fetch
-----
```console
$ python manage.py fetch
```
This fetches the CVS from location and prints it to stdout. For help do:

```console
$ python manage.py fetch --help
```

store
-----
```console
$ python manage.py store apps/bink/tests/_test_data.csv
```
This stores the data into the DB. For help do:

```console
$ python manage.py store --help
```
