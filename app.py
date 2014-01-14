# -*- coding: utf-8 -*-

import os
import fnmatch
import socket
import commands

from flask import Flask, send_from_directory, render_template, jsonify

# A bit hacky but in this way we seem to be getting the IP address on both Ubuntu and OS X:
try:
    HOST_IP = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0]
except:
    HOST_IP = commands.getoutput("/sbin/ifconfig").split("\n")[1].split()[1][5:]

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
EPUB_DIR = os.path.join(PROJECT_PATH, 'public', 'epub_content')

app = Flask(__name__, static_folder='public', static_url_path='')

@app.route("/")
def list_generated_epubs():
    def find_generated_epubs():
        for i in os.listdir(EPUB_DIR):
            if os.path.isdir(os.path.join(EPUB_DIR, i)):
                if os.path.exists(os.path.join(EPUB_DIR, i, "%s.epub" % i)):
                    yield {  'name': i, 'link' : "http://%s:5000/epub_content/%s/%s.epub" % (HOST_IP, i, i) }
                    
    generated_epubs = list(find_generated_epubs())
    address = "http://%s:5000/" % HOST_IP
    return render_template('generated_epubs.html', generated_epubs=generated_epubs, address=address)

@app.route("/index.html")
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
