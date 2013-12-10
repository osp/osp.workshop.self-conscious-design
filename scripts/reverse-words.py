#!usr/bin/env python
# -*-coding: utf-8 -*-

"""
frequency.Reader
frequency.Tailor
"""
"""
first we import needed libraries
- - -xml.dom.minidom helps us to detect the html tags - Because here we only want to play with the text of the story.
- - -nltk is Natural Language Toolkit. Here the function nltk.FreqDist calculate the frequency of the words.
- - - re is for regular expression operations. We use it to identify pattern and strings in the text.
"""
from xml.dom import Node
import xml.dom.minidom as minidom
import re
import codecs

"""
Here we define the path to the command arguments - so that we can launch this script in the Terminal as follows :
frequency-test.py yourxhtmlfilename.xhtml thenameoftheoutputfile.xhtml
"""
from sys import argv

path = argv[1]
savepath = argv[2]

"""here we precise that the variable 'parsedoc' correspond to the function 'minidom.parse'"""
parseddoc = minidom.parse (path)

def reverseText (element):
    for child in element.childNodes:
        if child.nodeType == Node.TEXT_NODE:
            text = child.data
            words = text.split(' ')
            words.reverse()
            child.data = ' '.join (words)
        else:
            child = reverseText (child)
            
    return element

"""defining other variables"""
reverseText (parseddoc.getElementsByTagName ('body')[0])

h = codecs.open (savepath, 'w', 'UTF-8')
parseddoc.writexml (h)

