#!/bin/bash

# no arguments: show available ebooks
if [ $# -eq 0 ]; then
    ls public/epub_content/ | grep -v epub_library.json
else
    if [ -d "public/epub_content/$1" ]; then
        echo "generating epub for $1"
        cd public/epub_content/$1
        rm -f $1.epub
        zip -X -Z store $1.epub mimetype
        zip -r $1.epub META-INF/ EPUB/
    else
        echo "Folder doesn’t exist"
        exit 64
    fi
fi



