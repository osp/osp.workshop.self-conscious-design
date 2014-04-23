import os
import json
import codecs

from xml.dom.minidom import parse

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
EPUB_DIR = os.path.join(PROJECT_PATH, 'public', 'epub_content')

obj = { "library_epubs" : [] }

def find_package(path):
    """
    Inside an epub folder, find the location of the package.opf
    If not found, return False
    """
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.opf'):
                return os.path.join(root, filename).replace(PROJECT_PATH + '/public/', '')
    return False

def parse_meta(path):
    meta = {}
    opf = parse(os.path.join('public', path))
    
    ti_e = opf.getElementsByTagName('dc:title')
    meta['title'] = ti_e[0].firstChild.data if len(ti_e) > 0 else u""
    
    a_e = opf.getElementsByTagName('dc:creator')
    meta['author'] = a_e[0].firstChild.data if len(a_e) > 0 else u""
    
    d_e = opf.getElementsByTagName('dc:description')
    meta['description'] = d_e[0].firstChild.data if len(d_e) > 0 else u""
    
    return meta

for i in os.listdir(EPUB_DIR):
    if os.path.isdir(os.path.join(EPUB_DIR, i)):
        this_epub_path = os.path.join(EPUB_DIR, i)
        if os.path.exists(os.path.join(EPUB_DIR, i, 'mimetype')):
            package = find_package(this_epub_path)
            if package:
                meta  = parse_meta(package)
                if not meta['title']:
                    meta['title'] = i.replace('_',' ').title()
                meta['epub_download'] = os.path.join('epub_content', i, '%s.epub' % i)
                meta['url_to_package_doc'] = package
                obj['library_epubs'].append(meta)

print json.dumps(obj, indent=2, ensure_ascii=False).encode('utf-8')
