Hyphenator - A Python based hyphenation module
==================================================
A Python hyphenation module. This module comes with Indic hyphenation
patterns. If you want it to work with other language you need to place
the proper rules under src/hyphenator/rules folder before compiling it

How to Install?
---------------
1. Clone the source code from Gitorious

    git://gitorious.org/hyphenator/hyphenator.git
    
2. Build and install using following command

    sudo python setup.py install
    
3. There is an alternative way to do this use following command

    sudo pip install hyphenator
    
How to use?
---------------
Simple usage of the module is shown below.
`from hyphenator import Hyphenator`
`h = Hyphenator()`
`h.hyphenate(text,language)`

If you want to change hyphenation symbol used then you can do that
by specifying 3rd argument
`from hyphenator import Hyphenator`
`h = Hyphenator()`
`h.hyphenate(text,language,hyphen='-')`

By default module will use soft hyphen (\u00AD)



