# -*- coding: utf-8 -*-

import os
import fnmatch

from flask import Flask, send_from_directory, jsonify

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
EPUB_DIR = os.path.join(PROJECT_PATH, 'public', 'epub_content')

app = Flask(__name__, static_folder='public', static_url_path='')

@app.route("/")
def static_home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/epub_content/epub_library.json")
def epub_titles():
    """
    This is a list of available eBooks.
    
    We look in the library folder to determine which folders look like eBooks,
    so we do not have to update this by hand.
    """
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
    return jsonify(obj)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
