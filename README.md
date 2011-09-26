hyphenation - A Python based hyphenation module based hyphenator module from Wilbert Berendsen
=======================================================================================
A Python hyphenation module.This module was originally written 
by Wilbert Berendsen <wbsoft at xs4all nl> and original module 
is avaialble at http://pypi.python.org/pypi/hyphenator/0.5.1.
This module is later modified by Santhosh Thottingal to include
indic hyphenation pattern and a hyphenation function which works
by taking text input and language and hyphenation symbol(optional)
as shown in below examples.
If you want it to work with other language you need to place
the proper rules under src/hyphenator/rules folder before compiling it.

PS: This module is same as hyphenator module but this includes Indian Language
hyphenation patterns some modifications to choose hyphenation patterns automatically
by using ISO language codes

How to Install?
---------------
1. Clone the source code from Gitorious

    git://gitorious.org/hyphenator/hyphenator.git
    
2. Build and install using following command

    sudo python setup.py install
    
3. There is an alternative way to do this use following command

    sudo pip install hyphenation
    
How to use?
---------------
Simple usage of the module is shown below.
`from hyphenation import Hyphenator`
`h = Hyphenator()`
`h.hyphenate(text,language)`

If you want to change hyphenation symbol used then you can do that
by specifying 3rd argument
`from hyphenation import Hyphenator`
`h = Hyphenator()`
`h.hyphenate(text,language,hyphen='-')`

By default module will use soft hyphen (\u00AD)



