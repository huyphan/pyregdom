pyregdom - Python library for Mozilla Public Suffix list
========

A Python version of [usrflo's regdom libs](https://github.com/usrflo/registered-domain-libs) to detect the registered domains for given hostnames, based on [Mozillas effective TLD listing](https://publicsuffix.org/list/).

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

Simply run the script `generate_effective_tlds.py` under `scripts` directory, it will download and parse the latest [Mozilla Public Suffix](https://publicsuffix.org/list/)
```
    $ scripts/generate_effective_tlds.py
``` 
Then re-install the module from source.

You can also use your own list file:
```
    $ scripts/generate_effective_tlds.py your_own_list_file.dat
``` 
The script doesn't check for the format of the file so make sure you have it in the same format defined at [Mozilla Public List](https://publicsuffix.org/list/). 

Author of this module will also update `pyregdom` on pypi every month if there are changes in the list.


