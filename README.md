pyregdom - Python library for Mozilla Public Suffix list
========

A Python version of [usrflo's regdom libs](https://github.com/usrflo/registered-domain-libs) to detect the registered domain for a given domain name, based on Mozillas effective TLD listing.

Installation
====
From source code:
```
    $ sudo python setup.py install
```
Using `pip`:
```
    $ pip install pyregdom
```
Usage
=====
```python
>>> import regdom
    
>>> regdom.get_registered_domain("mail.google.com")
'google.com'
    
>>> regdom.get_registered_domain("foobar.github.io")
'foobar.github.io'
    
>>> regdom.get_registered_domain("a.b.c.city.kawasaki.jp")
'city.kawasaki.jp'
    
>>> regdom.get_registered_domain("invalid_domain_name.com") # return None    
  
>>> regdom.get_registered_domain("not-recognized-tld.smile")
'not-recognized-tld.smile'
    
>>> regdom.get_registered_domain("not-recognized-tld.smile", fallback=False) # return None
```

Update the list
=====

Simply run the script `generate_effective_tlds.py` under `scripts` directory:
```
    $ scripts/generate_effective_tlds.py
``` 
Then re-install the module from source.

Author of this module will also update `pyregdom` on pypi every month if there are changes in the list.


