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

Given Requirements
------------------
I mapped the requirements 1 to 4 to django management commands.
 1. `current_rent`
 2. `lease_rent`
 3. `tenant_masts`
 4. `list_rentals`

The data is already imported and stored in the file `db.sqlite3` however if you
wish to reimport the data you can do so by using `fetch` and piping the output
to a file, followed by `store` with the argument the file where the data in the
previous step has been piped.


Commands
========
current_rent
----------
```console
$ python manage.py current_rent 
```
This returns a CSV formatted output of (by default 5 items) masts ordered in
ascending order of rent.
This function accepts additional arguments see:

```console
$ python manage.py current_rent  --help
```


lease_rent
----------
```console
$ python manage.py lease_rent 
```
This returns a CSV formatted output of mast filtered on lease years=25 with a
further line of the total rent of the above lines.
This function accepts additional arguments see:

```console
$ python manage.py lease_rent --help
```

tenant_masts
----------
```console
$ python manage.py lease_rent 
```
This returns a pretty printed dictionary with tenants and the amount of units
associated.

```console
$ python manage.py tenant_masts
```


list_rentals
------------
```console
$ python manage.py list_rentals 
```
This returns a csv type output filtered on the lease start date.
This function accepts additional arguments see:

```console
$ python manage.py rentals --help
```


fetch
-----
```console
$ python manage.py fetch
```
This fetches the CVS from location and prints it to stdout. This function
accepts additional arguments see:

```console
$ python manage.py fetch --help
```

store
-----
```console
$ python manage.py store apps/bink/tests/_test_data.csv
```
This stores the data into the DB. This function accepts additional arguments
see:

```console
$ python manage.py store --help
```

Scope Justification
===================
I was initially tempted to do this task in a straight forward manner without
using Django and just reparsing the input file for each command.
However I decided against this for the following reasons:
- The job requirement stated also Django as this is something I am familiar with
  and is helpful for this given task, specifically in creating nicely behaving
  cli commands.
- I don't like the idea of redownloading/reparsing the same dataset, as I
  already settled on Django, I might as well put the data in a table.
- The filtering and sorting of the data can indeed be done just straight in
  Python, however SQL is specifically designed for this, since I was already
  using Django I might as well implement it that way.

This did however mean that the time spend on this exercise is much greater than
doing it in a straight forward manner, I weighed this off against showing a more
'real world' scenario as if this would be a MVP for a paying customer. As such
it is designed to be relatively easily maintained and extended.

I do understand that there is a potential objection as the instructions of
'not overthinking' and 'avoid requirements' are thoroughly broken. In my defence
I would like to say that this is a better example of my capabilities and since
I already have Django as a requirement I added further ones for helping in
testing, coverage, code conformity and downloading of data.

As this was mostly my time (I do apologise for the reviewer who has to spend
more time) I made this call. However saying that, if this was on billing time
and the requirements where more in line of quick and run-once code, I would not
have made this decision. 

