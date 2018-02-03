# cucudb

cucudb is lightweight, fast, and simple database based on the [ujson](https://pypi.python.org/pypi/ujson/)

### How to use

```
    >>> import cucudb

    >>> db = cucu.load('test.db', False)

    >>> db.set('key', 'value')

    >>> db.get('key')
    'value'

    >>> db.dump()
    True
```

### How to install
```
$ pip install cucudb
```


### Links

* [website](http://packages.python.org/cucudb/)
* [documentation](http://cucudb.readthedocs.io)
* [pypi](http://pypi.python.org/pypi/cucudb)
