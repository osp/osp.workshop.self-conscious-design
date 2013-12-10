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
import nltk
import re

"""
Here we define the path to the command arguments - so that we can launch this script in the Terminal as follows :
frequency-test.py yourxhtmlfilename.xhtml thenameoftheoutputfile.xhtml
"""
from sys import argv

path = argv[1]
savepath = argv[2]

"""here we precise that the variable 'parsedoc' correspond to the function 'minidom.parse'"""
parseddoc = minidom.parse (path)

def getTextValue (element):
    text = ''
    
    for child in element.childNodes:
        if child.nodeType == Node.TEXT_NODE:
            text += child.data
        else:
            text += getTextValue (child)
            
    return text

"""defining other variables"""
text = getTextValue (parseddoc.getElementsByTagName ('body')[0])
tokens = nltk.word_tokenize(text.lower())
freqs = nltk.FreqDist (tokens)
words = freqs.keys ()

source = open (path, 'r').read ()
replacewordmax = 10
i = 0

"""selection of the 10 most frequent words"""
for word in words:
    """
    Then we use grep to add span tags with a specific class around the words we want to highlight. 
    This regular expression operation look for the words (part of the list of 10 we just build) 
    preceded by a closing chevron, a space, a dot, an apostrophe or at the beginning a sentence (so with a capital letter)
    and followed by a dot, a coma, a dash or the end of a line,
    and add the span tag around it.
    """
    print word
    if re.match ('^[a-z]+', word):
        source = re.sub (u'((?<=\s|\'|\.|(?<!class="frequent")>)|^)({0})(?=\s|\.|,|-|$)'.format (word), '<span class="frequent">\\2</span>', source, flags=re.I)
        i += 1
        
        if i >= 10:
            break
    
newFile = open (savepath, 'w   ')
newFile.write (source)


