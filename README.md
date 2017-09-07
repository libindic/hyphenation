# LibIndic N-gram Generator
[![Build Status](https://travis-ci.org/libindic/hyphenation.svg?branch=master)](https://travis-ci.org/libindic/hyphenation)
[![Coverage Status](https://coveralls.io/repos/github/libindic/hyphenation/badge.svg?branch=master)](https://coveralls.io/github/libindic/hyphenation?branch=master)

# LibIndic Hyphenation

LibIndic's Hyphenation module was inspired from the hyphenator module written by
Wilbert Berendsen <wbsoft at xs4all nl> (original module is avaialble at
http://pypi.python.org/pypi/hyphenator/0.5.1.). It was enhanced to include indic
hyphenation pattern and a hyphenation function which works by taking text input
and language and hyphenation symbol(optional) as shown in below examples. 

If you want it to work with other language you need to place the proper rules
under libindic/hyphenator/rules folder before compiling it.

## Installation
1. Clone the repository `git clone https://github.com/libindic/hyphenation.git`
2. Change to the cloned directory `cd hyphenation`
3. Run setup.py to create installable source `python setup.py sdist`
4. Install using pip `pip install dist/libindic-hyphenation*.tar.gz`

## Usage
```
>>> from libindic.hyphenation import Hyphenator
>>> instance = Hyphenator()
>>> result = instance.hyphenate(u"ഒഴിച്ചുകൂടാനാവാത്ത", hyphen="-")
ml_IN################################
>>> print(result)
ഒഴി-ച്ചു-കൂ-ടാ-നാ-വാ-ത്ത 

# If no hyphen character is specified, soft hyphen (\u00AD) will be used by
# default
```

## Tests
Run tests with ``python setup.py test``

Read the [docs](http://hyphenation.rtfd.org) for more.
