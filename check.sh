#!/bin/bash

# no arguments: show available ebooks
if [ $# -eq 0 ]; then
    ls public/epub_content/ | grep -v epub_library.json
else
    if [ -d "public/epub_content/$1" ]; then
        echo "checking epub $1"
        java -jar ~/src/epubcheck-3.0.1/epubcheck-3.0.1.jar public/epub_content/$1/$1.epub
    else
        echo "Folder doesn’t exist"
        exit 64
    fi
fi



