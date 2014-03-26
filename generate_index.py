import os
import json

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

for i in os.listdir(EPUB_DIR):
    if os.path.isdir(os.path.join(EPUB_DIR, i)):
        this_epub_path = os.path.join(EPUB_DIR, i)
        if os.path.exists(os.path.join(EPUB_DIR, i, 'mimetype')):
            package = find_package(this_epub_path)
            if package:
                obj['library_epubs'].append( { 
                        'title' : i.replace('_',' ').title(),
                        'url_to_package_doc' : package } )

print json.dumps(obj, indent=2, ensure_ascii=False)
