"""
frequency.Reader
frequency.Tailor
"""

from xml.dom import Node
import xml.dom.minidom as minidom
import nltk
import re

from sys import argv

path = argv[1]
savepath = argv[2]

parseddoc = minidom.parse (path)

def getTextValue (element):
    text = ''
    
    for child in element.childNodes:
        if child.nodeType == Node.TEXT_NODE:
            text += child.data
        else:
            text += getTextValue (child)
            
    return text

text = getTextValue (parseddoc.getElementsByTagName ('body')[0])
tokens = nltk.word_tokenize(text.lower())
freqs = nltk.FreqDist (tokens)
words = freqs.keys ()

source = open (path, 'r').read ()

for word in words[:10]:
    print word
    source = re.sub (u'((?<=\s|\'|\.|(?<!class="frequent")>)|^)({0})(?=\s|\.|,|-|$)'.format (word), '<span class="frequent">\\2</span>', source, flags=re.I)
    
newFile = open (savepath, 'w   ')
newFile.write (source)