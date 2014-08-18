pyregdom - Python library for Mozilla Public Suffix list
========================================================

A Python version of `usrflo's regdom
libs <https://github.com/usrflo/registered-domain-libs>`_ to detect the
registered domain for a given domain name, based on `Mozillas effective
TLD listing <https://publicsuffix.org/list/>`_.

Installation
============

From source code: ``$ sudo python setup.py install`` Using ``pip``:
``$ pip install pyregdom`` Usage ===== \`\`\`python >>> import regdom

            regdom.get\_registered\_domain("mail.google.com")
            'google.com'

            regdom.get\_registered\_domain("foobar.github.io")
            'foobar.github.io'

            regdom.get\_registered\_domain("a.b.c.city.kawasaki.jp")
            'city.kawasaki.jp'

            regdom.get\_registered\_domain("invalid\_domain\_name.com")
            # return None

            regdom.get\_registered\_domain("not-recognized-tld.smile")
            'not-recognized-tld.smile'

            regdom.get\_registered\_domain("not-recognized-tld.smile",
            fallback=False) # return None \`\`\`

Update the list
===============

Simply run the script ``generate_effective_tlds.py`` under ``scripts``
directory, it will download and parse the latest `Mozilla Public
Suffix <https://publicsuffix.org/list/>`_
``$ scripts/generate_effective_tlds.py`` Then re-install the module from
source.

You can also use your own list file:
``$ scripts/generate_effective_tlds.py your_own_list_file.dat`` The
script doesn't check for the format of the file so make sure you have it
in the same format defined at `Mozilla Public
List <https://publicsuffix.org/list/>`_.

Author of this module will also update ``pyregdom`` on pypi every month
if there are changes in the list.
