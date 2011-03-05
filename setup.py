############################################################################################################################
#   setup.py                                                                                                               #
#                                                                                                                          #
#   Copyright 2011 Vasudev Kamath <kamathvasudev@gmail.com>                                                                #
#                  Santhosh Thottingal <santhosh.thottingal@gmail.com>                                                     #
#                                                                                                                          #
#   This program is free software; you can redistribute it and/or modify                                                   #
#   it under the terms of the GNU  General Public License as published by                                                  #
#   the Free Software Foundation; either version 3 of the License, or                                                      #
#   (at your option) any later version.                                                                                    #
#                                                                                                                          #
#   This program is distributed in the hope that it will be useful,                                                        #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of                                                         #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                                                          #
#   GNU General Public License for more details.                                                                           #
#                                                                                                                          #
#   You should have received a copy of the GNU General Public License                                                      #
#   along with this program; if not, write to the Free Software                                                            #
#   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,                                                             #
#   MA 02110-1301, USA.                                                                                                    #
############################################################################################################################



import os
from setuptools import setup, find_packages

module_name='hyphenator'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description=(
        read('README.md')
        + '\n' 
        )


setup(
    name = module_name,
    version = "0.1b1",
    url="http://gitorious.org/hyphenator",
    license = "LGLP 3.0",
    description = "Hyphenation module for Python",
    author = "Santhosh Thottingal",
    author_email = "santhosh.thottingal@gmail.com",
    long_description = long_description,
    package = find_packages('src'),
    package_dir = {'' : 'src'},
    setup_requires = ['setuptools-git'],
    namespace_packages = ['hyphenator'],
    include_package_data = True,
    install_requires = ['setuptools'],
    zip_safe = False,
    )
